import os
import pandas
from MoveDex.code import move

# Define root path as a variable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define dataset path in reference to the root path
DATASET_PATH = os.path.join(ROOT_DIR, '..\\assets\\move_dataset.csv')

# Read in dataset
move_df = pandas.read_csv(DATASET_PATH, index_col='#')
# move_data_frame_move = pandas.read_csv(DATASET_PATH, index_col='Name')

# print(move_data_frame_num.iloc[0])
# print(move_data_frame_move.loc['Pound'])
# print(move_df.iloc[0][6])

# name = move_df.iloc[0][0]
# move_type = move_df.iloc[0][1]
# category = move_df.iloc[0][2]
# pp = move_df.iloc[0][3]
# power = move_df.iloc[0][4]
# accuracy = move_df.iloc[0][5]
# gen = move_df.iloc[0][6]

# move_test = move.Move(1, name, move_type, category, pp, power, accuracy, gen)
# print(move_test)
# print(move_test.name)

move_list = []
for i in range(0, 850):
    move_generic = move.Move(i+1, move_df.iloc[i][0], move_df.iloc[i][1], move_df.iloc[i][2], move_df.iloc[i][3], move_df.iloc[i][4], move_df.iloc[i][5], move_df.iloc[i][6])
    move_list.append(move_generic)

thing = move_list[0]
print(thing)
print(move_list[849])
