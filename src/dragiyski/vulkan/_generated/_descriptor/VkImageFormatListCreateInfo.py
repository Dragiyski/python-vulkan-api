from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageFormatListCreateInfo'
_member_list_ = ['sType', 'pNext', 'viewFormatCount', 'pViewFormats']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewFormatCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewFormats': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'length': [['viewFormatCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkImageCreateInfo',
    'VkPhysicalDeviceImageFormatInfo2',
    'VkSwapchainCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
