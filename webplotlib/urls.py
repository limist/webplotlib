from django.conf.urls.defaults import *


urlpatterns = patterns(
    'webplotlib.views',
    url(r'^ts_plot/foo.png$', 'show_ts_plot_png'),
    url(r'^bar_plot/bar.png$', 'show_bar_plot_png'),
    )
