import ctypes

class VkExternalMemoryProperties(ctypes.Structure):
    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]

VkExternalMemoryProperties._type_ = {
    'externalMemoryFeatures': ctypes.c_uint32,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
}
