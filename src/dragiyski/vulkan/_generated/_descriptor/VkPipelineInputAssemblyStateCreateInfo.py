from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineInputAssemblyStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'topology', 'primitiveRestartEnable']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineInputAssemblyStateCreateFlags',
        'enum': 'VkPipelineInputAssemblyStateCreateFlags',
        'is_string': False,
    },
    'topology': {
        'type': CIntType('c_int'),
        'type_name': 'VkPrimitiveTopology',
        'enum': 'VkPrimitiveTopology',
        'is_string': False,
    },
    'primitiveRestartEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
