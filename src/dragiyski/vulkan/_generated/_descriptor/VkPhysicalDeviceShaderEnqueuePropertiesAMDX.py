from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderEnqueuePropertiesAMDX'
_member_list_ = ['sType', 'pNext', 'maxExecutionGraphDepth', 'maxExecutionGraphShaderOutputNodes', 'maxExecutionGraphShaderPayloadSize', 'maxExecutionGraphShaderPayloadCount', 'executionGraphDispatchAddressAlignment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_PROPERTIES_AMDX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxExecutionGraphDepth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxExecutionGraphShaderOutputNodes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxExecutionGraphShaderPayloadSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxExecutionGraphShaderPayloadCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'executionGraphDispatchAddressAlignment': {
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
