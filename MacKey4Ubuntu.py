# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define_keymap({
#     K("L_SUPER"): K("LEFT_CTRL"),
#     K("R_SUPER"): K("RIGHT_CTRL"),
# })

define_multipurpose_modmap({
    # SandS
    # Key.Super_L: [Key.Control_L],
    # Key.Super_R: [Key.Control_R],
    # Key.LEFT_ALT: [Key.LEFT_CTRL],
    # Key.CAPSLOCK: [Key.LEFT_CTRL],
    Key.SPACE: [Key.SPACE, Key.LEFT_SHIFT],
    Key.CAPSLOCK: [Key.LEFT_ALT, Key.LEFT_META],
    Key.LEFT_META: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.RIGHT_META: [Key.HENKAN, Key.RIGHT_CTRL]
})
