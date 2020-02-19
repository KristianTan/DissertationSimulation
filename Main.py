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
        agents = []
        for line in file_lines:
            line = line.replace('\n', '')
            agent_values = line.split('[')
            opinion = agent_values[0]
            friendship_values_strings = str(agent_values[1])[:-1].split(',')
            friendship_values = list(map(float, friendship_values_strings))
            # TODO: Be able to pass initial values to Agent constructor. Be able to handle instance where some friendship values are not passed.  i.e. initsl pop = 10 but only passed 5 friendship values
            # Pass list of values or agents to Environment constructor.  Probably Agents?
            # TODO: Be able to pass list of initialised agents to Environment constructor.  Be able to handle missing friendship values and not enough agents in list

    print('Beginning simulation')
    environment = Environment(10)
    environment.run()
