from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCheckpointDataNV'
_member_list_ = ['sType', 'pNext', 'stage', 'pCheckpointMarker']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineStageFlagBits',
        'is_string': False,
    },
    'pCheckpointMarker': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetQueueCheckpointDataNV',
}
