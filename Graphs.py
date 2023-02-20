import matplotlib.pyplot as plt
import json
import os
from os import path
import sys

def generate_graphs(in_file):
    tuple_revenue               = []
    tuple_slowdown              = []
    path_scheduler = 'Graphs/'

    for file in in_file:
        y_axis                  = []
        x_axis                  = []
        name = file.split('/')[len(file.split('/')) - 1].replace(".json", "") # name.txt => name
        print('Processing "{}"...'.format(name))
        try:
            with open (file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print('File "{}" not found'.format(file))
        i = 0 
        for d in data:
            x_axis.append(i)
            y_axis.append(d['revenue'])
            i+=1
        tuple_revenue.append((name, x_axis, y_axis))        
        print('Revenue done...')

        y_axis = []
        x_axis = []
        data.sort(key=lambda k : k['slowdown'])
        i = 0
        for d in data:
            x_axis.append(float(d['slowdown']))
            y_axis.append(float(i / len(data)))
            i+=1
        tuple_slowdown.append((name, x_axis, y_axis)) 
        print('Slowdown done...')

    #revenue
    plt.ylabel("Revenue") 
    for t in tuple_revenue:
        plt.plot(t[1], t[2], label=t[0])
    name = path_scheduler + 'revenue.png'
    plt.xlabel("Time (seconds)")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()

    plt.ylabel("CDF") 
    for t in tuple_slowdown:
        plt.plot(t[1], t[2], label=t[0])
    name = path_scheduler + 'slowdown.png'
    plt.xlabel("Slowdown")
    plt.legend(loc='best')
    plt.savefig(name) 
    plt.clf()


if __name__ == '__main__':
    generate_graphs(sys.argv[1:])
