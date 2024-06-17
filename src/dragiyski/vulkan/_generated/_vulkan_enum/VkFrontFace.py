import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFrontFace(VulkanIntEnum):
    VK_FRONT_FACE_CLOCKWISE = 1
    VK_FRONT_FACE_COUNTER_CLOCKWISE = 0

sys.modules[__name__] = VkFrontFace

