from enum import IntEnum

class VkPhysicalDeviceType(IntEnum):
    VK_PHYSICAL_DEVICE_TYPE_CPU = 4
    VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = 2
    VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = 1
    VK_PHYSICAL_DEVICE_TYPE_OTHER = 0
    VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = 3
