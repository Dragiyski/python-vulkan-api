from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferInheritanceRenderingInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'viewMask', 'colorAttachmentCount', 'pColorAttachmentFormats', 'depthAttachmentFormat', 'stencilAttachmentFormat', 'rasterizationSamples']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDERING_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkRenderingFlags',
        'enum': 'VkRenderingFlags',
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
    'rasterizationSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
}
_extends_ = {
    'VkCommandBufferInheritanceInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
