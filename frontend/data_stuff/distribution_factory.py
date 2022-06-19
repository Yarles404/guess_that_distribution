import random
from scipy.stats import norm
import plotly.figure_factory as ff
from plotly import io


def normal(n):
    x = norm.rvs(size=n, loc=random.randint(-10, 10), scale=1)
    fig = ff.create_distplot([x], show_hist=False)
    return io.to_html(fig, include_plotlyjs=False)


    


