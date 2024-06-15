import ctypes, sys

class VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageSlicedViewOf3D', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT
