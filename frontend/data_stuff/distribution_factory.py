import random
from scipy.stats import norm
import plotly.figure_factory as ff


def normal(n):
    x = norm.rvs(size=n, loc=random.randint(-10, 10), scale=1)
    return ff.create_distplot(x, show_hist=False)


    


