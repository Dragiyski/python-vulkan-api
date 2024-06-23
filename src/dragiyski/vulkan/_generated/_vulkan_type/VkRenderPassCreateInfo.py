import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentDescription import CType as VkAttachmentDescription
from .VkSubpassDependency import CType as VkSubpassDependency
from .VkSubpassDescription import CType as VkSubpassDescription

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
        'VkRenderPassInputAttachmentAspectCreateInfo',
        'VkRenderPassMultiviewCreateInfo',
    },
    'includes': {
        'VkAttachmentDescription',
        'VkSubpassDependency',
        'VkSubpassDescription',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateRenderPass',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkRenderPassCreateFlags'},
        'attachmentCount': {'python_name': ['attachment', 'count']},
        'pAttachments': {'python_name': ['p', 'attachments'], 'len': [['attachmentCount']], 'type': 'VkAttachmentDescription'},
        'subpassCount': {'python_name': ['subpass', 'count']},
        'pSubpasses': {'python_name': ['p', 'subpasses'], 'len': [['subpassCount']], 'type': 'VkSubpassDescription'},
        'dependencyCount': {'python_name': ['dependency', 'count']},
        'pDependencies': {'python_name': ['p', 'dependencies'], 'len': [['dependencyCount']], 'type': 'VkSubpassDependency'},
    }
}
