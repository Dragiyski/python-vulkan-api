import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPointClippingBehavior(VulkanIntEnum):
    VK_POINT_CLIPPING_BEHAVIOR_ALL_CLIP_PLANES = 0
    VK_POINT_CLIPPING_BEHAVIOR_USER_CLIP_PLANES_ONLY = 1

sys.modules[__name__] = VkPointClippingBehavior
