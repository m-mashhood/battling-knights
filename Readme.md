# Battling Knights

The code has few base classes as following:

The `Position` class to store the position of Knights and Item on the Board.

The `Knight` class will hold properties such as name, pos (Position), item, status [Dead, Live, Drowned], base attack, & base defence.

The `Item` class will hold properties such as name, attack & base score, pos (Position) & is_equipped (True if the item is equipped by any Knight; false otherwise).

The `Board` class holds only size as property.

The `Game` class which uses all other classes & execute the game.


# Usage

To run the app:

    python main.py

To run the test:

    python test.py

Moves will be read in from `moves.txt`. The final state of knights & item will be written to `final_state.json`.
