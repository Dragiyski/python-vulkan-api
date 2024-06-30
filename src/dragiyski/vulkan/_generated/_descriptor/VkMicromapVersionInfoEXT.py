from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapVersionInfoEXT'
_member_list_ = ['sType', 'pNext', 'pVersionData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MICROMAP_VERSION_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pVersionData': {
        'type': CPointerType(CIntType('c_uint8')),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetDeviceMicromapCompatibilityEXT',
}
_output_of_ = set()
