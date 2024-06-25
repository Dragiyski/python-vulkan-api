import ctypes

class VkSetDescriptorBufferOffsetsInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stageFlags': ctypes.c_uint32,
            'layout': ctypes.c_void_p,
            'firstSet': ctypes.c_uint32,
            'setCount': ctypes.c_uint32,
            'pBufferIndices': ctypes.POINTER(ctypes.c_uint32),
            'pOffsets': ctypes.POINTER(ctypes.c_uint64),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('setCount', ctypes.c_uint32),
        ('pBufferIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pOffsets', ctypes.POINTER(ctypes.c_uint64)),
    ]
