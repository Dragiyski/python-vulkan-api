import ctypes, sys

class VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderZeroInitializeWorkgroupMemory', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeatures
