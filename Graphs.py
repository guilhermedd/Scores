import matplotlib.pyplot as plt
import argparse as ap
import json
import os
from os import path

def generate_graphs(in_file):
    tuple_makespan              = []
    tuple_slowdown              = []
    path_scheduler = 'Graphs/'

    for file in in_file:
        y_axis                  = []
        x_axis                  = []
        name = file.split('/')[len(file.split('/')) - 2] # name.txt => name

        try:
            with open (file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print('File "{}" not found'.format(file))
        
        for d in data:
            y_axis.append(data.index(d))
            x_axis.append(d['makespan'])
        
        plt.ylabel("Cumulative Distribution Function") 
            # t[0].sort()
        plt.scatter(x_axis, y_axis)
        name = path_scheduler + '_makespan_no_sort.png'
        plt.xlabel("Makespan Function")
        plt.legend(loc='best')
        plt.savefig(name) 
        plt.clf()

        for d in data:
            y_axis.append(data.index(d))
            x_axis.append(d['slowdown'])
        
        plt.ylabel("Cumulative Distribution Function") 
            # t[0].sort()
        plt.scatter(x_axis, y_axis)
        name = path_scheduler + '_slowdown_no_sort.png'
        plt.xlabel("Slowdown Function")
        plt.legend(loc='best')
        plt.savefig(name) 
        plt.clf()

        data.sort(key=lambda k : k['makespan'])
        for d in data:
            y_axis.append(data.index(d) / len(data))
            x_axis.append(d['makespan'])
        tuple_makespan.append((x_axis, name, y_axis))

        y_axis = []
        x_axis = []
        data.sort(key=lambda k : k['slowdown'])
        for d in data:
            x_axis.append(d['slowdown'])
            y_axis.append(data.index(d) / len(data))
        tuple_slowdown.append((x_axis, name,y_axis)) 
        
    #CDF
    if not path.exists(path_scheduler):
        try:
            os.mkdir(path_scheduler)
        except OSError as error:
            print(error)

    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_makespan:
        # t[0].sort()
        plt.plot(t[0], t[2], label=t[1])
    name = path_scheduler + '_makespan.png'
    plt.xlabel("Makespan")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    # tuple_slowdown.sort()
    plt.ylabel("Cumulative Distribution Function") 
    for t in tuple_slowdown:
        # t[0].sort()
        plt.plot(t[0], t[2], label=t[1])
    name = path_scheduler + '_slowdown.png'
    plt.xlabel("Slowdown")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()


if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('-f','--files_list', action='append', help='In FIles (json)', required=True)
    arg = parse.parse_args()

generate_graphs(arg.files_list)
