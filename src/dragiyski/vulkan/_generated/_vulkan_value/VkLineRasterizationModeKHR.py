from enum import IntEnum

class Value(IntEnum):
    VK_LINE_RASTERIZATION_MODE_BRESENHAM_KHR = 2
    VK_LINE_RASTERIZATION_MODE_DEFAULT_KHR = 0
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_KHR = 1
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_KHR = 3
    VK_LINE_RASTERIZATION_MODE_BRESENHAM_EXT = VK_LINE_RASTERIZATION_MODE_BRESENHAM_KHR
    VK_LINE_RASTERIZATION_MODE_DEFAULT_EXT = VK_LINE_RASTERIZATION_MODE_DEFAULT_KHR
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_EXT = VK_LINE_RASTERIZATION_MODE_RECTANGULAR_KHR
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_EXT = VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_KHR