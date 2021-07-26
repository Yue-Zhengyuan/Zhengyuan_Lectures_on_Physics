import numpy as np
import sys
import os
from itertools import product

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Polygon, Arc
import matplotlib.lines as lines
plt.style.use('default')
# plt.style.use('dark_background')

from matplotlib import rcParams

dir_path = os.path.dirname(os.path.realpath(__file__))

# from mpl_toolkits.mplot3d.axes3d import get_test_data

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
x = np.pi/6
basis2 = np.array([[np.cos(x), np.sin(x)], [-np.sin(x), np.cos(x)]])
bases = [basis1, basis2]
colors = ['red', 'blue']
vecComp = np.array([1,1])

arrow_kw = {'head_width': 0.1, 'head_length': 0.2, 'width': 0.02, 'length_includes_head': True}
text_kw = dict(fontsize=14)

# set up a figure twice as wide as it is tall
fig, ax = plt.subplots(1, 1, figsize=(3,3))
fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)
rangeX = (-1.5, 1.5)
rangeY = (-1, 2)
ax.set_xlim(*rangeX)
ax.set_ylim(*rangeY)
ax.set_aspect(1)
# turn off unnecessary axes
ax.axis('off')

for i, basis in enumerate(bases):
    if i == 0:
        alpha = 0.3
    else: 
        alpha = 1 
    # draw vector
    e1 = FancyArrow(0, 0, *basis[0], **arrow_kw, color='red', alpha=alpha)
    e2 = FancyArrow(0, 0, *basis[1], **arrow_kw, color='blue', alpha=alpha)
    vec = vecComp[0]*basis[0] + vecComp[1]*basis[1]
    v = FancyArrow(0, 0, *vec, **arrow_kw, color='green', alpha=alpha)
    ax.add_artist(e1)
    ax.add_artist(e2)
    ax.add_artist(v)
    # draw aux parallelogram
    if i != 0:
        verts1 = [np.array([0,0]), basis[0,0]*np.array([1,0]),
                 basis[0], basis[0,1]*np.array([0,1])]
        aux1 = Polygon(verts1, linestyle='--', linewidth=1, edgecolor='red', fill=False)
        ax.add_artist(aux1)
        verts2 = [np.array([0,0]), basis[1,0]*np.array([1,0]),
                 basis[1], basis[1,1]*np.array([0,1])]
        aux2 = Polygon(verts2, linestyle='--', linewidth=1, edgecolor='blue', fill=False)
        ax.add_artist(aux2)
    # vector label
    if i == 0:
        ax.text(*(basis[0] + 0.1*basis[1]), r'$e_1$', **text_kw, color='red', alpha=alpha)
        ax.text(*(basis[1] + 0.1*basis[0]), r'$e_2$', **text_kw, color='blue', alpha=alpha)
        ax.text(*(vec), r'$v$', **text_kw, color='green', alpha=alpha)
    else:
        ax.text(*(basis[0] + 0.1*basis[1]), r'$e_1^\prime$', **text_kw, color='red', alpha=alpha)
        ax.text(*(basis[1] + 0.15*basis[0]), r'$e_2^\prime$', **text_kw, color='blue', alpha=alpha)
        ax.text(*(vec), r'$v^\prime$', **text_kw, color='green', alpha=alpha)
    # draw grid
    # grid along basis vectors
    alist = np.linspace(-10,10,10)
    if i == 0:
        ax.text(-0.2, -0.2, 'O', **text_kw)
    for n in range(-10,10):
        ## parallel to e1
        line1 = np.transpose(np.array([a * basis[0] + n * basis[1] for a in alist]))
        ## parallel to e2
        line2 = np.transpose(np.array([a * basis[1] + n * basis[0] for a in alist]))
        ax.plot(line1[0], line1[1], color=grid_color(n), zorder=0, alpha=alpha)[0]
        ax.plot(line2[0], line2[1], color=grid_color(n), zorder=0, alpha=alpha)[0]
# draw arc to indicate angle
arc1 = Arc((0,0), 0.6, 0.6, theta2 = 30, color='red', lw=1.5)
ax.text(0.37, 0.04, r'$\theta$', **text_kw, color='red')
arc2 = Arc((0,0), 0.6, 0.6, theta1=90, theta2 =120, color='blue', lw=1.5)
ax.text(-0.18, 0.4, r'$\theta$', **text_kw, color='blue')
ax.add_artist(arc1)
ax.add_artist(arc2)

plt.show()
fig.savefig(dir_path + '/rotation_2d.svg')
