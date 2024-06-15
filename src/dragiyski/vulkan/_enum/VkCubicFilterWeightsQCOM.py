import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCubicFilterWeightsQCOM(VulkanIntEnum):
    VK_CUBIC_FILTER_WEIGHTS_B_SPLINE_QCOM = 2
    VK_CUBIC_FILTER_WEIGHTS_CATMULL_ROM_QCOM = 0
    VK_CUBIC_FILTER_WEIGHTS_MITCHELL_NETRAVALI_QCOM = 3
    VK_CUBIC_FILTER_WEIGHTS_ZERO_TANGENT_CARDINAL_QCOM = 1

sys.modules[__name__] = VkCubicFilterWeightsQCOM

