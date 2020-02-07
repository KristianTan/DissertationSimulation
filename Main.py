from Environment import Environment
import pandas as pd
import glob

if __name__ == '__main__':
    filenames = glob.glob('input/agent*.csv')
    df_list = [pd.read_csv(file) for file in filenames]

    print('Beginning simulation')
    environment = Environment(10)
    environment.run()
