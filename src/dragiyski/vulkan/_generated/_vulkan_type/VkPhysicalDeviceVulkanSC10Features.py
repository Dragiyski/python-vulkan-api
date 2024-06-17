import ctypes, sys

class VkPhysicalDeviceVulkanSC10Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderAtomicInstructions', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVulkanSC10Features
