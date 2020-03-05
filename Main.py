from Environment import Environment
from Agent import Agent

if __name__ == '__main__':
    file = open('input/seed')
    file_lines = [line for line in file.readlines() if line.strip()]
    file.close()
    agents = None

    # Check that file is not empty
    if file_lines:
        agents = []
        for i in range (0, len(file_lines)):
            line = file_lines[i]
            line = line.replace('\n', '')
            agent_values = line.split('[')
            opinion_rating = agent_values[0]
            friendship_values_strings = str(agent_values[1])[:-1].split(',')
            agents.append(Agent(i, opinion_rating, friendship_values_strings))

    print('Beginning simulation')
    if agents is not None:
        environment = Environment(agents=agents)
    else:
        environment = Environment(10)
    environment.run()
