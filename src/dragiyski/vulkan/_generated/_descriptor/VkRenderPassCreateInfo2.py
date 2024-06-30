from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassCreateInfo2'
_member_list_ = ['sType', 'pNext', 'flags', 'attachmentCount', 'pAttachments', 'subpassCount', 'pSubpasses', 'dependencyCount', 'pDependencies', 'correlatedViewMaskCount', 'pCorrelatedViewMasks']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2',
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
        'type': CPointerType(CComplexType('VkAttachmentDescription2')),
        'type_name': 'VkAttachmentDescription2',
        'structure': 'VkAttachmentDescription2',
        'length': [['attachmentCount']],
        'is_string': False,
    },
    'subpassCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSubpasses': {
        'type': CPointerType(CComplexType('VkSubpassDescription2')),
        'type_name': 'VkSubpassDescription2',
        'structure': 'VkSubpassDescription2',
        'length': [['subpassCount']],
        'is_string': False,
    },
    'dependencyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDependencies': {
        'type': CPointerType(CComplexType('VkSubpassDependency2')),
        'type_name': 'VkSubpassDependency2',
        'structure': 'VkSubpassDependency2',
        'length': [['dependencyCount']],
        'is_string': False,
    },
    'correlatedViewMaskCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCorrelatedViewMasks': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['correlatedViewMaskCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkRenderPassCreationControlEXT',
    'VkRenderPassCreationFeedbackCreateInfoEXT',
    'VkRenderPassFragmentDensityMapCreateInfoEXT',
}
_includes_ = {
    'VkAttachmentDescription2',
    'VkSubpassDependency2',
    'VkSubpassDescription2',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateRenderPass2',
}
_output_of_ = set()
