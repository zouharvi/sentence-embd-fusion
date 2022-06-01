import matplotlib.style
import matplotlib as mpl
from cycler import cycler

FONT_MONOSPACE = {'fontname':'monospace'}
MARKERS = "o^s*DP1"
COLORS = [
    "cornflowerblue",
    "salmon",
    "seagreen",
    "orange",
    "dimgray",
    "violet",
    "darkseagreen",
]

# mpl.rcParams['axes.prop_cycle'] = cycler(color=list('bgrcmyk'))
mpl.rcParams['axes.prop_cycle'] = cycler(color=COLORS)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 7
# mpl.style.use('classic')
