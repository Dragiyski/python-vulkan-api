import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkBlockMatchWindowCompareModeQCOM(VulkanIntEnum):
    VK_BLOCK_MATCH_WINDOW_COMPARE_MODE_MIN_QCOM = 0
    VK_BLOCK_MATCH_WINDOW_COMPARE_MODE_MAX_QCOM = 1

sys.modules[__name__] = VkBlockMatchWindowCompareModeQCOM
