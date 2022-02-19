from move import Move
import scripts

test_move = Move()
Move.id, Move.name, Move.accuracy, Move.pp, Move.priority, Move.power = 1, "", 1, 1, 1, 1
print(test_move)

print(scripts.move_data_frame)
