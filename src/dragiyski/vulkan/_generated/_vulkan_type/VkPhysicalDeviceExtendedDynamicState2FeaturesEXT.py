import ctypes

class VkPhysicalDeviceExtendedDynamicState2FeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'extendedDynamicState2': ctypes.c_uint32,
            'extendedDynamicState2LogicOp': ctypes.c_uint32,
            'extendedDynamicState2PatchControlPoints': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedDynamicState2', ctypes.c_uint32),
        ('extendedDynamicState2LogicOp', ctypes.c_uint32),
        ('extendedDynamicState2PatchControlPoints', ctypes.c_uint32),
    ]
