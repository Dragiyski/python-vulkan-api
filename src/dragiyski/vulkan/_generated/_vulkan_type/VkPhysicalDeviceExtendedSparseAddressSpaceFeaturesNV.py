import ctypes

class VkPhysicalDeviceExtendedSparseAddressSpaceFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedSparseAddressSpace', ctypes.c_uint32),
    ]

VkPhysicalDeviceExtendedSparseAddressSpaceFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'extendedSparseAddressSpace': ctypes.c_uint32,
}
