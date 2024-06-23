import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentDescription2 import CType as VkAttachmentDescription2
from .VkSubpassDependency2 import CType as VkSubpassDependency2
from .VkSubpassDescription2 import CType as VkSubpassDescription2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription2)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription2)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency2)),
    ('correlatedViewMaskCount', ctypes.c_uint32),
    ('pCorrelatedViewMasks', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkRenderPassCreationControlEXT',
        'VkRenderPassCreationFeedbackCreateInfoEXT',
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
    },
    'includes': {
        'VkAttachmentDescription2',
        'VkSubpassDependency2',
        'VkSubpassDescription2',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateRenderPass2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkRenderPassCreateFlags'},
        'attachmentCount': {'python_name': ['attachment', 'count']},
        'pAttachments': {'python_name': ['p', 'attachments'], 'len': [['attachmentCount']], 'type': 'VkAttachmentDescription2'},
        'subpassCount': {'python_name': ['subpass', 'count']},
        'pSubpasses': {'python_name': ['p', 'subpasses'], 'len': [['subpassCount']], 'type': 'VkSubpassDescription2'},
        'dependencyCount': {'python_name': ['dependency', 'count']},
        'pDependencies': {'python_name': ['p', 'dependencies'], 'len': [['dependencyCount']], 'type': 'VkSubpassDependency2'},
        'correlatedViewMaskCount': {'python_name': ['correlated', 'view', 'mask', 'count']},
        'pCorrelatedViewMasks': {'python_name': ['p', 'correlated', 'view', 'masks'], 'len': [['correlatedViewMaskCount']]},
    }
}
