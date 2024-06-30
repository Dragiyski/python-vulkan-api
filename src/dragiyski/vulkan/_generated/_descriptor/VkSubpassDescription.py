from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassDescription'
_member_list_ = ['flags', 'pipelineBindPoint', 'inputAttachmentCount', 'pInputAttachments', 'colorAttachmentCount', 'pColorAttachments', 'pResolveAttachments', 'pDepthStencilAttachment', 'preserveAttachmentCount', 'pPreserveAttachments']
_member_info_ = {
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSubpassDescriptionFlags',
        'enum': 'VkSubpassDescriptionFlags',
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'inputAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pInputAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference')),
        'type_name': 'VkAttachmentReference',
        'structure': 'VkAttachmentReference',
        'length': [['inputAttachmentCount']],
        'is_string': False,
    },
    'colorAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference')),
        'type_name': 'VkAttachmentReference',
        'structure': 'VkAttachmentReference',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'pResolveAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference')),
        'type_name': 'VkAttachmentReference',
        'structure': 'VkAttachmentReference',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'pDepthStencilAttachment': {
        'type': CPointerType(CComplexType('VkAttachmentReference')),
        'type_name': 'VkAttachmentReference',
        'structure': 'VkAttachmentReference',
        'is_string': False,
    },
    'preserveAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPreserveAttachments': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['preserveAttachmentCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkAttachmentReference',
}
_included_in_ = {
    'VkRenderPassCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
