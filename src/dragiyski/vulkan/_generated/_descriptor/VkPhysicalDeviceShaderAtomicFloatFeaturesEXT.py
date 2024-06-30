from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderAtomicFloatFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'shaderBufferFloat32Atomics', 'shaderBufferFloat32AtomicAdd', 'shaderBufferFloat64Atomics', 'shaderBufferFloat64AtomicAdd', 'shaderSharedFloat32Atomics', 'shaderSharedFloat32AtomicAdd', 'shaderSharedFloat64Atomics', 'shaderSharedFloat64AtomicAdd', 'shaderImageFloat32Atomics', 'shaderImageFloat32AtomicAdd', 'sparseImageFloat32Atomics', 'sparseImageFloat32AtomicAdd']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderBufferFloat32Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat32AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat64Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferFloat64AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat32Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat32AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat64Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedFloat64AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderImageFloat32Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderImageFloat32AtomicAdd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sparseImageFloat32Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sparseImageFloat32AtomicAdd': {
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
