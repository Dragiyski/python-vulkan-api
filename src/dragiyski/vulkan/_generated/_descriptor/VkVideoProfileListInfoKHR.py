from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoProfileListInfoKHR'
_member_list_ = ['sType', 'pNext', 'profileCount', 'pProfiles']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_LIST_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'profileCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pProfiles': {
        'type': CPointerType(CComplexType('VkVideoProfileInfoKHR')),
        'type_name': 'VkVideoProfileInfoKHR',
        'structure': 'VkVideoProfileInfoKHR',
        'length': [['profileCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBufferCreateInfo',
    'VkImageCreateInfo',
    'VkPhysicalDeviceImageFormatInfo2',
    'VkPhysicalDeviceVideoFormatInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoProfileInfoKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
