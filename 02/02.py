import skimage.io as io
import scipy.ndimage as ndi
from numpy import array
from numpy import float32
from matplotlib.pyplot import figure

c = io.imread("cameraman.png")
f = array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
cf2 = ndi.convolve(float32(c), f, mode="constant")
maxcf2 = cf2.max()
mincf2 = cf2.min()
cf2f = (cf2 - mincf2) / (maxcf2 - mincf2)

figure(), io.imshow(cf2f)
figure(), io.imshow(cf2/60, vmax=1.0, vmin=0.0, cmap ="gray")

