import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorBuffer', ctypes.c_uint32),
        ('descriptorBufferCaptureReplay', ctypes.c_uint32),
        ('descriptorBufferImageLayoutIgnored', ctypes.c_uint32),
        ('descriptorBufferPushDescriptors', ctypes.c_uint32),
    ]
