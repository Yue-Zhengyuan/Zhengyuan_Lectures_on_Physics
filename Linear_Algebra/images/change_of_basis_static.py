"""
    Demostration of change of basis
    ===============================
    Author: Yue Zhengyuan

    Drag the basis vectors to see how the components
    of an arbitrary vector change

    Adapted from the StackOverflow answer
    https://stackoverflow.com/a/63568715/10444934
"""

import numpy as np
import os
from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon, FancyArrow

def grid_color(n):
    if n == 0:
        color = 'black'
    else:
        color = 'cornflowerblue'
    return color

# rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

plt.style.use('default')
# plt.style.use('dark_background')
dir_path = os.path.dirname(os.path.realpath(__file__))

rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial"],
})

# the whole figure
fig, ax = plt.subplots(1, 1, figsize=(4, 4))

# parameters for text
text_kw = dict(fontsize=14)
text_kw2 = dict(fontsize=14)

ax.set_xlim(-3.5, 4.5)
ax.set_ylim(-2.5, 5.5)
ax.set_aspect(1)
# axes go through origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
# turn off unnecessary axes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(left=False, bottom=False, labelsize=14)
# axis label
ax.text(4, 0.3, '$x$', **text_kw)
ax.text(0.3, 5, '$y$', **text_kw)
# set position of grid
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
# axis grid
ax.grid(True, which='major', linestyle='-', lw=1)
# ax.grid(True, which='minor', linestyle=':', lw=0.5)

def vecNewBasis(v, e1, e2):
    """Find components of v along e1, e2"""
    matD = np.array([e1, e2])
    return np.dot(np.linalg.inv(matD.T), np.array(v))

def vecLabelXY(v, start=(0,0)):
    """Determine the position of the vector label"""
    raise NotImplementedError
    # midpoint = tuple((v[i] + start[i])/2 for i in range(2))
    # # direction orthogonal to v
    # coord = midpoint
    # return coord

# locator of vectors
init_e1, init_e2, init_v = np.array([2,1]), np.array([-2,2]), np.array([2,3])
# basis vector and its label
# use empty annotation as arrow
arrow_kw = {'head_width': 0.2, 'head_length': 0.3, 'width': 0.03, 'length_includes_head': True}
e1New = FancyArrow(0, 0, *init_e1, **arrow_kw, color='red')
e1Label = ax.text(*(1.1*init_e1), '$e_1$', **text_kw, color='red')
e2New = FancyArrow(0, 0, *init_e2, **arrow_kw, color='blue')
e2Label = ax.text(*(1.1*init_e2), '$e_2$', **text_kw, color='blue')

# arbitrary vector
vOld = FancyArrow(0, 0, *init_v, **arrow_kw, color='green')
vLabel = ax.text(*(1.1*init_v), '$v$', **text_kw, color='green')
ax.add_artist(e1New)
ax.add_artist(e2New)
ax.add_artist(vOld)

# auxiliary lines
init_vNew = vecNewBasis(init_v, init_e1, init_e2)
verts = [np.array([0,0]), init_vNew[0]*init_e1,
        init_v, init_vNew[1]*init_e2,]
aux = Polygon(verts, linestyle='--', linewidth=1, edgecolor='black', fill=False)
ax.add_artist(aux)
# grid along basis vectors
alpha = np.linspace(-10,10,10)
grid1, grid2 = [], []
for n in range(-10,10):
    ## parallel to e1
    line1 = np.transpose(np.array([a * init_e1 + n * init_e2 for a in alpha]))
    ## parallel to e2
    line2 = np.transpose(np.array([a * init_e2 + n * init_e1 for a in alpha]))
    grid1.append(ax.plot(line1[0], line1[1], color=grid_color(n), zorder=0)[0])
    grid2.append(ax.plot(line2[0], line2[1], color=grid_color(n), zorder=0)[0])

plt.show()
fig.savefig(dir_path + '/change_of_basis.svg')