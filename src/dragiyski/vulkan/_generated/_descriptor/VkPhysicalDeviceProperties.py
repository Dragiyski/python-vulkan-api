from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceProperties'
_member_list_ = ['apiVersion', 'driverVersion', 'vendorID', 'deviceID', 'deviceType', 'deviceName', 'pipelineCacheUUID', 'limits', 'sparseProperties']
_member_info_ = {
    'apiVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'driverVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vendorID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceType': {
        'type': CIntType('c_int'),
        'type_name': 'VkPhysicalDeviceType',
        'enum': 'VkPhysicalDeviceType',
        'is_string': False,
    },
    'deviceName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'pipelineCacheUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'limits': {
        'type': CComplexType('VkPhysicalDeviceLimits'),
        'type_name': 'VkPhysicalDeviceLimits',
        'structure': 'VkPhysicalDeviceLimits',
        'is_string': False,
    },
    'sparseProperties': {
        'type': CComplexType('VkPhysicalDeviceSparseProperties'),
        'type_name': 'VkPhysicalDeviceSparseProperties',
        'structure': 'VkPhysicalDeviceSparseProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkPhysicalDeviceLimits',
    'VkPhysicalDeviceSparseProperties',
}
_included_in_ = {
    'VkPhysicalDeviceProperties2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceProperties',
}
