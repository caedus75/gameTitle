# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class GB(Platform):
    def __init__(self):
        header = memLocation(0x100, None, 80)
        title = memLocation(0x34, 0x43, None)
        code = memLocation(None, None, None)
        super().__init__(header, title, code)