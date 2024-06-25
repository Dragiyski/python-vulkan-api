import ctypes

class VkCommandPoolMemoryConsumption(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPoolAllocated', ctypes.c_uint64),
        ('commandPoolReservedSize', ctypes.c_uint64),
        ('commandBufferAllocated', ctypes.c_uint64),
    ]

VkCommandPoolMemoryConsumption._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'commandPoolAllocated': ctypes.c_uint64,
    'commandPoolReservedSize': ctypes.c_uint64,
    'commandBufferAllocated': ctypes.c_uint64,
}
