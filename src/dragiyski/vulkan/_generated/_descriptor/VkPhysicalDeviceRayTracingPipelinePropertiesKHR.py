from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRayTracingPipelinePropertiesKHR'
_member_list_ = ['sType', 'pNext', 'shaderGroupHandleSize', 'maxRayRecursionDepth', 'maxShaderGroupStride', 'shaderGroupBaseAlignment', 'shaderGroupHandleCaptureReplaySize', 'maxRayDispatchInvocationCount', 'shaderGroupHandleAlignment', 'maxRayHitAttributeSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR',
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
    'maxRayRecursionDepth': {
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
    'shaderGroupHandleCaptureReplaySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxRayDispatchInvocationCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderGroupHandleAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxRayHitAttributeSize': {
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
