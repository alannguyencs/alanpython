from PIL import Image
import queue

"""
Given an image as 2D array with 0-255 values.
Define 2 pixels are connected if their distance is equal or smaller than "distance"
return a 2D array with biggest connected component.
"""


def isInsideBox(x, y, width, height):
    if x < 0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return True

def collectBiggestConnectedComponent(img, distance):
    pixdata = img.load()
    (width, height) = img.size
    q = queue.Queue()
    b = [[-1 for _ in range(height)] for _ in range(width)]
    connectedComponentID = 0
    NoConnectedPoints = []
    for i in range(width):
            for j in range(height):
                if pixdata[i, j] == 255 and b[i][j] == -1:
                    b[i][j] = connectedComponentID
                    q.put((i, j))
                    cnt = 0
                    while not q.empty():
                        cnt += 1
                        p = q.get()
                        for id1 in range (-distance, distance+1):
                            for id2 in range (-distance, distance+1):
                                if isInsideBox(p[0] + id1, p[1] + id2, width, height) \
                                        and pixdata[p[0] + id1, p[1] + id2] == 255 and b[p[0] + id1][p[1] + id2] == -1:
                                    b[p[0] + id1][p[1] + id2] = connectedComponentID
                                    q.put((p[0] + id1, p[1] + id2))

                    NoConnectedPoints.append(cnt)
                    connectedComponentID += 1


    mx = max(NoConnectedPoints)
    for i in range(width):
        for j in range(height):
            if NoConnectedPoints[b[i][j]] < mx:
                pixdata[i, j] = 0

    return img

#test the algorithm
test_img = Image.open("./test_data/biggest_component.png")
result_img = collectBiggestConnectedComponent(test_img, distance=1)
result_img.save("./test_data/biggest_component_result.png")