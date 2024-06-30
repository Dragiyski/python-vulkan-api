from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassStripeInfoARM'
_member_list_ = ['sType', 'pNext', 'stripeArea']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_INFO_ARM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stripeArea': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = {
    'VkRenderPassStripeBeginInfoARM',
}
_input_of_ = set()
_output_of_ = set()
