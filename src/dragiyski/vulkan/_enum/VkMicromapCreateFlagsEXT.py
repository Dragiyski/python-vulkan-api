import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkMicromapCreateFlagsEXT(VulkanUIntFlag):
    VK_MICROMAP_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_EXT = 1

sys.modules[__name__] = VkMicromapCreateFlagsEXT
