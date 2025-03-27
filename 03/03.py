import skimage.io as io
import scipy.ndimage as ndi
from matplotlib.pyplot import figure

c = io.imread("cameraman.png")

c1 = ndi.gaussian_filter(c, 0.5, truncate=5)
c2 = ndi.gaussian_filter(c, 2, truncate=5)
c3 = ndi.gaussian_filter(c, 1, truncate=11)
c4 = ndi.gaussian_filter(c, 5, truncate=11)

figure(), io.imshow(c1)
figure(), io.imshow(c2)
figure(), io.imshow(c3)
figure(), io.imshow(c4)
