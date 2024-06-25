import ctypes

class VkPhysicalDeviceSparseProperties(ctypes.Structure):
    _fields_ = [
        ('residencyStandard2DBlockShape', ctypes.c_uint32),
        ('residencyStandard2DMultisampleBlockShape', ctypes.c_uint32),
        ('residencyStandard3DBlockShape', ctypes.c_uint32),
        ('residencyAlignedMipSize', ctypes.c_uint32),
        ('residencyNonResidentStrict', ctypes.c_uint32),
    ]

VkPhysicalDeviceSparseProperties._type_ = {
    'residencyStandard2DBlockShape': ctypes.c_uint32,
    'residencyStandard2DMultisampleBlockShape': ctypes.c_uint32,
    'residencyStandard3DBlockShape': ctypes.c_uint32,
    'residencyAlignedMipSize': ctypes.c_uint32,
    'residencyNonResidentStrict': ctypes.c_uint32,
}
