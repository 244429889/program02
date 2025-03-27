import skimage.io as io
from matplotlib.pyplot import figure
import skimage.restoration as re

c = io.imread("cameraman.png")

ca = re.denoise_bilateral(c,win_size=5,sigma_color=0.2,sigma_spatial=2,mode='symmetric')
cb = re.denoise_bilateral(c,win_size=7,sigma_color=0.2,sigma_spatial=10,mode='symmetric')
cc = re.denoise_bilateral(c,win_size=11,sigma_color=0.1,sigma_spatial=3,mode='symmetric')
cd = re.denoise_bilateral(c,win_size=11,sigma_color=0.5,sigma_spatial=5,mode='symmetric')

figure(), io.imshow(ca)
figure(), io.imshow(cb)
figure(), io.imshow(cc)
figure(), io.imshow(cd)
