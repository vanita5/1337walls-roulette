#!/usr/bin/python

import os
import sys
import argparse
import requests
import urllib.parse
from subprocess import call
from PIL import Image, ImageFilter

__version__ = '0.1.5'
__author__ = 'vanita5'

__api_url__ = 'http://1337walls.w8l.org/api/?'
__api_params__ = { 'rows': '', 'count': 1, 'order_by': 'rand', 'format': 'raw', 'client': 'de.vanita5.1337wallsroulette' }
__home_dir__ = os.path.expanduser("~") + '/.config/1337walls/'

DEBUG = False
VERBOSE = False

def console_out(format_str, *args, **kwargs):
    if VERBOSE or DEBUG:
        print(format_str.format(*args, **kwargs))
        
def console_debug(format_str, *args, **kwargs):
    if DEBUG:
        sys.stderr.write(format_str.format(*args, **kwargs))
        sys.stderr.write(os.linesep)
        
def console_error(format_str, *args, **kwargs):
    sys.stderr.write(format_str.format(*args, **kwargs))
    sys.stderr.write(os.linesep)

def console():
    # http://docs.python.org/library/argparse.html#module-argparse
    parser = argparse.ArgumentParser(description='No arguments needed')
    parser.add_argument("--version", action='version', version="%(prog)s {}".format(__version__))
    parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', help="show output")
    parser.add_argument("-b", "--blur", dest="blur", action='store_true', help="blur the image")
    parser.add_argument("-r", "--resolution", dest="resolution", help="270p, 720p or 1080p")
    parser.add_argument("--debug", dest="debug", action='store_true', help="turn on more verbose output")
    parser.add_argument("--dry", dest="dry", action='store_true', help="dry run, does not run nitrogen/feh")
    parser.add_argument("--use-feh", dest="feh", action='store_true', help="use feh to set the wallpaper (standard: nitrogen)")
   
    args = parser.parse_args()
    
    global DEBUG
    global VERBOSE
    DEBUG = args.debug
    VERBOSE = args.verbose
    blur = args.blur
    resolution = args.resolution
    dry = args.dry
    use_feh = args.feh

    if resolution not in ["270p", "720p", "1080p"]:
        resolution = "1080p"

    __api_params__["rows"] = resolution
    
    if not os.path.exists(__home_dir__):
        console_debug("Creating directory {}", __home_dir__)
        os.makedirs(__home_dir__)    

    console_out("Lurking on http://1337walls.w8l.org/...")
    r = requests.get(__api_url__ + urllib.parse.urlencode(__api_params__))
    
    if r.status_code != 200:
        console_out("Could not connect to the 1337walls API: {}", r.status_code)
        return

    console_out("Downloading image ({})", r.text)
    r = requests.get(r.text, stream=True)
    
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
    
    if not dry:
        console_out("Setting background image...")
        try:
            if use_feh:
                call(["feh", "--bg-fill", dir])
            else:
                call(["nitrogen", "--set-zoom-fill", dir, "--save"])
        except FileNotFoundError:
            console_error("[ERROR] {} needs to be installed!", "feh" if use_feh else "nitrogen")

    
if __name__ == "__main__":
    sys.exit(console())
