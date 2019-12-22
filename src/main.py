import cv2
import numpy as np
from pathlib import Path

lenna = cv2.imread(str(Path("Lenna.png").resolve()))

cv2.startWindowThread()
cv2.namedWindow("image")
cv2.imshow("image", lenna)
cv2.waitKey(0)
cv2.destroyAllWindows()
