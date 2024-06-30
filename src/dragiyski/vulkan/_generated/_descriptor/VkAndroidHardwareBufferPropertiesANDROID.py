from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAndroidHardwareBufferPropertiesANDROID'
_member_list_ = ['sType', 'pNext', 'allocationSize', 'memoryTypeBits']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'allocationSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'memoryTypeBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkAndroidHardwareBufferFormatProperties2ANDROID',
    'VkAndroidHardwareBufferFormatPropertiesANDROID',
    'VkAndroidHardwareBufferFormatResolvePropertiesANDROID',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetAndroidHardwareBufferPropertiesANDROID',
}
