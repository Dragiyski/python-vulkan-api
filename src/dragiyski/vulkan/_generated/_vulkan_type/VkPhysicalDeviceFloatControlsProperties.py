import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'denormBehaviorIndependence': {'python_name': ['denorm', 'behavior', 'independence'], 'type': 'VkShaderFloatControlsIndependence'},
        'roundingModeIndependence': {'python_name': ['rounding', 'mode', 'independence'], 'type': 'VkShaderFloatControlsIndependence'},
        'shaderSignedZeroInfNanPreserveFloat16': {'python_name': ['shader', 'signed', 'zero', 'inf', 'nan', 'preserve', 'float16']},
        'shaderSignedZeroInfNanPreserveFloat32': {'python_name': ['shader', 'signed', 'zero', 'inf', 'nan', 'preserve', 'float32']},
        'shaderSignedZeroInfNanPreserveFloat64': {'python_name': ['shader', 'signed', 'zero', 'inf', 'nan', 'preserve', 'float64']},
        'shaderDenormPreserveFloat16': {'python_name': ['shader', 'denorm', 'preserve', 'float16']},
        'shaderDenormPreserveFloat32': {'python_name': ['shader', 'denorm', 'preserve', 'float32']},
        'shaderDenormPreserveFloat64': {'python_name': ['shader', 'denorm', 'preserve', 'float64']},
        'shaderDenormFlushToZeroFloat16': {'python_name': ['shader', 'denorm', 'flush', 'to', 'zero', 'float16']},
        'shaderDenormFlushToZeroFloat32': {'python_name': ['shader', 'denorm', 'flush', 'to', 'zero', 'float32']},
        'shaderDenormFlushToZeroFloat64': {'python_name': ['shader', 'denorm', 'flush', 'to', 'zero', 'float64']},
        'shaderRoundingModeRTEFloat16': {'python_name': ['shader', 'rounding', 'mode', 'rtefloat16']},
        'shaderRoundingModeRTEFloat32': {'python_name': ['shader', 'rounding', 'mode', 'rtefloat32']},
        'shaderRoundingModeRTEFloat64': {'python_name': ['shader', 'rounding', 'mode', 'rtefloat64']},
        'shaderRoundingModeRTZFloat16': {'python_name': ['shader', 'rounding', 'mode', 'rtzfloat16']},
        'shaderRoundingModeRTZFloat32': {'python_name': ['shader', 'rounding', 'mode', 'rtzfloat32']},
        'shaderRoundingModeRTZFloat64': {'python_name': ['shader', 'rounding', 'mode', 'rtzfloat64']},
    }
}
