import ctypes, sys

class VkExternalFenceProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
        ('externalFenceFeatures', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExternalFenceProperties
