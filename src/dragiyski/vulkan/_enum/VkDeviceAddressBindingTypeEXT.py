import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDeviceAddressBindingTypeEXT(VulkanIntEnum):
    VK_DEVICE_ADDRESS_BINDING_TYPE_BIND_EXT = 0
    VK_DEVICE_ADDRESS_BINDING_TYPE_UNBIND_EXT = 1

sys.modules[__name__] = VkDeviceAddressBindingTypeEXT
