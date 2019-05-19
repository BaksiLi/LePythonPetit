#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.offsetbox import AnchoredText


def archive_files() -> None:
    # get root dir info
    source = os.getcwd()
    files = os.listdir(source)

    # check destination dir
    destination = os.path.join(source, 'archive')
    os.makedirs(destination, exist_ok=True)  # if no dir then create

    # move files to destination dir
    for f in files:
        if f[:4] == 'plot' and f[-4:] == '.pdf':
            shutil.move(f, destination)


def plot_usage(data: pd.DataFrame) -> None:
    # create two subgraphs on a row
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2, sharex=True, figsize=(8, 5)
    )
    fig.suptitle('Activity log')

    # subgraph 1
    ax1.set_title('keystrokes')
    data.plot(y='keystrokes', use_index=True, legend=False, ax=ax1)
    ax1.plot([data['keystrokes'][:-1].mean()] * len(data),
             label='Mean',
             color='r',
             linestyle='--')

    # subgraph 2
    ax2.set_title('Mouse move distance (in m)')
    data.plot(y='mouse distance', use_index=True, legend=False, ax=ax2)
    ax2.plot([data['mouse distance'][:-1].mean()] * len(data),
             label='Mean',
             color='r',
             linestyle='--')

    # archive old plots
    archive_files()

    # plt.show()
    plt.savefig('plot_{}.pdf'.format(datetime.date.today()))


def plot_usage_two_scales(data: pd.DataFrame) -> None:
    # create two subgraphs on a row
    fig, ax1 = plt.subplots()
    plt.title('Activity log')
    plt.xlabel('Days')
    plt.legend()

    # subgraph 1
    colour = 'tab:blue'
    mean = data['keystrokes'][:-1].mean()
    plot1 = data.plot(
        y='keystrokes',
        color=colour,
        xticks=[i for i in range(0, len(data), 5)],
        use_index=True,
        ax=ax1,
        legend=False
    )
    ax1.plot([mean] * len(data),
             label='  Mean: {}'.format(int(mean)),
             color=colour,
             linestyle='--')
    ax1.set_ylabel('Number of Keystrokes')

    # subgraph 2
    ax2 = ax1.twinx()
    colour = 'tab:red'
    mean = data['trackpad distance'][:-1].mean()
    plot2 = data.plot(
        y='trackpad distance', color=colour, use_index=True, ax=ax2
    )
    ax2.plot([mean] * len(data),
             label='  Mean: {:.1f} $m$'.format(mean),
             color=colour,
             linestyle='--')
    ax2.set_ylabel('Trackpad Moving Distance (m)')

    # legends
    h1, l1 = plot1.get_legend_handles_labels()
    h2, l2 = plot2.get_legend_handles_labels()
    plt.legend(h1 + h2, l1 + l2, loc=1)

    # panel
    box = AnchoredText(
        'Total Keys/Dist: {} / {:.1f} $m$'.format(
            int(data['keystrokes'][:-1].sum()),
            data['trackpad distance'][:-1].sum()
        ),
        loc='lower left',
        bbox_to_anchor=(.1, .1),
        frameon=False
    )
    ax1.add_artist(box)
    # TODO: https://matplotlib.org/gallery/widgets/textbox.html#sphx-glr-gallery-widgets-textbox-py TEXTBOX??

    # archive old plots
    archive_files()

    fig.tight_layout()
    fig.subplots_adjust(top=0.9)
    # plt.show()
    plt.savefig('plot_{}.pdf'.format(datetime.date.today()))


if __name__ == '__main__':
    # read csv from OctoMouse with the last row dropped
    data = pd.read_csv('*.csv')[:-1]
    data['trackpad distance'] = (
        data['mouse distance'] + data['scroll distance']
    ) * 1000  # in metres

    # plot graph
    #plot_usage(data)
    plot_usage_two_scales(data)

