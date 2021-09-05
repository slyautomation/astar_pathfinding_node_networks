This project extracts the canvas data on https://www.osrsmap.net/ and converts each canvas display as an png file. This is done by exploiting html elements on the website and adding javascript parameter functions such as .toDataURL.


.toDataURL() method returns a data URI containing a representation of the image in the format specified by the type parameter (defaults to PNG). 


WebDriver is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.  


Download the chrome webdriver here: https://chromedriver.chromium.org/downloads


Base64 module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. 


This is useful converting the canvas data to a png file.


The next function merges those images by looping the interations of the canvas images, that results in the final product a full osrs map with icons and detailed.

The end result is a fully rendered old school runescape map.

https://github.com/slyautomation/astar_pathfinding_node_networks/blob/main/world_rs_walker_AUG_2021.png

![image](https://user-images.githubusercontent.com/81003470/132083438-57e61393-68b4-4bba-95f0-a3b99f79864c.png)


Youtube Tutorial: https://youtu.be/fbgUzBb2JVg

This is the second part to the tutorial on the auto walker for old school runescape using python. This tuttorial will cover how to visualise node points and assign them with available star paths. this will use opencv to read the image files and plot the points and lines for each node. 
The blueprint for the nodes was provided by ollydev's github library: https://github.com/ollydev/SRL-Development/blob/master/osr/walker/world.graph 

Once the node points and lines are plotted on the map the end product is a web of paths a player can take around most of Runescape.

https://github.com/slyautomation/astar_pathfinding_node_networks/blob/main/RES_WALKER_NAMES_PATHS_AUG_2021.png

![image](https://user-images.githubusercontent.com/81003470/132083487-f959dd9b-e0fb-4f44-819f-4a620d870613.png)

Youtube Tutorial: https://www.youtube.com/watch?v=W-ZAm7D7e2o

This is the final part to the tutorial on the auto walker for old school runescape using python. This tutorial will cover how the astar algo works and how we can use our points to find the shortest path throughout Runescape. The main function aStarAlgo uses sets, loops and arrays to calculate, store and output the desired shortest path. 

From the output we will use opencv to read the image map and take image snippets of the x and y points to use in template matching against the mini map.

![image](https://user-images.githubusercontent.com/81003470/132083506-912f65c4-b938-4582-bace-24e89d053984.png)

Youtube Tutorial: https://www.youtube.com/watch?v=RuTTs0RgZPo
