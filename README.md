# pinScraper
Sets desktop background to rotate through images in a specified Pinterest board. Script can be run from any location on MacOS.

## Functions
### makeScrapeDir
Creates a "Scraped Images" directory to contain the downloaded images.

### getScrapeDir
Returns the path of the directory containing the downloaded images.

### scrapeImages
Downloads images from the Pinterest board to the "Scraped Images" directory.
Parameter `link` represents the Pinterest board link.
Parameter `destPath` represents the path of the directory where the images are to be downloaded.

### setWallpaper
Sets the desktop wallpaper to rotate through the downloaded images at the speed specified by the user.
Parameter `imgDir` represents the path of the directory where the images are to be downloaded.
Parameter `delay`represents the interval at which the user wishes to have the images rotate.

### main
Gets user input, runs program, prints closing message.
