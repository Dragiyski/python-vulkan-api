import ctypes

class VkBufferCollectionBufferCreateInfoFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('collection', ctypes.c_void_p),
        ('index', ctypes.c_uint32),
    ]

VkBufferCollectionBufferCreateInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'collection': ctypes.c_void_p,
    'index': ctypes.c_uint32,
}
