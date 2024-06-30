from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceCapabilitiesFullScreenExclusiveEXT'
_member_list_ = ['sType', 'pNext', 'fullScreenExclusiveSupported']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_FULL_SCREEN_EXCLUSIVE_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fullScreenExclusiveSupported': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSurfaceCapabilities2KHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
