from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassStripeBeginInfoARM'
_member_list_ = ['sType', 'pNext', 'stripeInfoCount', 'pStripeInfos']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_BEGIN_INFO_ARM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stripeInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStripeInfos': {
        'type': CPointerType(CComplexType('VkRenderPassStripeInfoARM')),
        'type_name': 'VkRenderPassStripeInfoARM',
        'structure': 'VkRenderPassStripeInfoARM',
        'length': [['stripeInfoCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassBeginInfo',
    'VkRenderingInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkRenderPassStripeInfoARM',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
