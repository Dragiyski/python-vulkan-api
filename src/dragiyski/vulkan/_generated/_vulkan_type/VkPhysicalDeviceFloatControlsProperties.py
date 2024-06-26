import ctypes

class VkPhysicalDeviceFloatControlsProperties(ctypes.Structure):
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

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'denormBehaviorIndependence': 'denorm_behavior_independence',
        'roundingModeIndependence': 'rounding_mode_independence',
        'shaderSignedZeroInfNanPreserveFloat16': 'shader_signed_zero_inf_nan_preserve_float16',
        'shaderSignedZeroInfNanPreserveFloat32': 'shader_signed_zero_inf_nan_preserve_float32',
        'shaderSignedZeroInfNanPreserveFloat64': 'shader_signed_zero_inf_nan_preserve_float64',
        'shaderDenormPreserveFloat16': 'shader_denorm_preserve_float16',
        'shaderDenormPreserveFloat32': 'shader_denorm_preserve_float32',
        'shaderDenormPreserveFloat64': 'shader_denorm_preserve_float64',
        'shaderDenormFlushToZeroFloat16': 'shader_denorm_flush_to_zero_float16',
        'shaderDenormFlushToZeroFloat32': 'shader_denorm_flush_to_zero_float32',
        'shaderDenormFlushToZeroFloat64': 'shader_denorm_flush_to_zero_float64',
        'shaderRoundingModeRTEFloat16': 'shader_rounding_mode_rtefloat16',
        'shaderRoundingModeRTEFloat32': 'shader_rounding_mode_rtefloat32',
        'shaderRoundingModeRTEFloat64': 'shader_rounding_mode_rtefloat64',
        'shaderRoundingModeRTZFloat16': 'shader_rounding_mode_rtzfloat16',
        'shaderRoundingModeRTZFloat32': 'shader_rounding_mode_rtzfloat32',
        'shaderRoundingModeRTZFloat64': 'shader_rounding_mode_rtzfloat64',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'denormBehaviorIndependence': 'VkShaderFloatControlsIndependence',
        'roundingModeIndependence': 'VkShaderFloatControlsIndependence',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFloatControlsProperties._type_ = {
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
