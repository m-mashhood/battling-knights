import json

class IOFormatter:

    @staticmethod
    def read_file(filename):
        """
        Read the file and returns the list of move
        """
        with open(filename) as f:
            moves = f.read().splitlines()

        moves = moves[1:-1]
        moves  = [m.split(':') for m in moves]
        return moves

    @staticmethod
    def format_output(knights, items):
        """
        Convert the knights & item data into proper format
        """
        data = {}
        for knight in knights:
            knight_pos = [knight.pos.y, knight.pos.x] if knight.pos else None
            knight_data = [knight_pos, knight.status]

            if knight.item:
                knight_data.extend([
                    knight.item.name,
                    knight.get_total_attack_score(),
                    knight.get_total_defense_score(),
                ])
            else:
                knight_data.extend([None, knight.base_attack, knight.base_defense])

            data[knight.name] = knight_data

        for item in items:
            item_pos = [item.pos.y, item.pos.x] if item.pos else None
            data[item.name] = [item_pos, item.is_equipped]

        return data

    @staticmethod
    def write_to_file(data, filename):
        """
        Write the data provided to the file
        """
        with open(filename, 'w') as f:
            json.dump(data, f)

