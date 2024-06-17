import ctypes, sys

class VkGeometryAABBNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('aabbData', ctypes.c_void_p),
        ('numAABBs', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('offset', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkGeometryAABBNV
