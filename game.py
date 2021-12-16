from knight import Knight
from board import Board
from item import Item
from io_formatter import IOFormatter

class Game:
    surprise_attack_score = 0.5

    def __init__(self):
        """
        Setup the game board, knights & items and their attributes.
        """
        self.board = Board(8)

        self.R = Knight('red', 0, 0)
        self.Y = Knight('yellow', 0, 7)
        self.B = Knight('blue', 7, 0)
        self.G = Knight('green', 7, 7)

        self.A = Item('axe', 2, 0, 2, 2)
        self.D = Item('dagger', 1, 0, 5, 2)
        self.M = Item('magic_staff', 1, 1, 2, 5)
        self.H = Item('helmet', 0, 1, 5, 5)

    def execute_moves(self):
        """
        Read the moves from the file & execute them in sequence
        """
        moves = IOFormatter.read_file('moves.txt')
        for move in moves:
            self.execute_move(move[0], move[1])

    def execute_move(self, knight_str, direction):
        """
        This functions moves the knight in the provided direction.
        If the new direction is invalid, set the knight status to drowned.
        If any other knight is occupying new position, execute battle and set knight status.
        If any item is present, knight is equipped with that item.
        """
        knight = getattr(self, knight_str)

        if not knight.is_alive():
            return

        is_drowned = self.board.is_outside_board(knight.pos, direction)
        if is_drowned:
            knight.set_drowned()
            return

        new_pos = self.board.get_new_position(knight.pos, direction)

        item_present = self.is_any_item_present(new_pos)
        if item_present and not knight.item:
            knight.item = item_present
            item_present.is_equipped = True

        other_knight = self.is_any_knight_present(new_pos)
        if other_knight and other_knight.is_alive():
            is_alive = self.survive_battle(knight, other_knight)
            if not is_alive:
                return

        knight.pos = new_pos
        if knight.item:
            knight.item.pos = new_pos

    def is_any_knight_present(self, pos):
        """
        Check if any other knight is present on the position on which knight is moving
        """
        if self.R.pos == pos:
            return self.R
        elif self.G.pos == pos:
            return self.G
        elif self.B.pos == pos:
            return self.B
        elif self.Y.pos == pos:
            return self.Y
        else:
            return None

    def survive_battle(self, attacking_knight, defending_knight):
        """
        Execute the battle between two knights & update the status of drowning knight
        Returns True of the attacking knight survives the battle; false otherwise
        """
        attack_score = attacking_knight.get_total_attack_score()
        defend_score = defending_knight.get_total_defense_score()
        if attack_score + self.surprise_attack_score > defend_score:
            defending_knight.set_dead()
            return True
        else:
            attacking_knight.set_dead()
            return False

    def is_any_item_present(self, pos):
        """
        Check if any item is present on the position on which knight is moving.
        if any item is present, it returns them in following order (A, M, D, H).
        """
        if self.A.pos == pos:
            return self.A
        elif self.M.pos == pos:
            return self.M
        elif self.D.pos == pos:
            return self.D
        elif self.H.pos == pos:
            return self.H
        else:
            return None

    def output_json(self):
        """
        Read the moves from the file & execute them in sequence
        """
        data = IOFormatter.format_output([self.R, self.B, self.G, self.Y], [self.M, self.H, self.D, self.A])
        IOFormatter.write_to_file(data, 'final_state.json')
