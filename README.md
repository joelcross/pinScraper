# pinScraper
Sets desktop background to rotate through images in a specified Pinterest board.

## Functions
### makeScrapeDir
Creates a "Scraped Images" directory to contain the downloaded images.

### getScrapeDir
Returns the path of the directory containing the downloaded images.

### scrapeImages
Downloadeds images from the Pinterest board to the "Scraped Images" directory.
Takes parameters `link` and `destPath`, which represent the Pinterest board link and path of the folder in which to download the images, respectively.

### setWallpaper
Sets the desktop wallpaper to rotate through the downloaded images at the speed specified by the user.
Takes parameters `imgDir` and `delay`, which represent the path of the folder in which to download the images and the interval at which the user wishes to have the images rotate, respectively.

### main
Gets user input, runs program, prints closing message.
