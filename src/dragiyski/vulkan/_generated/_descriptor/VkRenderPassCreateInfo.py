from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'attachmentCount', 'pAttachments', 'subpassCount', 'pSubpasses', 'dependencyCount', 'pDependencies']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkRenderPassCreateFlags',
        'enum': 'VkRenderPassCreateFlags',
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentDescription')),
        'type_name': 'VkAttachmentDescription',
        'structure': 'VkAttachmentDescription',
        'length': [['attachmentCount']],
        'is_string': False,
    },
    'subpassCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSubpasses': {
        'type': CPointerType(CComplexType('VkSubpassDescription')),
        'type_name': 'VkSubpassDescription',
        'structure': 'VkSubpassDescription',
        'length': [['subpassCount']],
        'is_string': False,
    },
    'dependencyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDependencies': {
        'type': CPointerType(CComplexType('VkSubpassDependency')),
        'type_name': 'VkSubpassDependency',
        'structure': 'VkSubpassDependency',
        'length': [['dependencyCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkRenderPassFragmentDensityMapCreateInfoEXT',
    'VkRenderPassInputAttachmentAspectCreateInfo',
    'VkRenderPassMultiviewCreateInfo',
}
_includes_ = {
    'VkAttachmentDescription',
    'VkSubpassDependency',
    'VkSubpassDescription',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateRenderPass',
}
_output_of_ = set()
