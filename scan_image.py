import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


import sys
if len(sys.argv) == 2:
    nomImage = sys.argv[1]
else:
    print("Alternative: python scan_image.py <image>")
    nomImage = input("nom de l'image: ")

image = cv2.imread(nomImage)

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Données: ", obj.data, "\n")


def afficherImage(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
afficherImage(image)

