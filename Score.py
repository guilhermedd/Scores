import argparse as ap
import pandas as pd
import json

def getScore(in_file, out_file):
    jobs = pd.read_csv(in_file)
    jobs.sort_values(by='submission_time')
    jobs_json = []
    queijo = list(jobs.iterrows())
    for index_current, current_job in queijo:
        print(index_current)
        if current_job['success'] == 0:
            continue
        makespan_func = 0
        makespan_reward = 0
        slowdown_func = 0
        slowdown_reward = 0
        starting_time = current_job['starting_time']
        for index_line, job in queijo[:index_current]:
            if job['success'] == 0:
                continue

            if job['submission_time'] <= current_job['submission_time'] and job['submission_time'] is not None:
                makespan_func += job['finish_time'] - job['submission_time']
                slowdown_func += (job['execution_time'] + job['waiting_time'] ) / job['execution_time']
            # slowdown = (running_time + waiting_time) / running_time

        multi_allocated_resources = current_job['allocated_resources'].split() # 0-15 16-17 => [0-15, 16-17]
        for x in multi_allocated_resources:
            allocated_resources = x.split('-')
            try:
                makespan_reward = int(allocated_resources[1]) - int(allocated_resources[0])
            except IndexError:
                makespan_reward = int(allocated_resources[0])
        slowdown_reward = (current_job['execution_time'] + current_job['waiting_time'] ) / current_job['execution_time']
        
        jobs_json.append({'Job_id' : current_job['job_id'], 'makespan_function' : makespan_func, 'makespan_reward' : makespan_reward, 'slowdown_function' : slowdown_func, 'slowdown_reward' : slowdown_reward, 'starting_time' : starting_time})

    with open(out_file, 'w') as out:
        json.dump(jobs_json, out, indent=4)



if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file_name', help='Name of the file to get the scores')
    parse.add_argument('out_file_name', help='Name of the file to save the scores')
    arg = parse.parse_args()

getScore(in_file=arg.in_file_name, out_file=arg.out_file_name)