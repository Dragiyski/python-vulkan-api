import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeArea', VkRect2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': {
        'VkRenderPassStripeBeginInfoARM',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_INFO_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stripeArea': {'python_name': ['stripe', 'area'], 'type': 'VkRect2D'},
    }
}
