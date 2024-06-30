from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDriverProperties'
_member_list_ = ['sType', 'pNext', 'driverID', 'driverName', 'driverInfo', 'conformanceVersion']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'driverID': {
        'type': CIntType('c_int'),
        'type_name': 'VkDriverId',
        'enum': 'VkDriverId',
        'is_string': False,
    },
    'driverName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'driverInfo': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'conformanceVersion': {
        'type': CComplexType('VkConformanceVersion'),
        'type_name': 'VkConformanceVersion',
        'structure': 'VkConformanceVersion',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkConformanceVersion',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
