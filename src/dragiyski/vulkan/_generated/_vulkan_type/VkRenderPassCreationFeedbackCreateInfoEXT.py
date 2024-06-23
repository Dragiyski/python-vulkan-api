import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassCreationFeedbackInfoEXT import CType as VkRenderPassCreationFeedbackInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pRenderPassFeedback', ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]

descriptor = {
    'extends': {
        'VkRenderPassCreateInfo2',
    },
    'extended_by': set(),
    'includes': {
        'VkRenderPassCreationFeedbackInfoEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_FEEDBACK_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pRenderPassFeedback': {'python_name': ['p', 'render', 'pass', 'feedback'], 'type': 'VkRenderPassCreationFeedbackInfoEXT'},
    }
}
