from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAndroidHardwareBufferUsageANDROID'
_member_list_ = ['sType', 'pNext', 'androidHardwareBufferUsage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'androidHardwareBufferUsage': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkImageFormatProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
