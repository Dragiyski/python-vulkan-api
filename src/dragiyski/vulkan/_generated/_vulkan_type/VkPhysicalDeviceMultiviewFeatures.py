import ctypes, sys

class VkPhysicalDeviceMultiviewFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiview', ctypes.c_uint32),
        ('multiviewGeometryShader', ctypes.c_uint32),
        ('multiviewTessellationShader', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultiviewFeatures
