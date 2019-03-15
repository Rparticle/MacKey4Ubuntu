# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *


define_multipurpose_modmap({
    # SandS
    Key.SPACE: [Key.SPACE, Key.LEFT_SHIFT],

    # Key Remapping(Caps→Alt, Option→Super)
    Key.CAPSLOCK: [Key.LEFT_ALT, Key.LEFT_ALT],
    Key.LEFT_ALT: [Key.LEFT_META, Key.LEFT_META],

    # 英かな（Cmd→変換、無変換、コンビネーションでCtrl）
    Key.LEFT_META: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.RIGHT_META: [Key.HENKAN, Key.RIGHT_CTRL],
})
