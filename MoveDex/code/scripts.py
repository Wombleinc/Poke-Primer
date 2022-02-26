import move
import os
import pandas

# Define root path as a variable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define dataset path in reference to the root path
DATASET_PATH = os.path.join(ROOT_DIR, '..\\assets\\move_dataset.csv')

# Read in dataset
move_data_frame_num = pandas.read_csv(DATASET_PATH, index_col='#')
move_data_frame_move = pandas.read_csv(DATASET_PATH, index_col='Name')

# brainstorming pseudocode for interaction script:

# while user in MoveDex:
# user_query = bla (input from kivy)
# if move_data_frame[user_query] exists:
# output(move_data_frame[user_query])

print(move_data_frame_num.iloc[0])
print(move_data_frame_move.loc['Pound'])
