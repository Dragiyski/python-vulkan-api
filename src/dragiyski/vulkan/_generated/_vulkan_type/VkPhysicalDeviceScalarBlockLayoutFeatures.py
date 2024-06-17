import ctypes, sys

class VkPhysicalDeviceScalarBlockLayoutFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('scalarBlockLayout', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceScalarBlockLayoutFeatures
