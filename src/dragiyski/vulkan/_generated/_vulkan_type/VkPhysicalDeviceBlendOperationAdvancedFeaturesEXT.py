import ctypes

class VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('advancedBlendCoherentOperations', ctypes.c_uint32),
    ]

VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'advancedBlendCoherentOperations': ctypes.c_uint32,
}
