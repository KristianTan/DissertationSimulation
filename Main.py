from Environment import Environment
import pandas as pd
import glob

if __name__ == '__main__':
    # filenames = glob.glob('input/seed')
    # df_list = [pd.read_csv(file) for file in filenames]
    file = open('input/seed')
    file_lines = [line for line in file.readlines() if line.strip()]
    file.close()

    # Check that file is not empty
    if file_lines:
        initial_size = int(file_lines[0].replace('\n', ''))
        del file_lines[0]
        for line in file_lines:
            s = line.split('[')
            opinion = s[0]
            friendship_values_strings = str(s[1])[0:-1].split(',')
            friendship_values = list(map(float, friendship_values_strings))

    print('Beginning simulation')
    environment = Environment(10)
    environment.run()
