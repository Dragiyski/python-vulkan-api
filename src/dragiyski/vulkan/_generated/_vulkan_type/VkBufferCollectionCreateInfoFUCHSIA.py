import ctypes, sys

class VkBufferCollectionCreateInfoFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('collectionToken', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkBufferCollectionCreateInfoFUCHSIA
