import skimage.color as co
import skimage.io as io
import skimage.util as ut
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

em = io.imread("emu.png")

if em.shape[-1] == 4:
    em = em[..., :3]
e = co.rgb2gray(em)

e2 = ut.img_as_ubyte(e)

figure(), io.imshow(em)
figure(), io.imshow(e)
figure(), io.imshow(e2)
plt.show()
plt.imshow(e2, cmap="gray")
