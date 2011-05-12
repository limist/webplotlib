# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect

from webplotlib.chart_templates import create_chart_as_png_str


def index(request):
    return HttpResponseRedirect('/admin/')


def show_ts_plot_png(request):
    fake_data_dct = {
        'data': [[1, 2, 1, 2, 3, 1, 4, 2, 2.5, 1.3]]}
    img_str = create_chart_as_png_str('timeseries', fake_data_dct, {}, '')
    # From here the Django-specific part follows; not much to it:
    response = HttpResponse(img_str, mimetype='image/png')
    # Development note: the function create_timeseries_png_str uses a
    # StringIO approach, which is better than some examples (on the
    # web) using print_png(response) tried first (below) which causes
    # timeout error messages on the server-side.
    #
    # figure.print_png(response)
    return response
