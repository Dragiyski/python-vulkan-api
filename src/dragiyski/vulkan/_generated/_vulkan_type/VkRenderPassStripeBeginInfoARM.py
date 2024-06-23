import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassStripeInfoARM import CType as VkRenderPassStripeInfoARM

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRenderPassStripeInfoARM',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_BEGIN_INFO_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stripeInfoCount': {'python_name': ['stripe', 'info', 'count']},
        'pStripeInfos': {'python_name': ['p', 'stripe', 'infos'], 'len': [['stripeInfoCount']], 'type': 'VkRenderPassStripeInfoARM'},
    }
}
