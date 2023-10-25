'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Inputs: 
- image: m x n integer grid image 
- sr: int 
- sc: int
- color: int 

Outputs: 
- list of lists representing an m x n matrix
'''

def flood_fill(image: list, sr: int, sc: int, color: int) -> list:
    hashmap_image = {}
    for row, l  in enumerate(image):
        hashmap_image[row] = l

    start_pixel = hashmap_image[sr][sc]
    print(start_pixel)

    for i, row in enumerate(image):
        for j, column in enumerate(row): 
            if column == image[sr][sc] and (column == image[sr+1][sc] or column == image[sr+1][sc] or column == image[sr+1][sc])

if __name__=='__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2

    print(flood_fill(image=image, sr=sr, sc=sc, color=color))
    # Output = [[2,2,2],[2,2,0],[2,0,1]]
    # Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    # Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.


    '''
    Closest Neighbors: 
    https://samirkhanal35.medium.com/relationships-between-pixels-neighbours-and-connectivity-d38e473cd994#:~:text=a)%204%2Dconnectivity%3A%20Two,m%2Dadjacent%20with%20each%20others.
    Two pixels are said to be connected:

if they are adjacent in some sense(neighbour pixels,4/8/m-adjacency)
if their gray levels satisfy a specified criterion of similarity(equal intensity level)
There are three types of connectivity on the basis of adjacency. They are:

a) 4-connectivity: Two or more pixels are said to be 4-connected if they are 4-adjacent with each others.

b) 8-connectivity: Two or more pixels are said to be 8-connected if they are 8-adjacent with each others.

c) m-connectivity: Two or more pixels are said to be m-connected if they are m-adjacent with each others.
 

  '''