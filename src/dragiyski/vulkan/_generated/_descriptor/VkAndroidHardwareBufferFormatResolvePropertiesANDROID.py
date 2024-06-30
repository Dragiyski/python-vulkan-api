from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAndroidHardwareBufferFormatResolvePropertiesANDROID'
_member_list_ = ['sType', 'pNext', 'colorAttachmentFormat']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_RESOLVE_PROPERTIES_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'colorAttachmentFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
}
_extends_ = {
    'VkAndroidHardwareBufferPropertiesANDROID',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
