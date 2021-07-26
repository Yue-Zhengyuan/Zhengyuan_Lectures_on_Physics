import numpy as np
import sys
import os
from itertools import product

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
import matplotlib.lines as lines
plt.style.use('default')
# plt.style.use('dark_background')

from matplotlib import rcParams

dir_path = os.path.dirname(os.path.realpath(__file__))

def grid_color(n):
    if n == 0:
        color = 'black'
    else:
        color = 'cornflowerblue'
    return color

rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial"],
})

basis1 = np.array([[1,0], [0,1]])
basis2 = np.array([[1,-0.2], [-0.5, 1]])
basislist = [basis1, basis2]
vecComp = np.array([2,3])

arrow_kw = {'head_width': 0.2, 'head_length': 0.3, 'width': 0.03, 'length_includes_head': True}
text_kw = dict(fontsize=14)

# set up a figure twice as wide as it is tall
fig, axs = plt.subplots(1, 2, figsize=(6,3))
plt.subplots_adjust(left=0.04, right=0.96, bottom=0.05, top=0.95)
rangeX = (-2.5,2.5)
rangeY = (-1.5,3.5)
for basis, ax in zip(basislist, axs):
    ax.set_xlim(*rangeX)
    ax.set_ylim(*rangeY)
    ax.set_aspect(1)
    # turn off unnecessary axes
    ax.axis('off')
    # draw basis vector
    e1 = FancyArrow(0, 0, *basis[0], **arrow_kw, color='red')
    e2 = FancyArrow(0, 0, *basis[1], **arrow_kw, color='blue')
    ax.add_artist(e1)
    ax.add_artist(e2)
    # basis vector label
    ax.text(*(basis[0] + 0.1*basis[1]), r'$e_1$', **text_kw, color='red')
    ax.text(*(basis[1] + 0.1*basis[0]), r'$e_2$', **text_kw, color='blue')
    # draw vector
    vec = vecComp[0]*basis[0] + vecComp[1]*basis[1]
    v = FancyArrow(0, 0, *vec, **arrow_kw, color='green')
    ax.add_artist(v)
    # vector label
    ax.text(*(vec), r'$v$', **text_kw, color='green')
    # draw grid
    # grid along basis vectors
    alpha = np.linspace(-10,10,10)
    ax.text(-0.3, -0.3, 'O', **text_kw)
    for n in range(-10,10):
        ## parallel to e1
        line1 = np.transpose(np.array([a * basis[0] + n * basis[1] for a in alpha]))
        ## parallel to e2
        line2 = np.transpose(np.array([a * basis[1] + n * basis[0] for a in alpha]))
        ax.plot(line1[0], line1[1], color=grid_color(n), zorder=0)[0]
        ax.plot(line2[0], line2[1], color=grid_color(n), zorder=0)[0]
        # add axis ticks
        if n != 0:
            # x tick
            pos = n * basis[0]
            if rangeX[0]-0.5 < pos[0] < rangeX[1]+0.5:
                ax.text(*(pos - 0.4*basis[1]), str(n), **text_kw)
            # y tick
            pos = n * basis[1]
            if rangeY[0]-0.5 < pos[1] < rangeY[1]+0.5:
                ax.text(*(pos - 0.4*basis[0]), str(n), **text_kw)

plt.show()
fig.savefig(dir_path + '/different_basis.svg')
