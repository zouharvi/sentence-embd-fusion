import matplotlib.style
import matplotlib as mpl
from cycler import cycler

# mpl.rcParams['axes.prop_cycle'] = cycler(color=list('bgrcmyk'))
mpl.rcParams['axes.prop_cycle'] = cycler(color=[
    "cornflowerblue",
    "salmon",
    "seagreen",
    "orange",
    "dimgray",
    "violet",
    "darkseagreen",
])
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 7

# mpl.style.use('classic')
