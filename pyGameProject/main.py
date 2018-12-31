import os
import pygame

from tileCacheMgr import *

if __name__ == '__main__':
    pygame.init()

    tile_mgr = tile_cache_mgr()

    mario_object = mario()

    tile_mgr.add_element(ELEMENT_MARIO)