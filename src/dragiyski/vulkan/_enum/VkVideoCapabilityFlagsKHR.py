import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoCapabilityFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_CAPABILITY_SEPARATE_REFERENCE_IMAGES_BIT_KHR = 2
    VK_VIDEO_CAPABILITY_PROTECTED_CONTENT_BIT_KHR = 1

sys.modules[__name__] = VkVideoCapabilityFlagsKHR
