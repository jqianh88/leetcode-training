class Solution: 
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int):

        start_color = image[sr][sc]

        def flood_fill(x, y):
            print(x,y)
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] == color or image[x][y] != start_color:
                return 
            
            image[x][y] = color 

            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)

        flood_fill(sr, sc)
        return image
    


if __name__=='__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    self = Solution()

    print(self.floodFill(image=image, sr=sr, sc=sc, color=color))

    # Really need to work on recursion and OOP