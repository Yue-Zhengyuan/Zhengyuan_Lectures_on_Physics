"""
    Demostration of linear map
    =====================================
    Author: Yue Zhengyuan

    Drag the basis vectors to see how an arbitrary vector is transformed

    Adapted from the StackOverflow answer
    https://stackoverflow.com/a/63568715/10444934
"""

import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon, FancyArrow
# from matplotlib.widgets import Slider, Button, RadioButtons
# from matplotlib.widgets import TextBox

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

rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial"],
})

# initialize data
unit1, unit2 = np.array([1,0]), np.array([0,1])
init_e1, init_e2 = np.array([2,1]), np.array([-1,2])
init_vOld = np.array([3,4])

# the whole figure
fig = plt.figure(figsize=(10, 7))

# add axis 
# [left, bottom, width, height]
## for plotting to current figure
ax = plt.axes([0.05, 0.1, 0.6, 0.8])
## for showing info
ax2 = plt.axes([0.68, 0.4, 0.25, 0.5])
### turn off all axes in ax2
ax2.axis('off')

# parameters for text
text_kw = dict(fontsize=14)
text_kw2 = dict(fontsize=14)

ax.set_title('Linear Map Demostration', fontsize=16)
ax.set_xlim(-9, 9)
ax.set_ylim(-5, 13)
ax.set_aspect(1)
# axes go through origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
# turn off unnecessary axes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(left=False, bottom=False, labelsize=14)
# axis label
ax.text(8, 0.3, '$x$', **text_kw)
ax.text(0.3, 12, '$y$', **text_kw)
# set position of grid
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
# axis grid
ax.grid(True, which='major', linestyle='-', lw=1)
ax.grid(True, which='minor', linestyle=':', lw=0.5)

def vecNew(v, e1, e2):
    """Find strandard components of v after transformation"""
    return v[0]*e1 + v[1]*e2

def vecLabelXY(v, start=(0,0)):
    """Determine the position of the vector label"""
    raise NotImplementedError
    # midpoint = tuple((v[i] + start[i])/2 for i in range(2))
    # # direction orthogonal to v
    # coord = midpoint
    # return coord

arrow_kw = {'head_width': 0.2, 'head_length': 0.3, 'width': 0.03, 'length_includes_head': True}

# linear map
## components of basis vec after transform
e1New = FancyArrow(0, 0, *init_e1, **arrow_kw, color='red')
e1Label = ax.text(*(1.1*init_e1), '$e_1$', **text_kw, color='red')
e2New = FancyArrow(0, 0, *init_e2, **arrow_kw, color='blue')
e2Label = ax.text(*(1.1*init_e2), '$e_2$', **text_kw, color='blue')
## display standard components of e1, e2
transInfo = ax2.text(0, 0.9, 
    'Components of $e_1, e_2$ \nafter transformation:', 
    **text_kw2
)
e1NewInfo = ax2.text(0, 0.82, 
    '$e_1$: ({:.3f}, {:.3f})'.format(*init_e1), 
    **text_kw2, color='red'
)
e2NewInfo = ax2.text(0, 0.75, 
    '$e_2$: ({:.3f}, {:.3f})'.format(*init_e2), 
    **text_kw2, color='blue'
)

# arbitrary vector
## components of v before transform
vOld = FancyArrow(0, 0, *init_vOld, **arrow_kw, color='green', alpha=0.5)
vOldLabel = ax.text(*(1.1*init_vOld), '$v$', **text_kw, color='green')
## auxiliary parallelogram
vertsOld = [np.array([0,0]), init_vOld[0]*unit1,
        init_vOld, init_vOld[1]*unit2]
polygon_kw = dict(linestyle='--', linewidth=1, edgecolor='black', fill=False)
auxOld = Polygon(vertsOld, **polygon_kw, alpha=0.5)
ax.add_artist(auxOld)
## components of v after transform
init_vNew = vecNew(init_vOld, init_e1, init_e2)
vNew = FancyArrow(0, 0, *init_vNew, **arrow_kw, color='green')
vNewLabel = ax.text(*(1.02*init_vNew), r'$v^\prime$', **text_kw, color='green')
## auxiliary parallelogram
vertsNew = [np.array([0,0]), init_vOld[0]*init_e1,
        init_vNew, init_vOld[1]*init_e2]
polygon_kw = dict(linestyle='--', linewidth=1, edgecolor='black', fill=False)
auxNew = Polygon(vertsNew, **polygon_kw)
ax.add_artist(auxNew)
## display information
vInfo = ax2.text(0, 0.6, 
    'Components of $v$ \nalong old basis:',
    **text_kw2, color='green'
)
vOldInfo = ax2.text(0, 0.45, 
    'Before transformation: \n({:.3f}, {:.3f})'.format(*init_vOld), 
    **text_kw2, color='green', alpha=0.5
)
vNewInfo = ax2.text(0, 0.3, 
    'After transformation: \n({:.3f}, {:.3f})'.format(*init_vNew), 
    **text_kw2, color='green'
)

