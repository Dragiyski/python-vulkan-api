from enum import IntFlag

class Value(IntFlag):
    VK_CULL_MODE_BACK_BIT = 2
    VK_CULL_MODE_FRONT_AND_BACK = 3
    VK_CULL_MODE_FRONT_BIT = 1
    VK_CULL_MODE_NONE = 0
