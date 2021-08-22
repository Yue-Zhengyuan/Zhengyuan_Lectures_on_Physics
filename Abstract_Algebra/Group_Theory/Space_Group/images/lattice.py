import numpy as np
from math import sqrt
from itertools import product
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def draw_lattice(basis, showfig=False):
    fig, ax = plt.subplots(figsize=(3,3))
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    
    ax.set_aspect(1)
    plotrange = 2
    ax.set_xlim(-plotrange-0.2, plotrange+0.2)
    ax.set_ylim(-plotrange-0.2, plotrange+0.2)
    ax.tick_params(labelleft=False, labelbottom=False, labelsize=12)
    ax.set_xticks(np.arange(-plotrange, plotrange+1, dtype=int))
    ax.set_yticks(np.arange(-plotrange, plotrange+1, dtype=int))

    points = []
    n = 4
    for i,j in product(np.arange(-n, n+1, dtype=int), repeat=2):
        points.append(i*basis[0] + j*basis[1])
    points = np.asarray(points)
    print(points.shape)
    ax.scatter(points[:,0], points[:,1], color='black', s=15)

    arrow_kw = {'head_width': 0.15, 'head_length': 0.2, 'width': 0.03, 'length_includes_head': True}
    b1 = FancyArrow(0, 0, *basis[0], **arrow_kw, color='red', zorder=3)
    b2 = FancyArrow(0, 0, *basis[1], **arrow_kw, color='red', zorder=3)
    ax.add_artist(b1)
    ax.add_artist(b2)

    fig.tight_layout()
    if showfig:
        plt.show()
    return fig

if __name__ == '__main__':
    basis = {
        "square": np.array([
            [1,0], [0,1]
        ]),
        "hex": np.array([
            [1,0], [-1/2, sqrt(3)/2]
        ]),
        "oblique": np.array([
            [1,0], [9/41, 40/41]
        ]),
        "rectangular": np.array([
            [1.0,0], [0,0.7]
        ]),
        "rhombic": np.array([
            [0.7, 0.6], [0.7, -0.6]
        ])
    }
    for key in basis:
        fig = draw_lattice(basis[key], False)
        fig.savefig('{}.svg'.format(key))
    