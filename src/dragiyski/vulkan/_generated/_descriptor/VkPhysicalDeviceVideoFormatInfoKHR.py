from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVideoFormatInfoKHR'
_member_list_ = ['sType', 'pNext', 'imageUsage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_FORMAT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageUsage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoProfileListInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
}
_output_of_ = set()
