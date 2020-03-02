from Environment import Environment
from Agent import Agent
import pandas as pd
import glob

if __name__ == '__main__':
    # filenames = glob.glob('input/seed')
    # df_list = [pd.read_csv(file) for file in filenames]
    file = open('input/seed')
    file_lines = [line for line in file.readlines() if line.strip()]
    file.close()
    agents = None

    # Check that file is not empty
    if file_lines:
        # initial_size = int(file_lines[0].replace('\n', ''))
        # del file_lines[0]
        agents = []
        for i in range (0, len(file_lines)):
            line = file_lines[i]
            line = line.replace('\n', '')
            agent_values = line.split('[')
            opinion_rating = float(agent_values[0])
            friendship_values_strings = str(agent_values[1])[:-1].split(',')
            friendship_values = list(map(float, friendship_values_strings))
            agents.append(Agent(i, opinion_rating, friendship_values))

    print('Beginning simulation')
    if agents is not None:
        environment = Environment(10, agents)
    environment = Environment(10)
    environment.run()
