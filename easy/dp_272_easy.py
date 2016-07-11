"""
[2016-06-20] Challenge #272 [Easy] What's in the bag?
https://tinyurl.com/rDP-272-easy
"""
# Status: Done

import random


class Scrubble:
    """Class simulates a Scrubble tile bag.

    Attributes:
        tile_bag: contains all 23 letters of the English alphabet and
                  blank tile in tile_bag = [[tile, count, value] ...] format.
    """
    def __init__(self):
        # CHANGED from list of list to dictionary.
        self.tile_bag = {'_': [2, 0],
                         'A': [9, 1],
                         'B': [2, 3],
                         'C': [2, 3],
                         'D': [4, 2],
                         'E': [12, 1],
                         'F': [2, 4],
                         'G': [3, 2],
                         'H': [2, 4],
                         'I': [9, 1],
                         'J': [1, 8],
                         'K': [1, 5],
                         'L': [4, 1],
                         'M': [2, 3],
                         'N': [6, 1],
                         'O': [8, 1],
                         'P': [2, 3],
                         'Q': [1, 10],
                         'R': [6, 1],
                         'S': [4, 1],
                         'T': [6, 1],
                         'U': [4, 1],
                         'V': [2, 4],
                         'W': [2, 4],
                         'X': [1, 8],
                         'Y': [2, 4],
                         'Z': [1, 10]}
        # non-public attribute _tiles_string used to create
        # random sets of tiles
        self._tiles_string = ""
        for (tile, (count, _)) in self.tile_bag.items():
            self._tiles_string += "".join(tile * count)
        # non-public attribute _sorted_bag created in _sort_bag method
        self._sorted_bag = None

    def _take_one_tile(self, tile):
        """Remove one tile from tile_bag.

        Decreases tile_count by one. Removes tile from _tiles_string.
        Prints error message if no requested tiles lift in tiles_bag.

        Args:
            tile (str): requested tile.
        Returns:
            removed (bool): True if tile were successfully removed from
                tile_bag and _tiles_string; False otherwise.
        """
        removed = False
        tile_count = self.tile_bag[tile][0]
        if tile_count > 0:
            self.tile_bag[tile][0] -= 1
            self._tiles_string = self._tiles_string.replace(tile, "")
            removed = True
        else:
            print("Invalid input.")
            print("More %s's have been taken from the bag than possible."
                  % tile)
        return removed

    def get_tiles_left(self):
        """Get dict {amount_left: [tiles],...} from the tile_bag.

        Returns:
            tiles_left (dict): {count: [tiles], ...}.
        """
        sorted_keys = sorted(self.tile_bag)
        counts = sorted(set([count for [count, _] in
                             self.tile_bag.values()]), reverse=True)
        tiles_left = {}
        for count in counts:
            tiles = []
            for tile in sorted_keys:
                if self.tile_bag[tile][0] == count:
                    tiles.append(tile)
            tiles_left[count] = tiles
        return tiles_left

    def take_tiles_set(self, tile_set=None):
        """Take specific set of tiles from the tiles_bag.

        Args:
            tile_set (str or list): set of predefined tiles.
        Returns:
            player_tiles (list): list of tiles taken from the tile_bag.
        """
        player_tiles = []
        # ensured that requested tiles in the upper case
        tile_set = tile_set.upper()

        for tile in tile_set:
            tile_removed = self._take_one_tile(tile)
            if not tile_removed:
                break
            player_tiles.append(tile)
        return player_tiles

    def take_tiles_num(self, num=0):
        """Take specific number of random tiles from the tiles_bag.

        Args:
            num (int): get that amount of random tiles from the tiles_bag.
        Returns:
            player_tiles (list): list of tiles taken from the tile_bag.
        """
        player_tiles = []
        if num <= len(self._tiles_string):
            tile_set = random.sample(self._tiles_string, num)
        else:
            print("There is less then %d in the bag" % num)
            return
        for tile in tile_set:
            tile_removed = self._take_one_tile(tile)
            if not tile_removed:
                break
            player_tiles.append(tile)
        return player_tiles

if __name__ == '__main__':
    bag = Scrubble()
    bag.take_tiles_set('AXHDRUIOR_XHJZUQEE')
    tiles_in_bag = bag.get_tiles_left()
    
    for c in sorted(tiles_in_bag, reverse=True):
        print(c, tiles_in_bag[c])
