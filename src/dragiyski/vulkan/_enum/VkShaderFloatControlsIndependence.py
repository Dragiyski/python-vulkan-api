import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkShaderFloatControlsIndependence(VulkanIntEnum):
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE = 2
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL = 1
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY = 0

sys.modules[__name__] = VkShaderFloatControlsIndependence
