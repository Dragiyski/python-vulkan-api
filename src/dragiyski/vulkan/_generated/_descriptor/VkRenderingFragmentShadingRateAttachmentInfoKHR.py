from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderingFragmentShadingRateAttachmentInfoKHR'
_member_list_ = ['sType', 'pNext', 'imageView', 'imageLayout', 'shadingRateAttachmentTexelSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'shadingRateAttachmentTexelSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderingInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
