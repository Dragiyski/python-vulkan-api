from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceIDProperties'
_member_list_ = ['sType', 'pNext', 'deviceUUID', 'driverUUID', 'deviceLUID', 'deviceNodeMask', 'deviceLUIDValid']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'driverUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'deviceLUID': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'deviceNodeMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceLUIDValid': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
