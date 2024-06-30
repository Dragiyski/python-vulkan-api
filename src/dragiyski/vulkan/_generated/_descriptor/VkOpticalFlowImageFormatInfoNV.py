from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOpticalFlowImageFormatInfoNV'
_member_list_ = ['sType', 'pNext', 'usage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowUsageFlagsNV',
        'enum': 'VkOpticalFlowUsageFlagsNV',
        'is_string': False,
    },
}
_extends_ = {
    'VkImageCreateInfo',
    'VkPhysicalDeviceImageFormatInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
}
_output_of_ = set()
