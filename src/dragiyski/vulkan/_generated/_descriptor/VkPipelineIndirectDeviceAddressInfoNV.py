from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineIndirectDeviceAddressInfoNV'
_member_list_ = ['sType', 'pNext', 'pipelineBindPoint', 'pipeline']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_INDIRECT_DEVICE_ADDRESS_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPipelineIndirectDeviceAddressNV',
}
_output_of_ = set()
