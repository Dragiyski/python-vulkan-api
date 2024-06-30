from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryGetAndroidHardwareBufferInfoANDROID'
_member_list_ = ['sType', 'pNext', 'memory']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_GET_ANDROID_HARDWARE_BUFFER_INFO_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetMemoryAndroidHardwareBufferANDROID',
}
_output_of_ = set()
