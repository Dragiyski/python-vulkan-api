from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRenderingCreateInfo'
_member_list_ = ['sType', 'pNext', 'viewMask', 'colorAttachmentCount', 'pColorAttachmentFormats', 'depthAttachmentFormat', 'stencilAttachmentFormat']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RENDERING_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'colorAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorAttachmentFormats': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'depthAttachmentFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'stencilAttachmentFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
}
_extends_ = {
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
