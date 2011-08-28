# Copyright (C) 2011 Michal Zielinski (michal@zielinscy.org.pl)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import freeciv
import pygame

dirkeymap = {
    pygame.K_UP: freeciv.const.DIR8_NORTH,
    pygame.K_RIGHT: freeciv.const.DIR8_EAST,
    pygame.K_LEFT: freeciv.const.DIR8_WEST,
    pygame.K_DOWN: freeciv.const.DIR8_SOUTH,
}

def key(type, key):
    if type == pygame.KEYDOWN:
        if key in dirkeymap:
            direction = dirkeymap[key]
            freeciv.func.key_unit_move_direction(direction)
        if key == pygame.K_g:
            freeciv.func.key_unit_goto()
        if key == pygame.K_ESCAPE:
            freeciv.func.key_cancel_action()
        if key == pygame.K_b:
            freeciv.func.key_unit_build_city()