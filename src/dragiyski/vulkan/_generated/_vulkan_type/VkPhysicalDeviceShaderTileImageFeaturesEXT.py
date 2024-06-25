import ctypes

class VkPhysicalDeviceShaderTileImageFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderTileImageColorReadAccess': ctypes.c_uint32,
            'shaderTileImageDepthReadAccess': ctypes.c_uint32,
            'shaderTileImageStencilReadAccess': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageColorReadAccess', ctypes.c_uint32),
        ('shaderTileImageDepthReadAccess', ctypes.c_uint32),
        ('shaderTileImageStencilReadAccess', ctypes.c_uint32),
    ]
