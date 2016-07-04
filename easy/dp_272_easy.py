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
        self.tile_bag = [['_', 2, 0],
                         ['A', 9, 1],
                         ['B', 2, 3],
                         ['C', 2, 3],
                         ['D', 4, 2],
                         ['E', 12, 1],
                         ['F', 2, 4],
                         ['G', 3, 2],
                         ['H', 2, 4],
                         ['I', 9, 1],
                         ['J', 1, 8],
                         ['K', 1, 5],
                         ['L', 4, 1],
                         ['M', 2, 3],
                         ['N', 6, 1],
                         ['O', 8, 1],
                         ['P', 2, 3],
                         ['Q', 1, 10],
                         ['R', 6, 1],
                         ['S', 4, 1],
                         ['T', 6, 1],
                         ['U', 4, 1],
                         ['V', 2, 4],
                         ['W', 2, 4],
                         ['X', 1, 8],
                         ['Y', 2, 4],
                         ['Z', 1, 10]]
        #  non-public attribute _positions added for the fast access
        # to the tile_bag
        self._positions = {tile: pos for (pos, (tile, _, _))
                           in enumerate(self.tile_bag)}
        # non-public attribute _tiles_string used to create
        # random sets of tiles
        self._tiles_string = ""
        for (tile, count, _) in self.tile_bag:
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
        tile_count = self.tile_bag[self._positions[tile]][1]
        if tile_count > 0:
            self.tile_bag[self._positions[tile]][1] -= 1
            self._tiles_string = self._tiles_string.replace(tile, "")
            removed = True
        else:
            print("Invalid input.")
            print("More %s's have been taken from the bag than possible."
                  % tile)
        return removed

    def _sort_bag(self):
        """Sort tile_bag by the amount of tiles left in reverse order.
        
        """
        self._sorted_bag = sorted(self.tile_bag,
                                  key=lambda tile_info: tile_info[1],
                                  reverse=True)

    def get_tiles_left(self):
        """Get an ordered list of lists of tiles that are left in a bag.

        Returns:
            tiles_left (list): ordered list of lists in [[num_left, tile_1,
                tile_2, ...], ...] format of tiles lift in tiles_bag.
        """
        self._sort_bag()

        tiles_left = []

        num_tiles = self._sorted_bag[0][1]
        tiles_left_row = [num_tiles]

        # value in the tuple left unused to provide possibility
        # for the future extension with addition of scores
        for (tile, count, value) in self._sorted_bag:
            if count == num_tiles:
                tiles_left_row.append(tile)
            elif count < num_tiles:
                tiles_left.append(tiles_left_row)

                num_tiles = count
                tiles_left_row = [num_tiles]

                tiles_left_row.append(tile)

        tiles_left.append(tiles_left_row)
        return tiles_left

    def take_tiles(self, tile_set=None, num=0):
        """Take specific set or number of random tiles from the tiles_bag.

        Args:
            tile_set (str or list): set of predefined tiles.
            num (int): get that amount of random tiles or first num
                tiles from tile_set if tile_set is not None.
        Returns:
            player_tiles (list): list of tiles taken from the tile_bag.
        """
        player_tiles = []
        if tile_set:
            # ensured that requested tiles in the upper case
            # to properly access tiles in tile_bag 
            tile_set = tile_set.upper()
            if not num:
                num = len(tile_set)
        else:
            if num <= len(self._tiles_string):
                tile_set = random.sample(self._tiles_string, num)
            else:
                print("There is less then %d in the bag" % num)
                return
        for tile in tile_set[0:num]:
            tile_removed = self._take_one_tile(tile)
            if not tile_removed:
                break
            player_tiles.append(tile)
        return player_tiles



if __name__ == '__main__':
    pass
