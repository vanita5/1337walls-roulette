#!/usr/bin/python

import os
import sys
import argparse
import requests
from subprocess import call
from random import choice
from PIL import Image, ImageFilter

__version__ = '0.1.1'
__author__ = 'vanita5'

__api_url__ = 'http://1337walls.w8l.org/api/?rows=image'
__home_dir__ = os.path.expanduser("~") + '/.config/1337walls/'

DEBUG = False
VERBOSE = False

def console_out(format_str, *args, **kwargs):
    if VERBOSE:
        print(format_str.format(*args, **kwargs))
        
def console_debug(format_str, *args, **kwargs):
    if DEBUG and VERBOSE:
        sys.stderr.write(format_str.format(*args, **kwargs))
        sys.stderr.write(os.linesep)

def console():
    # http://docs.python.org/library/argparse.html#module-argparse
    parser = argparse.ArgumentParser(description='No arguments needed')
    parser.add_argument("--version", action='version', version="%(prog)s {}".format(__version__))
    parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="show output")
    parser.add_argument("-b", "--blur", dest="blur", action='store_true', help="blur the image")
    parser.add_argument("--debug", dest="debug", action='store_true', help="turn on more verbose output")
    
    args = parser.parse_args()
    
    global DEBUG
    global VERBOSE
    DEBUG = args.debug
    VERBOSE = args.verbose
    blur = args.blur
    
    if not os.path.exists(__home_dir__):
        console_debug("Creating directory {}", __home_dir__)
        os.makedirs(__home_dir__)    
    
    console_out("Lurking on http://1337walls.w8l.org/...")
    r = requests.get(__api_url__)
    
    if r.status_code != 200:
        console_out("Could not connect to the 1337walls API: {}", r.status_code)
        return
        
    json = r.json()
    image = choice(json)
    url = image['image']
    
    console_out("Downloading image ({})", url)
    r = requests.get(url, stream=True)
    
    if r.status_code != 200:
        console_out("Could not download the image. Error code: {}", r.status_code)
        return
            
    console_out("Download successful!")
    
    dir = __home_dir__ + '1337_wp'
    with open(dir, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
            
    console_debug("Image temporarely saved to {}", f.name)
    
    if blur:
        console_out("Bluring image...")
        dir = __home_dir__ + "1337_wp_blurred.png"
        try:
            original = Image.open(f.name)
            blured = original.filter(ImageFilter.BLUR)
        
            blured.save(dir)
        except:
            console_out("[PIL] Unable to load image")
            return
    
    console_out("Setting background image...")
    call(["nitrogen", "--set-zoom-fill", dir, "--save"])
    
if __name__ == "__main__":
    sys.exit(console())
