import random
from scipy.stats import norm
import plotly.figure_factory as ff
from plotly import io


DIV_ID = 'guess-me'


def distribution_plot(data):
    fig = ff.create_distplot([data], ['A Mysterious Distribution'], show_hist=False)
    return io.to_html(fig, include_plotlyjs=False, div_id=DIV_ID, full_html=False)


def normal(n):
    x = norm.rvs(size=n, loc=random.randint(-10, 10), scale=1)
    return distribution_plot(x)


    


