import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDeviceAddressBindingFlagsEXT(VulkanUIntFlag):
    VK_DEVICE_ADDRESS_BINDING_INTERNAL_OBJECT_BIT_EXT = 1

sys.modules[__name__] = VkDeviceAddressBindingFlagsEXT

