from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentSampleCountInfoAMD'
_member_list_ = ['sType', 'pNext', 'colorAttachmentCount', 'pColorAttachmentSamples', 'depthStencilAttachmentSamples']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_SAMPLE_COUNT_INFO_AMD',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'colorAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorAttachmentSamples': {
        'type': CPointerType(CIntType('c_uint32')),
        'type_name': 'VkSampleCountFlagBits',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'depthStencilAttachmentSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
}
_extends_ = {
    'VkCommandBufferInheritanceInfo',
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
