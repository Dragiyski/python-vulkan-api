from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderingAttachmentLocationInfoKHR'
_member_list_ = ['sType', 'pNext', 'colorAttachmentCount', 'pColorAttachmentLocations']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_LOCATION_INFO_KHR',
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
    'pColorAttachmentLocations': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['colorAttachmentCount']],
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
_input_of_ = {
    'vkCmdSetRenderingAttachmentLocationsKHR',
}
_output_of_ = set()
