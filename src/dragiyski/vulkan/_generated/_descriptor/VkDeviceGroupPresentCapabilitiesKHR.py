from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceGroupPresentCapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'presentMask', 'modes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'presentMask': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'modes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDeviceGroupPresentModeFlagsKHR',
        'enum': 'VkDeviceGroupPresentModeFlagsKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDeviceGroupPresentCapabilitiesKHR',
}
