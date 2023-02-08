import argparse as ap
import pandas as pd
import json

def getScore(in_file, out_file):
    jobs = list(pd.read_csv(in_file).sort_values(by='submission_time').iterrows())
    jobs_json = []
    for index_current, current_job in jobs:
        print(index_current)
        if current_job['success'] == 0:
            continue
        makespan = 0
        slowdown = 0
        starting_time = current_job['starting_time']
        # slowdown = (running_time + waiting_time) / running_time

        multi_allocated_resources = current_job['allocated_resources'].split() # 0-15 16-17 => [0-15, 16-17]
        for x in multi_allocated_resources:
            allocated_resources = x.split('-')
            try:
                makespan = 1 + int(allocated_resources[1]) - int(allocated_resources[0])
            except IndexError:
                makespan = int(allocated_resources[0]) + 1 if int(allocated_resources[0]) != 0 else 1
        slowdown = (current_job['execution_time'] + current_job['waiting_time'] ) / current_job['execution_time']
        
        jobs_json.append({'Job_id' : current_job['job_id'], 'makespan' : makespan, 'slowdown' : slowdown, 'starting_time' : starting_time})

    with open(out_file, 'w') as out:
        json.dump(jobs_json, out, indent=4)



if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file_name', help='Name of the file to get the scores')
    parse.add_argument('out_file_name', help='Name of the file to save the scores')
    arg = parse.parse_args()

getScore(in_file=arg.in_file_name, out_file=arg.out_file_name)