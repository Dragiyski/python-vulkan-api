import ctypes

class VkPhysicalDeviceNestedCommandBufferFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'nestedCommandBuffer': ctypes.c_uint32,
            'nestedCommandBufferRendering': ctypes.c_uint32,
            'nestedCommandBufferSimultaneousUse': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nestedCommandBuffer', ctypes.c_uint32),
        ('nestedCommandBufferRendering', ctypes.c_uint32),
        ('nestedCommandBufferSimultaneousUse', ctypes.c_uint32),
    ]
