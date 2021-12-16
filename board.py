from position import Position

class Board:

    def __init__(self, size):
        self.size = size

    def is_outside_board(self, pos, direction):
        """
        Validate whether the new position of the object is inside the board
        """
        pos = self.get_new_position(pos, direction)
        valid_values = range(0, self.size)

        if pos.x not in valid_values or pos.y not in valid_values:
            return True
        return False

    def get_new_position(self, current_pos, direction):
        """
        Return new position of the object in provided direction
        """
        x, y = current_pos.x, current_pos.y

        if direction == 'N':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        elif direction == 'S':
            y += 1

        return Position(x, y)