# draw vectors on the figure
ax.add_artist(e1New)
ax.add_artist(e2New)
ax.add_artist(vOld)
ax.add_artist(vNew)

# locator of vectors
## drag pt1, pt2 to change transformation (e1, e2)
pt1, = ax.plot(*init_e1, '+', color='red', ms=10, picker=20)
pt2, = ax.plot(*init_e2, '+', color='blue', ms=10, picker=20)
## drag ptv to change vOld
ptv, = ax.plot(*init_vOld, '+', color='green', ms=10, picker=20)

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

picked_artist = None

def on_pick(event):
    'called when an element is picked'
    global picked_artist
    if event.mouseevent.button == MouseButton.LEFT:
        picked_artist = event.artist

def on_button_release(event):
    'called when a mouse button is released'
    global picked_artist
    if event.button == MouseButton.LEFT:
        # clear picker_artist when release mouse button
        picked_artist = None

def on_motion_notify(event):
    'called when the mouse moves'
    global picked_artist
    global init_e1, init_e2, init_vOld
    global e1New, e2New, vOld, vNew
    global auxOld, auxNew
    global grid1, grid2
    if picked_artist is not None and event.inaxes is not None and event.button == MouseButton.LEFT:
        picked_artist.set_data([event.xdata], [event.ydata])
        if picked_artist == pt1 or picked_artist == pt2:
            if picked_artist == pt1:
                # redraw arrow e1
                init_e1 = np.array([event.xdata, event.ydata])
                e1New.remove()
                e1New = FancyArrow(0, 0, *init_e1, **arrow_kw, color='red')
                ax.add_artist(e1New)
                e1Label.set_position(1.1 * init_e1)
            elif picked_artist == pt2:
                # redraw arrow e2
                init_e2 = np.array([event.xdata, event.ydata])
                e2New.remove()
                e2New = FancyArrow(0, 0, *init_e2, **arrow_kw, color='blue')
                ax.add_artist(e2New)
                e2Label.set_position(1.1 * init_e2)
            # redraw gridlines
            for line1, line2 in zip(grid1, grid2):
                line1.remove()
                line2.remove()
            grid1.clear()
            grid2.clear()
            for n in range(-10,10):
                ## parallel to e1
                line1 = np.transpose(np.array([a * init_e1 + n * init_e2 for a in alpha]))
                ## parallel to e2
                line2 = np.transpose(np.array([a * init_e2 + n * init_e1 for a in alpha]))
                grid1.append(ax.plot(line1[0], line1[1], color=grid_color(n), zorder=0)[0])
                grid2.append(ax.plot(line2[0], line2[1], color=grid_color(n), zorder=0)[0])
        elif picked_artist == ptv:
            # redraw vOld
            init_vOld = np.array([event.xdata, event.ydata])
            vOld.remove()
            vOld = FancyArrow(0, 0, *init_vOld, **arrow_kw, color='green', alpha=0.5)
            ax.add_artist(vOld)
            vOldLabel.set_position(1.1 * init_vOld)
        # redraw vNew
        vNew.remove()
        init_vNew = vecNew(init_vOld, init_e1, init_e2)
        vNew = FancyArrow(0, 0, *init_vNew, **arrow_kw, color='green')
        ax.add_artist(vNew)
        vNewLabel.set_position(1.02 * init_vNew)
        # redraw parallelograms
        auxOld.remove()
        auxNew.remove()
        vertsOld = [np.array([0,0]), init_vOld[0]*unit1,
                    init_vOld, init_vOld[1]*unit2]
        vertsNew = [np.array([0,0]), init_vOld[0]*init_e1,
                    init_vNew, init_vOld[1]*init_e2]
        auxOld = Polygon(vertsOld, **polygon_kw, alpha=0.5)
        ax.add_artist(auxOld)
        auxNew = Polygon(vertsNew, **polygon_kw)
        ax.add_artist(auxNew)
        # update vector info
        e1NewInfo.set_text('$e_1$: ({:.3f}, {:.3f})'.format(*init_e1))
        e2NewInfo.set_text('$e_2$: ({:.3f}, {:.3f})'.format(*init_e2))
        vOldInfo.set_text('Before transformation: \n({:.3f}, {:.3f})'.format(*init_vOld))
        vNewInfo.set_text('After transformation: \n({:.3f}, {:.3f})'.format(*init_vNew))
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_release_event', on_button_release)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('motion_notify_event', on_motion_notify)

plt.show()
