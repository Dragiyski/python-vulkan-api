from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassStripeSubmitInfoARM'
_member_list_ = ['sType', 'pNext', 'stripeSemaphoreInfoCount', 'pStripeSemaphoreInfos']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_SUBMIT_INFO_ARM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stripeSemaphoreInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStripeSemaphoreInfos': {
        'type': CPointerType(CComplexType('VkSemaphoreSubmitInfo')),
        'type_name': 'VkSemaphoreSubmitInfo',
        'structure': 'VkSemaphoreSubmitInfo',
        'length': [['stripeSemaphoreInfoCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkCommandBufferSubmitInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkSemaphoreSubmitInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
