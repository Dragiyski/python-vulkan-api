import ctypes, sys

class VkCommandPoolMemoryReservationCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPoolReservedSize', ctypes.c_uint64),
        ('commandPoolMaxCommandBuffers', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkCommandPoolMemoryReservationCreateInfo
