from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFloatControlsProperties'
_member_list_ = ['sType', 'pNext', 'denormBehaviorIndependence', 'roundingModeIndependence', 'shaderSignedZeroInfNanPreserveFloat16', 'shaderSignedZeroInfNanPreserveFloat32', 'shaderSignedZeroInfNanPreserveFloat64', 'shaderDenormPreserveFloat16', 'shaderDenormPreserveFloat32', 'shaderDenormPreserveFloat64', 'shaderDenormFlushToZeroFloat16', 'shaderDenormFlushToZeroFloat32', 'shaderDenormFlushToZeroFloat64', 'shaderRoundingModeRTEFloat16', 'shaderRoundingModeRTEFloat32', 'shaderRoundingModeRTEFloat64', 'shaderRoundingModeRTZFloat16', 'shaderRoundingModeRTZFloat32', 'shaderRoundingModeRTZFloat64']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'denormBehaviorIndependence': {
        'type': CIntType('c_int'),
        'type_name': 'VkShaderFloatControlsIndependence',
        'enum': 'VkShaderFloatControlsIndependence',
        'is_string': False,
    },
    'roundingModeIndependence': {
        'type': CIntType('c_int'),
        'type_name': 'VkShaderFloatControlsIndependence',
        'enum': 'VkShaderFloatControlsIndependence',
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
