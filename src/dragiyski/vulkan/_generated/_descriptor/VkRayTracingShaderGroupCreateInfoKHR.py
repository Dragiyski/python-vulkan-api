from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRayTracingShaderGroupCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'type', 'generalShader', 'closestHitShader', 'anyHitShader', 'intersectionShader', 'pShaderGroupCaptureReplayHandle']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkRayTracingShaderGroupTypeKHR',
        'enum': 'VkRayTracingShaderGroupTypeKHR',
        'is_string': False,
    },
    'generalShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'closestHitShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'anyHitShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'intersectionShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pShaderGroupCaptureReplayHandle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRayTracingPipelineCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
