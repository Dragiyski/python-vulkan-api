import ctypes, sys

class VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveTopologyListRestart', ctypes.c_uint32),
        ('primitiveTopologyPatchListRestart', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT
