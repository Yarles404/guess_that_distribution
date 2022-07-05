from flask import Blueprint, render_template
import random
from data_stuff.distribution_factory import normal


play = Blueprint('play', __name__)


DISTRIBUTIONS = [
    normal
]

def get_random_distribution():
    return DISTRIBUTIONS[random.randint(0, len(DISTRIBUTIONS) - 1)]


@play.route('/play', methods=['GET'])
def question():
    distribution = get_random_distribution()
    return render_template('play.html', distribution=distribution)