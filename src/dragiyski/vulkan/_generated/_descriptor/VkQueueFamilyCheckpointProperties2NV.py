from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueueFamilyCheckpointProperties2NV'
_member_list_ = ['sType', 'pNext', 'checkpointExecutionStageMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_2_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'checkpointExecutionStageMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkPipelineStageFlags2',
        'enum': 'VkPipelineStageFlags2',
        'is_string': False,
    },
}
_extends_ = {
    'VkQueueFamilyProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
