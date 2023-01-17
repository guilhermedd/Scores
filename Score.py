import argparse as ap

def getScore(in_file, out_file):
    with open(in_file) as file:
        for current_line in file[1:]: # 1st line is a description of the log
            for line in file:
                if line[0] == current_line[0]:
                    break




if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file_name', help='Name of the file to get the scores')
    parse.add_argument('out_file_name', help='Name of the file to save the scores')
    arg = parse.parse_args()

getScore(in_file=arg.in_file_name, out_file=arg.out_file_name)