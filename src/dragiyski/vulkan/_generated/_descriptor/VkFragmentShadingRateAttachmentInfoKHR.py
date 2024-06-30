from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFragmentShadingRateAttachmentInfoKHR'
_member_list_ = ['sType', 'pNext', 'pFragmentShadingRateAttachment', 'shadingRateAttachmentTexelSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pFragmentShadingRateAttachment': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
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
    'VkSubpassDescription2',
}
_extended_by_ = set()
_includes_ = {
    'VkAttachmentReference2',
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
