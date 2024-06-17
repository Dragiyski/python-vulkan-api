import ctypes, sys

class VkBufferCollectionConstraintsInfoFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minBufferCount', ctypes.c_uint32),
        ('maxBufferCount', ctypes.c_uint32),
        ('minBufferCountForCamping', ctypes.c_uint32),
        ('minBufferCountForDedicatedSlack', ctypes.c_uint32),
        ('minBufferCountForSharedSlack', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkBufferCollectionConstraintsInfoFUCHSIA
