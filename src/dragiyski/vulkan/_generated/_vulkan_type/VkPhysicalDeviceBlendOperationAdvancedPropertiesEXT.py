import ctypes

class VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'advancedBlendMaxColorAttachments': ctypes.c_uint32,
            'advancedBlendIndependentBlend': ctypes.c_uint32,
            'advancedBlendNonPremultipliedSrcColor': ctypes.c_uint32,
            'advancedBlendNonPremultipliedDstColor': ctypes.c_uint32,
            'advancedBlendCorrelatedOverlap': ctypes.c_uint32,
            'advancedBlendAllOperations': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('advancedBlendMaxColorAttachments', ctypes.c_uint32),
        ('advancedBlendIndependentBlend', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedSrcColor', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedDstColor', ctypes.c_uint32),
        ('advancedBlendCorrelatedOverlap', ctypes.c_uint32),
        ('advancedBlendAllOperations', ctypes.c_uint32),
    ]
