from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSemaphoreSubmitInfo'
_member_list_ = ['sType', 'pNext', 'semaphore', 'value', 'stageMask', 'deviceIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_SUBMIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'semaphore': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'value': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'stageMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkPipelineStageFlags2',
        'enum': 'VkPipelineStageFlags2',
        'is_string': False,
    },
    'deviceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassStripeSubmitInfoARM',
    'VkSubmitInfo2',
}
_input_of_ = set()
_output_of_ = set()
