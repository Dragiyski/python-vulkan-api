from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceImageViewImageFormatInfoEXT'
_member_list_ = ['sType', 'pNext', 'imageViewType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageViewType': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageViewType',
        'enum': 'VkImageViewType',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceImageFormatInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
