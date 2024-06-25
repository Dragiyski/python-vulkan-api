import ctypes

class VkPhysicalDeviceFloatControlsProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'denormBehaviorIndependence': ctypes.c_int,
            'roundingModeIndependence': ctypes.c_int,
            'shaderSignedZeroInfNanPreserveFloat16': ctypes.c_uint32,
            'shaderSignedZeroInfNanPreserveFloat32': ctypes.c_uint32,
            'shaderSignedZeroInfNanPreserveFloat64': ctypes.c_uint32,
            'shaderDenormPreserveFloat16': ctypes.c_uint32,
            'shaderDenormPreserveFloat32': ctypes.c_uint32,
            'shaderDenormPreserveFloat64': ctypes.c_uint32,
            'shaderDenormFlushToZeroFloat16': ctypes.c_uint32,
            'shaderDenormFlushToZeroFloat32': ctypes.c_uint32,
            'shaderDenormFlushToZeroFloat64': ctypes.c_uint32,
            'shaderRoundingModeRTEFloat16': ctypes.c_uint32,
            'shaderRoundingModeRTEFloat32': ctypes.c_uint32,
            'shaderRoundingModeRTEFloat64': ctypes.c_uint32,
            'shaderRoundingModeRTZFloat16': ctypes.c_uint32,
            'shaderRoundingModeRTZFloat32': ctypes.c_uint32,
            'shaderRoundingModeRTZFloat64': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('denormBehaviorIndependence', ctypes.c_int),
        ('roundingModeIndependence', ctypes.c_int),
        ('shaderSignedZeroInfNanPreserveFloat16', ctypes.c_uint32),
        ('shaderSignedZeroInfNanPreserveFloat32', ctypes.c_uint32),
        ('shaderSignedZeroInfNanPreserveFloat64', ctypes.c_uint32),
        ('shaderDenormPreserveFloat16', ctypes.c_uint32),
        ('shaderDenormPreserveFloat32', ctypes.c_uint32),
        ('shaderDenormPreserveFloat64', ctypes.c_uint32),
        ('shaderDenormFlushToZeroFloat16', ctypes.c_uint32),
        ('shaderDenormFlushToZeroFloat32', ctypes.c_uint32),
        ('shaderDenormFlushToZeroFloat64', ctypes.c_uint32),
        ('shaderRoundingModeRTEFloat16', ctypes.c_uint32),
        ('shaderRoundingModeRTEFloat32', ctypes.c_uint32),
        ('shaderRoundingModeRTEFloat64', ctypes.c_uint32),
        ('shaderRoundingModeRTZFloat16', ctypes.c_uint32),
        ('shaderRoundingModeRTZFloat32', ctypes.c_uint32),
        ('shaderRoundingModeRTZFloat64', ctypes.c_uint32),
    ]
