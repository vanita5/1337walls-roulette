1337walls Roulette
==================

1337walls Roulette automatically downloads a random wallpaper from [1337walls](http://1337walls.w8l.org/), blurs 
the image (optional) and sets it as your wallpaper.
This is intended for WM's like Openbox and uses nitrogen to set the desktop wallpaper!

Installation
------------
Dependencies:
[nitrogen](https://wiki.archlinux.org/index.php/nitrogen)
OR
[Feh](https://wiki.archlinux.org/index.php/feh)
    

Install 1337walls_roulette:

    pip install git+https://github.com/vanita5/1337walls-roulette
    
    
Usage
-----
Just run the following command. Your background should change!

    1337walls_roulette
    
Options:

    --version           Display version
    -b, --blur          Blur the wallpaper
    -r, --resolution    270p, 720p or 1080p
    -v, --verbose       Verbose output
    --debug             Even more output, for debug purposes
    --use-feh           Use feh to set your wallpaper instead of nitrogen (standard)
    
You can run this script on startup or setup a cronjob to update your background image automatically 
after a period of time.


License
-------

    /*
     * 1337walls Roulette
     *
     * Copyright (C) 2014 vanita5 <mail@vanita5.de>
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 3 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */
                                                                                                             
<a href="https://www.gnu.org/licenses/gpl-3.0.en.html"><img src="https://www.gnu.org/graphics/gplv3-127x51.png"><br/>GNU General Public License</a>
