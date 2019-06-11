import cv2
import sys

image1 = cv2.imread('triangle.jpg')
image2 = cv2.imread('circle.jpg')

new = []
for i in range(image1.shape[0]):
    row = []
    for j in range(image1.shape[1]):
        col = []
        if i < image2.shape[0] and j < image2.shape[1]:
            diff = []
            for k in range(image1.shape[2]):
                diff.append(image1[i, j][k] - image2[i, j][k])
            allZero = True
            for i in diff:
                if i != 0:
                    allZero = False
            if allZero:
                col = image1[i, j]
            else:
                col.append(image1[i, j])
                col.append(image2[i, j])
        row.append(col)
    new.append(row)

print(sys.getsizeof(new))
