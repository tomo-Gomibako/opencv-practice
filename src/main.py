import cv2
import numpy as np
from pathlib import Path
from gui import Window

lenna = cv2.imread(str(Path("Lenna.png").resolve()))

Window(lenna).run()
