# -*- coding: utf-8 -*-
#
desc = 'Dual axis plot'
phash = '41a3dc4b76a9ca35'


def plot():
    from matplotlib import pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax = fig.add_subplot(111)
    dat = np.linspace(0, 10, 20)
    ax.plot(dat, dat**2)
    ax2 = ax.twinx()
    ax2.plot(20*dat, 20*dat**2)

    return fig
