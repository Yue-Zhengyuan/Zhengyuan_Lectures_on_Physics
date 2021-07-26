import numpy as np
import os
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

plt.style.use('default')
# plt.style.use('dark_background')
dir_path = os.path.dirname(os.path.realpath(__file__))
solution = False

fig, ax = plt.subplots(figsize=(3,3))
# set axis limit
ax.set_ylim(-0.5, 6)
ax.set_xlim(-0.5, 6)
# style for text
text_kw = dict(fontsize=14, transform=ax.transAxes)

# Make parallelogram
ori = np.zeros((2,))
a = np.array([3,1])
b = np.array([2,4])
verts = [ori, a, a+b, b]
poly = patches.Polygon(verts, edgecolor='black', fill=False, linewidth=1.5)
ax.add_patch(poly)

# draw auxilliary lines
if solution:
    ## cut-and-paste triangles
    q = np.array([a[0] - a[1]*b[0]/b[1], 0])
    tri1 = patches.Polygon([ori, q, a], facecolor='lightblue', edgecolor=None)
    ax.add_patch(tri1)
    tri2 = patches.Polygon([b, b+q, a+b], facecolor='lightblue', edgecolor=None)
    ax.add_patch(tri2)

    ## auxilliary lines
    line_kw = dict(linewidth=1., linestyle='--', color='black')
    line1 = lines.Line2D([q[0],a[0]], [q[1],a[1]], **line_kw)
    line2 = lines.Line2D([b[0],b[0] + q[0]], [b[1],b[1] + q[1]], **line_kw)
    ax.add_artist(line1)
    ax.add_artist(line2)

    ## related labels
    ax.text(0.8, 0.65, 'P', **text_kw)
    ax.text(0.45, 0.005, 'Q', **text_kw)

# the basis vectors a and b
arrow_kw = {'color': 'red', 'head_width': 0.2, 'head_length': 0.3, 'width': 0.05, 'length_includes_head': True}
arrow_a = patches.FancyArrow(*ori, *a, **arrow_kw)
arrow_b = patches.FancyArrow(*ori, *b, **arrow_kw)
ax.add_patch(arrow_a)
ax.add_patch(arrow_b)
text_kw2 = dict(color='red')
ax.text(0.3, 0.2, r'$\mathbf{a}$', **text_kw, **text_kw2)
ax.text(0.15, 0.35, r'$\mathbf{b}$', **text_kw, **text_kw2)

# add axis label
ax.text(0.9, 0.1, '$x$', **text_kw)
ax.text(0.1, 0.9, '$y$', **text_kw)
# add important points
ax.text(0.01, 0.005, 'O', **text_kw)
ax.text(0.01, 0.1, 'A', **text_kw)
ax.text(0.55, 0.15, 'B', **text_kw)
ax.text(0.85, 0.85, 'C', **text_kw)
ax.text(0.35, 0.72, 'D', **text_kw)

# set axes width
for key in ax.spines:
    ax.spines[key].set_linewidth(1)
# remove unnecessary axes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# set axes to go across the origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
# remove ticks
ax.set_xticks([])
ax.set_yticks([])

plt.show()
if solution:
    fig.savefig(dir_path + '/2d_det-solution.svg')
else:
    fig.savefig(dir_path + '/2d_det.svg')