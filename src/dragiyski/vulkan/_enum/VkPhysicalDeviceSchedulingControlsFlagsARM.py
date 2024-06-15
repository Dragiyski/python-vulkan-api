import ctypes, sys
from .._vulkan_base import VulkanULongFlag

class VkPhysicalDeviceSchedulingControlsFlagsARM(VulkanULongFlag):
    VK_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_SHADER_CORE_COUNT_ARM = 1

sys.modules[__name__] = VkPhysicalDeviceSchedulingControlsFlagsARM
