from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalFormatANDROID'
_member_list_ = ['sType', 'pNext', 'externalFormat']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'externalFormat': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkAttachmentDescription2',
    'VkCommandBufferInheritanceInfo',
    'VkGraphicsPipelineCreateInfo',
    'VkImageCreateInfo',
    'VkSamplerYcbcrConversionCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
