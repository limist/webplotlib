# -*- coding: utf-8 -*-

import itertools
from StringIO import StringIO

import matplotlib  # Must be prior to pyplot import.
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


# See http://matplotlib.sourceforge.net/users/customizing.html
font_params = {
    'sans-serif': [
        'Helvetica Neue', 'Arial', 'Liberation Sans',
        'FreeSans', 'sans-serif'],
    'size': 13.0,
    }
matplotlib.rc('font', **font_params)


# Automatic cycling of colors and linestyles is useful when plotting
# multiple data/lines - itertools usage from Ryan May's Nov.8 2010
# Matplot-lib-users list message:
colors_default = itertools.cycle([
    '#7C8BD9',  # Light blue
    '#DE2D26',  # Medium red
    '#2CA25F',  # Medium green
    ])
linestyles_default = itertools.cycle([
    '-',   # solid
    '--',  # dashed
    '-.',  # dash-dot
    ':'])  # dotted


def create_timeseries_figure(ts_data_dct, labels_dct, template,
                             show_title=False, set_y_origin_zero=True):
    """
    For a given sequence or dictionary of timeseries data, creates and
    returns a Matplotlib Figure(Canvas) instance/visualization.  That
    Figure can then be written to different formats, e.g. PNG or PDF.
    """
    # This function's organizing princple is to first express the
    # figure's content/data, then handle its presentation/styling.
    #
    # CONTENT of figure:
    assert isinstance(ts_data_dct, dict), \
           "Unknown type for ts_data_dct: %s" % ts_data_dct
    tseries_data = ts_data_dct['data']
    assert all([len(this_ts) > 0 for this_ts in tseries_data])
    tseries_names = ts_data_dct.get('names')
    if 'colors' in ts_data_dct:
        colors = itertools.cycle(ts_data_dct['colors'])
    else:
        colors = colors_default
    if 'linestyles' in ts_data_dct:
        linestyles = itertools.cycle(ts_data_dct['linestyles'])
    else:
        linestyles = linestyles_default
    # With data unpacked, start building matplotlib Figure:
    the_figure = Figure()
    ax = the_figure.add_subplot(1, 1, 1)
    ts_lines = []
    for ts in tseries_data:
        this_ts_line, = ax.plot(
            ts,
            linestyle=linestyles.next(),
            color=colors.next(),
            linewidth=1)
        ts_lines.append(this_ts_line)
    # Set the legend:
    if tseries_names:
        ax.legend(
            ts_lines, tseries_names,
            'upper right', frameon=False)
    # The extents, title, and axis labels - set their text:
    #
    # if set_y_origin_zero:  # and min(ts_data) >= 0:
    #     y_bottom = 0
    # y_top = max(ts_data) + 10
    # ax.set_ylim(y_bottom, y_top)
    #
    # Set labels: title, x, y
    figure_title = None
    if 'title' in labels_dct and show_title:
        # Note - it's not clear how to later select the title Text
        # instance after its construction via suptitle below, so setup
        # the reference here and use it later:
        figure_title = the_figure.suptitle(labels_dct['title'])
    if 'x' in labels_dct:
        ax.set_xlabel(labels_dct['x'])
    else:
        ax.set_xlabel('Time')
    if 'y' in labels_dct:
        ax.set_ylabel(labels_dct['y'])
    else:
        ax.set_ylabel('Data')
    # PRESENTATION of figure:
    #
    # The template parameter should/will set the overall styling of
    # the chart, set below:
    bgcolor = '#FFFFFF'
    border_color = '#CCCCCC'
    axis_label_color = '#555555'
    axis_ticks_color = '#555555'
    # Change the overall background color, which is grey by default:
    the_figure.patch.set_color(bgcolor)
    # Changing the border of a matplotlib chart is clumsy, but here it
    # is per http://stackoverflow.com/q/1982770/294239
    for child in ax.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color(border_color)
    # Next, change the color of the title, and axis+tick labels:
    #
    # This does not work to select the figure title:
    # the_figure.gca().axes.title.set_color(axis_label_color)
    if figure_title:
        figure_title.set_color(axis_label_color)
    ax.xaxis.get_label().set_color(axis_label_color)
    for label in ax.xaxis.get_ticklabels():
        label.set_color(axis_ticks_color)
    ax.yaxis.get_label().set_color(axis_label_color)
    for label in ax.yaxis.get_ticklabels():
        label.set_color(axis_ticks_color)
    return FigureCanvas(the_figure)


def create_timeseries_png_str(data_dct, labels_dct=None, template=None):
    assert isinstance(data_dct, dict) and 'data' in data_dct
    assert len(data_dct['data'][0]) > 0
    if labels_dct:
        assert isinstance(labels_dct, dict) and 'title' in labels_dct
    # With arguments checked, create the matplotlib Figure instance:
    figure = create_timeseries_figure(data_dct, labels_dct, template)
    # From here on, PNG-specific code happens.
    #
    # Note: there's no need to specify resolution/DPI for web-usage,
    # what matters is the pixel count.  See
    # http://benthinkin.net/imagery/on-the-web-dpi-doesn-t-matter
    img_data_str = StringIO()
    figure.print_png(img_data_str)
    img_data_str.seek(0)  # After writing, rewind data for further use.
    return img_data_str.read()
