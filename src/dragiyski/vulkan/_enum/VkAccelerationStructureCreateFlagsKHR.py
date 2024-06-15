import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkAccelerationStructureCreateFlagsKHR(VulkanUIntFlag):
    VK_ACCELERATION_STRUCTURE_CREATE_MOTION_BIT_NV = 4
    VK_ACCELERATION_STRUCTURE_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = 1
    VK_ACCELERATION_STRUCTURE_CREATE_DESCRIPTOR_BUFFER_CAPTURE_REPLAY_BIT_EXT = 8

sys.modules[__name__] = VkAccelerationStructureCreateFlagsKHR
