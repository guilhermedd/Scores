import numpy as np
import matplotlib.pyplot as plt
import argparse as ap
import json
import os
from os import path

def generate_graphs(in_file):
    tuple_mkspan_func           = []
    tuple_mkspan_reward         = []
    tuple_slowdown_func         = []
    tuple_slowdown_reward       = []

    for file in in_file:
        y_axis                  = []
        x_axis                  = []
        name = file.split('/')[len(file.split('/')) - 2] # name.txt => name

        try:
            with open (file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print('File "{}" not found'.format(file))

        # data_by_starting_time = data.sort(key=lambda k : k['starting_time'])
        data.sort(key=lambda k : k['makespan_function'])
        for d in data:
            y_axis.append(data.index(d) / len(data))
            x_axis.append(d['makespan_function'])
        tuple_mkspan_func.append((x_axis, name, y_axis))

        y_axis = []
        x_axis = []
        data.sort(key=lambda k : k['makespan_reward'])
        for d in data:
            x_axis.append(d['makespan_reward'])
            y_axis.append(data.index(d) / len(data))
        tuple_mkspan_reward.append((x_axis, name, y_axis))

        y_axis = []
        x_axis = []
        data.sort(key=lambda k : k['slowdown_function'])
        for d in data:
            x_axis.append(d['slowdown_function'])
            y_axis.append(data.index(d) / len(data))
        tuple_slowdown_func.append((x_axis, name, y_axis))

        y_axis = []
        x_axis = []
        data.sort(key=lambda k : k['slowdown_reward'])
        for d in data:
            x_axis.append(d['slowdown_reward'])
            y_axis.append(data.index(d) / len(data))
        tuple_slowdown_reward.append((x_axis, name,y_axis))
        
        
    # #CDF
    path_scheduler = 'Graphs/'
    if not path.exists(path_scheduler):
        try:
            os.mkdir(path_scheduler)
        except OSError as error:
            print(error)

    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_mkspan_func:
        # t[0].sort()
        plt.plot(t[0], t[2], label=t[1])
    name = path_scheduler + '_makespan_function.png'
    plt.xlabel("Makespan Function")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_mkspan_reward:
        # t[0].sort()
        plt.scatter(t[0], t[2], label=t[1])
    name = path_scheduler + '_makespan_reward.png'
    plt.xlabel("Makespan Reward")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    # tuple_slowdown_func.sort()
    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_slowdown_func:
        # t[0].sort()
        plt.plot(t[0], t[2], label=t[1])
    name = path_scheduler + '_slowdown_function.png'
    plt.xlabel("Slowdown Function")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    # tuple_slowdown_reward.sort()
    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_slowdown_reward:
        # t[0].sort()
        plt.plot(t[0], t[2], label=t[1])
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
