import ctypes, sys

class VkPhysicalDeviceSparseProperties(ctypes.Structure):
    _fields_ = [
        ('residencyStandard2DBlockShape', ctypes.c_uint32),
        ('residencyStandard2DMultisampleBlockShape', ctypes.c_uint32),
        ('residencyStandard3DBlockShape', ctypes.c_uint32),
        ('residencyAlignedMipSize', ctypes.c_uint32),
        ('residencyNonResidentStrict', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceSparseProperties
