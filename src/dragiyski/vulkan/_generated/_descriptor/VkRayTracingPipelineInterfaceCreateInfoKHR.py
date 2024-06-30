from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRayTracingPipelineInterfaceCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'maxPipelineRayPayloadSize', 'maxPipelineRayHitAttributeSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxPipelineRayPayloadSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPipelineRayHitAttributeSize': {
        'type': CIntType('c_uint32'),
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
