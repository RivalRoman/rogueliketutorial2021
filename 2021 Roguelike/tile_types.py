from typing import Tuple

import numpy as np #type: ignore

#tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #unicode codepoint
        ("fg", "3B"), #3 unsigned bytes for rgb colors
        ("bg", "3B"),
    ]
)

#Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #true if this tile can be walked over
        ("transparent", np.bool), #true if this tile doesn't block Fov
        ("dark", graphic_dt), #graphics for when this tile is not in Fov
    ]
)

def new_tile(
    *, #enforce the use of keywords so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
   """Helper function for defining individual tile types """
   return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (188, 187, 187)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (46, 46, 46)),
)