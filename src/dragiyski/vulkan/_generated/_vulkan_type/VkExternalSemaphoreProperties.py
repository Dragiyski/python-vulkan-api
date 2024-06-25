import ctypes

class VkExternalSemaphoreProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
        ('externalSemaphoreFeatures', ctypes.c_uint32),
    ]

VkExternalSemaphoreProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
    'externalSemaphoreFeatures': ctypes.c_uint32,
}
