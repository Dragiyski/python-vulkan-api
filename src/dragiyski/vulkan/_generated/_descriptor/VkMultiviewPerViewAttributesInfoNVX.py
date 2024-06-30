from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMultiviewPerViewAttributesInfoNVX'
_member_list_ = ['sType', 'pNext', 'perViewAttributes', 'perViewAttributesPositionXOnly']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_ATTRIBUTES_INFO_NVX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'perViewAttributes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'perViewAttributesPositionXOnly': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkCommandBufferInheritanceInfo',
    'VkGraphicsPipelineCreateInfo',
    'VkRenderingInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
