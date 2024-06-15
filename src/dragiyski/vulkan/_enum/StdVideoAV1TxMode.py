import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoAV1TxMode(VulkanIntEnum):
    STD_VIDEO_AV1_TX_MODE_INVALID = 2147483647
    STD_VIDEO_AV1_TX_MODE_LARGEST = 1
    STD_VIDEO_AV1_TX_MODE_ONLY_4X4 = 0
    STD_VIDEO_AV1_TX_MODE_SELECT = 2

sys.modules[__name__] = StdVideoAV1TxMode

