from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferSubmitInfo'
_member_list_ = ['sType', 'pNext', 'commandBuffer', 'deviceMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_SUBMIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkRenderPassStripeSubmitInfoARM',
}
_includes_ = set()
_included_in_ = {
    'VkSubmitInfo2',
}
_input_of_ = set()
_output_of_ = set()
