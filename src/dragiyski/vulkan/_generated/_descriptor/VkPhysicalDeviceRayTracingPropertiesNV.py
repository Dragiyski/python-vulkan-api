from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRayTracingPropertiesNV'
_member_list_ = ['sType', 'pNext', 'shaderGroupHandleSize', 'maxRecursionDepth', 'maxShaderGroupStride', 'shaderGroupBaseAlignment', 'maxGeometryCount', 'maxInstanceCount', 'maxTriangleCount', 'maxDescriptorSetAccelerationStructures']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderGroupHandleSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxRecursionDepth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxShaderGroupStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderGroupBaseAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxInstanceCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxTriangleCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxDescriptorSetAccelerationStructures': {
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
