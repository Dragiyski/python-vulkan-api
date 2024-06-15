import ctypes, sys

class VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedSparseAddressSpaceSize', ctypes.c_uint64),
        ('extendedSparseImageUsageFlags', ctypes.c_uint32),
        ('extendedSparseBufferUsageFlags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV
