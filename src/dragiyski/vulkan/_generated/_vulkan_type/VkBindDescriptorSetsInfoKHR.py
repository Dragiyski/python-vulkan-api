import ctypes

class VkBindDescriptorSetsInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stageFlags': ctypes.c_uint32,
            'layout': ctypes.c_void_p,
            'firstSet': ctypes.c_uint32,
            'descriptorSetCount': ctypes.c_uint32,
            'pDescriptorSets': ctypes.POINTER(ctypes.c_void_p),
            'dynamicOffsetCount': ctypes.c_uint32,
            'pDynamicOffsets': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pDescriptorSets', ctypes.POINTER(ctypes.c_void_p)),
        ('dynamicOffsetCount', ctypes.c_uint32),
        ('pDynamicOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ]
