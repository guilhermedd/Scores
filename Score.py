import argparse as ap
import pandas as pd
import json

def getScore(in_file, out_file):
    jobs = pd.read_csv(in_file)
    jobs_json = []
    for index_current, current_job in jobs.iterrows():
        if current_job['success'] == 0:
            continue
        makespan_func = 0
        makespan_reward = 0
        energy_consuption_func = 0
        energy_consuption_reward = 0
        energy_efficiency_func = 0
        energy_efficiency_reward = 0
        for index_line, job in jobs.iterrows():
            if job['success'] == 0:
                continue

            if job['submission_time'] >= current_job['submission_time']:
                makespan_func += job['finish_time'] - job['submission_time']

            if current_job['starting_time'] <= job['finish_time'] or current_job['finish_time'] >= job['starting_time']:
                makespan_reward += 0
        
        jobs_json.append({'Job_id' : current_job['job_id'], 'makespan_function' : makespan_func, 'makespan_reward' : makespan_reward, 'energy_consuption_function' : energy_consuption_func, 'energy_consuption_reward' : energy_consuption_reward, 'energy_efficiency_function' : energy_efficiency_func, 'energy_efficiency_reward': energy_efficiency_reward})

    with open(out_file, 'w') as out:
        json.dump(jobs_json, out, indent=4)


if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file_name', help='Name of the file to get the scores')
    parse.add_argument('out_file_name', help='Name of the file to save the scores')
    arg = parse.parse_args()

getScore(in_file=arg.in_file_name, out_file=arg.out_file_name)