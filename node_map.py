import cv2
import node_settings
def test_draw_pint():
    #path = r'world_rs_walker.png'
    path = r'world_rs_walker_AUG_2021.png'
    image = cv2.imread(path)
    coord = (90, 120)
    radius = 2
    color = (0, 0, 255)
    thickness = 0
    window_name = 'Image'
    # Using cv2.circle() method
    # Draw a point
    image = cv2.circle(image, coord, radius, color, thickness)
    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def world_graph_nodes():
    path = r'world_rs_walker_AUG_2021.png'
    img = cv2.imread(path, 1)

    df = node_settings.WorldGraph_Nodes
    # loop through each coordinate pair in arr
    for item in df:
        cv2.drawMarker(img, (item[0], item[1]), (0, 0, 255), markerType=cv2.MARKER_DIAMOND,
                       markerSize=3, thickness=1, line_type=cv2.LINE_AA)
    cv2.imwrite('RES_WALKER.png', img)
    #window_name = 'Image'
    #cv2.imshow(window_name, img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def world_graph_nodes_names():
    path = r'world_rs_walker_AUG_2021.png'
    img = cv2.imread(path, 1)
    df_Nodes = node_settings.WorldGraph_Nodes
    df_Names = node_settings.WorldGraph_Names
    df = df_Nodes
    # loop through each coordinate pair in arr
    index = 0
    for item in df:
        name = df_Names[index]
        cv2.circle(img, (item[0], item[1]), radius=2, color=(0, 0, 255), thickness=0)
        cv2.putText(img, name, (item[0], item[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        index += 1
    cv2.imwrite('RES_WALKER_NAMES_AUG.png', img)
    #window_name = 'Image'
    #cv2.imshow(window_name, img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def world_graph_nodes_names_paths():
    #path = r'world_rs_walker.png'
    path = r'world_rs_walker_AUG_2021.png'
    # store image file to variable
    img = cv2.imread(path, 1)
    # Store array of node points, the names of specific points and the available paths to each node
    df_Nodes = node_settings.WorldGraph_Nodes
    df_Names = node_settings.WorldGraph_Names
    df_Paths = node_settings.WorldGraph_Paths

    df = df_Nodes
    # loop through each coordinate pair in arr
    index = 0
    for item in df:
        #print(df_Paths[index])

        # using an index get the corresponding name and path array
        name = df_Names[index]
        path = df_Paths[index]

        # using cv2 draw a circle for the node points
        cv2.circle(img, (item[0], item[1]), radius=2, color=(0, 0, 255), thickness=-1)

        # using cv2 add the name text for the node names
        cv2.putText(img, name, (item[0], item[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        #line_pos = path[0]
        #print(line_pos)

        # itterate through each available path in the corresponding node
        for paths in path:
            cv2.line(img, (item[0], item[1]), (df[paths][0], df[paths][1]), (0, 255, 0), 1)

        # make sure index keeps in line with index position of node
        index += 1

    # overlay names = white text, paths = green lines and node = red dots on image map
    cv2.imwrite('RES_WALKER_NAMES_PATHS_AUG_2021.png', img)
    #window_name = 'Image'
    #cv2.imshow(window_name, img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def test_array_format():
    test_pos = [[4659, 2734], [4684, 2734], [4678, 2760], [4637, 2734]]
    test = [[1, 3, 5, 4, 6, 2], [0, 2, 6, 25]]
    index = 0
    position = test[index][1]
    print(test_pos[position])

#test_array_format()
#world_graph_nodes()
#world_graph_nodes_names()
world_graph_nodes_names_paths()
#test_draw_pint()