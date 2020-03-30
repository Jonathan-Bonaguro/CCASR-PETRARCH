# setup environment

import pandas as pd
import numpy as np
import random

# input path to file, file_name, and decision to randomize rows

path = input("Path to Directory with File: ")
filename = input("Filename (.csv): ")
decision = input("Do you want to randomize this file? [Y/N]: ")

# read in data

df = pd.read_csv(str(path) + '/' + str(filename))

# function to randomize rows and print as "df_random.csv" in same directory

def randomize_file():
    np.random.seed(846258)
    df['rand'] = np.random.random(size=(len(df)))

    df_rand = df.sort_values(['rand']).reset_index(drop = True)

    df_rand.drop(['rand'], axis = 1)

    header = ['id', 'num_tokens', 'date', 'sent_num', 'random', 'id', 'doc_len', 'content']

    df_rand.to_csv(str(path) + '/' + filename[:-4] + '_random.csv', index=False, columns = header)

    print("File written as" + str(path) + '/' + filename[:-4]+'_random.csv')

# if they say they don't want to randomize the rows (idk why they ran this file...), exit

if str(decision) == "Y":
    randomize_file()
else:
    print("Okay. Goodbye.")