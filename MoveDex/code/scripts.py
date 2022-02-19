import move
import os
import pandas

# Define root path as a variable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define dataset path in reference to the root path
DATASET_PATH = os.path.join(ROOT_DIR, '..\\assets\\move_dataset.csv')

# Read in dataset
move_data_frame = pandas.read_csv(DATASET_PATH)

