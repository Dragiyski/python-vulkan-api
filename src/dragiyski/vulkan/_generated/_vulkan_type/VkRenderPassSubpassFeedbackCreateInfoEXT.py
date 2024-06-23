import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassSubpassFeedbackInfoEXT import CType as VkRenderPassSubpassFeedbackInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]

descriptor = {
    'extends': {
        'VkSubpassDescription2',
    },
    'extended_by': set(),
    'includes': {
        'VkRenderPassSubpassFeedbackInfoEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_SUBPASS_FEEDBACK_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pSubpassFeedback': {'python_name': ['p', 'subpass', 'feedback'], 'type': 'VkRenderPassSubpassFeedbackInfoEXT'},
    }
}
