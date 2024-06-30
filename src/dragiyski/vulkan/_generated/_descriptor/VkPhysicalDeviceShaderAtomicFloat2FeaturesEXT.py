from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT'
_member_list_ = ['sType', 'pNext', 'shaderBufferFloat16Atomics', 'shaderBufferFloat16AtomicAdd', 'shaderBufferFloat16AtomicMinMax', 'shaderBufferFloat32AtomicMinMax', 'shaderBufferFloat64AtomicMinMax', 'shaderSharedFloat16Atomics', 'shaderSharedFloat16AtomicAdd', 'shaderSharedFloat16AtomicMinMax', 'shaderSharedFloat32AtomicMinMax', 'shaderSharedFloat64AtomicMinMax', 'shaderImageFloat32AtomicMinMax', 'sparseImageFloat32AtomicMinMax']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_2_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderBufferFloat16Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat16AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat16AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat32AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat64AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat16Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat16AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat16AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat32AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat64AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderImageFloat32AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sparseImageFloat32AtomicMinMax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
