#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Joel Cross
Date last modified: Oct. 22, 2020

This python script uses the Beautiful Soup module to scrape images
from any given pinterest board. The desktop wallpaper is then set to
rotate through the images in the specified board.
'''

import urllib.request
from urllib.request import urlopen, urlretrieve
import bs4 as bs
import os
import shutil
from subprocess import Popen, PIPE


# Creates "Scraped Images" directory to contain downloaded images
def makeScrapeDir():
    # Retrieve current directory
    currentDir = os.path.dirname(os.path.realpath(__file__)) 

    # Create "Scraped Images" directory (overwrite if already exists)
    if os.path.exists(currentDir + "/Scraped Images"):
        shutil.rmtree(currentDir + "/Scraped Images")
    os.makedirs(currentDir + "/Scraped Images")


# Returns path of folder containing downloaded images
def getScrapeDir():
    return os.path.dirname(os.path.realpath(__file__)) + "/Scraped Images"


# Downloaded images from pinterest board to "Scraped Images" directory
def scrapeImages(link, destPath):
    # Create beautiful soup object from pinterest link
    source = urlopen(link).read()
    soup = bs.BeautifulSoup(source, "html.parser")

    # Find all pins saved to specified board
    pins = soup.findAll("a", attrs={"data-test-id": "PinImageLink"})
    # Create list containing <img> tags of each pin
    imgTags = [pin.find("img") for pin in pins]

    # Iterate through list of <img> tags
    count = 1
    for imgTag in imgTags:
        # Download image, set appropriate file name
        urllib.request.urlretrieve(imgTag.get('src'), destPath + "/image" + str(count) + ".jpg")
        count += 1


# Sets desktop wallpaper to rotate through downloaded images
def setWallpaper(imgDir, delay):
    # AppleScript performs commands for MacOS
    script = '''
        tell application "System Events"
            tell current desktop
                set pictures folder to "''' + imgDir + '''"
                set picture rotation to 1 -- (0=off, 1=interval, 2=login, 3=sleep)
                set random order to true
                set change interval to ''' + delay + ''' -- in seconds
            end tell
        end tell'''

    # Run script
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)


def main():
    # Get user input
    boardLink = input("Board link: ")
    imageDelay = input("Image rotation delay (seconds): ")

    makeScrapeDir()
    scrapeImages(boardLink, getScrapeDir())
    setWallpaper(getScrapeDir(), imageDelay)

    print("Scrape complete. Enjoy your new wallpaper!")


if __name__ == "__main__":
    main()