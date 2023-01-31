import numpy as np
import matplotlib.pyplot as plt
import argparse as ap
import json
import os
from os import path

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def generate_graphs(in_file):
    tuple_mkspan_func           = []
    tuple_mkspan_reward         = []
    tuple_slowdown_func         = []
    tuple_slowdown_reward       = []

    for file in in_file:
        y_axis_CDF                  = []
        x_axis_makespan_function    = []
        x_axis_makespan_reward      = []
        x_axis_slowdown_function    = []
        x_axis_slowdown_reward      = []
        name = file.split('/')[len(file.split('/')) - 2] # name.txt => name
        with open (file, 'r') as f:
            data = json.load(f)

        data.sort(key=lambda k : k['starting_time'])
        for d in data:
            y_axis_CDF.append(data.index(d) / len(data))
            x_axis_makespan_function.append(d['makespan_function'])
            x_axis_makespan_reward.append(d['makespan_reward'])
            x_axis_slowdown_function.append(d['slowdown_function'])
            x_axis_slowdown_reward.append(d['slowdown_reward'])
        
        tuple_mkspan_func.append((x_axis_makespan_function, name))
        tuple_mkspan_reward.append((x_axis_makespan_reward, name))
        tuple_slowdown_func.append((x_axis_slowdown_function, name))
        tuple_slowdown_reward.append((x_axis_slowdown_reward, name))
        
    # #CDF
    path_scheduler = 'Graphs/'
    if not path.exists(path_scheduler):
        try:
            os.mkdir(path_scheduler)
        except OSError as error:
            print(error)
    

    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_mkspan_func:
        t[0].sort()
        plt.plot(t[0], y_axis_CDF, label=t[1])
    name = path_scheduler + '_makespan_function.png'
    plt.xlabel("Makespan Function")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_mkspan_reward:
        t[0].sort()
        plt.scatter(t[0], y_axis_CDF, label=t[1])
    name = path_scheduler + '_makespan_reward.png'
    plt.xlabel("Makespan Reward")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    # tuple_slowdown_func.sort()
    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_slowdown_func:
        t[0].sort()
        plt.plot(t[0], y_axis_CDF, label=t[1])
    name = path_scheduler + '_slowdown_function.png'
    plt.xlabel("Slowdown Function")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    # tuple_slowdown_reward.sort()
    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_slowdown_reward:
        t[0].sort()
        plt.plot(t[0], y_axis_CDF, label=t[1])
    name = path_scheduler + '_slowdown_reward.png'
    plt.xlabel("Slowdown Reward")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()


if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('-f','--files_list', action='append', help='In FIles (json)', required=True)
    arg = parse.parse_args()

generate_graphs(arg.files_list)
