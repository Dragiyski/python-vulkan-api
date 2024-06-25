import ctypes

class VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxWorkGroupCount': ctypes.ARRAY(ctypes.c_uint32, 3),
            'maxWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
            'maxOutputClusterCount': ctypes.c_uint32,
            'indirectBufferOffsetAlignment': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxOutputClusterCount', ctypes.c_uint32),
        ('indirectBufferOffsetAlignment', ctypes.c_uint64),
    ]
