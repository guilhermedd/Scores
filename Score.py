import argparse as ap
import pandas as pd
import json

def getScore(in_file, out_file):
    jobs = list(pd.read_csv(in_file).sort_values(by='submission_time').iterrows())
    jobs_json = []
    for index_current, current_job in jobs:
        if current_job['success'] == 0:
            continue
        revenue = 0
        slowdown = 0
        starting_time = current_job['starting_time']
        multi_allocated_resources = current_job['allocated_resources'].split() # 0-15 16-17 => [0-15, 16-17]
        for x in multi_allocated_resources:
            allocated_resources = x.split('-')
            try:
                revenue += 1 + int(allocated_resources[1]) - int(allocated_resources[0])
            except IndexError:
                revenue += int(allocated_resources[0]) + 1 if int(allocated_resources[0]) != 0 else 1
            slowdown = max(current_job['turnaround_time'] / max(current_job['execution_time'], 10), 1)
            if slowdown > 1000.0:
                print(current_job)

        jobs_json.append({'Job_id' : current_job['job_id'], 'revenue' : revenue, 'slowdown' : slowdown, 'starting_time' : starting_time})

    with open(out_file, 'w') as out:
        json.dump(jobs_json, out, indent=4)



if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file_name', help='Name of the file to get the scores')
    parse.add_argument('out_file_name', help='Name of the file to save the scores')
    arg = parse.parse_args()

getScore(in_file=arg.in_file_name, out_file=arg.out_file_name)
