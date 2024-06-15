import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkBlockMatchWindowCompareModeQCOM(VulkanIntEnum):
    VK_BLOCK_MATCH_WINDOW_COMPARE_MODE_MAX_QCOM = 1
    VK_BLOCK_MATCH_WINDOW_COMPARE_MODE_MIN_QCOM = 0

sys.modules[__name__] = VkBlockMatchWindowCompareModeQCOM

