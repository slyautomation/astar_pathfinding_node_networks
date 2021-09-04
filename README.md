This project extracts the canvas data on https://www.osrsmap.net/ and converts each canvas display as an png file. This is done by exploiting html elements on the website and adding javascript parameter functions such as .toDataURL.


.toDataURL() method returns a data URI containing a representation of the image in the format specified by the type parameter (defaults to PNG). 


WebDriver is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.  


Download the chrome webdriver here: https://chromedriver.chromium.org/downloads


Base64 module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. 


This is useful converting the canvas data to a png file.


The next function merges those images by looping the interations of the canvas images, that results in the final product a full osrs map with icons and detailed.

Youtube Tutorial: https://youtu.be/fbgUzBb2JVg

This is the second part to the tutorial on the auto walker for old school runescape using python. This tuttorial will cover how to visualise node points and assign them with available star paths. this will use opencv to read the image files and plot the points and lines for each node. 
The blueprint for the nodes was provided by ollydev's github library: https://github.com/ollydev/SRL-Development/blob/master/osr/walker/world.graph 

Youtube Tutorial: https://www.youtube.com/watch?v=W-ZAm7D7e2o

This is the final part to the tutorial on the auto walker for old school runescape using python. This tutorial will cover how the astar algo works and how we can use our points to find the shortest path throughout Runescape. The main function aStarAlgo uses sets, loops and arrays to calculate, store and output the desired shortest path. 

From the output we will use opencv to read the image map and take image snippets of the x and y points to use in template matching against the mini map.

Youtube Tutorial: https://www.youtube.com/watch?v=de2XpHu_fJk
