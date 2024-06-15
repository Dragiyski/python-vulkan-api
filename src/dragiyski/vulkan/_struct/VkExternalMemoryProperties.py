import ctypes, sys

class VkExternalMemoryProperties(ctypes.Structure):
    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExternalMemoryProperties
