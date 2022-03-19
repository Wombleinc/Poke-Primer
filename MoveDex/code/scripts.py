import os
import pandas
from MoveDex.code import move

# Define root path as a variable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define dataset path in reference to the root path
DATASET_PATH = os.path.join(ROOT_DIR, '..\\assets\\move_dataset.csv')

# Read in dataset
move_df = pandas.read_csv(DATASET_PATH, index_col='#')

move_list = []
for i in range(0, 850):
    move_generic = move.Move(i+1, move_df.iloc[i][0], move_df.iloc[i][1], move_df.iloc[i][2], move_df.iloc[i][3], move_df.iloc[i][4], move_df.iloc[i][5], move_df.iloc[i][6])
    move_list.append(move_generic)
