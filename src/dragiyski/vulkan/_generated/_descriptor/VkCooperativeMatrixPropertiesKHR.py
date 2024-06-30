from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCooperativeMatrixPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'MSize', 'NSize', 'KSize', 'AType', 'BType', 'CType', 'ResultType', 'saturatingAccumulation', 'scope']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'MSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'NSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'KSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'AType': {
        'type': CIntType('c_int'),
        'type_name': 'VkComponentTypeKHR',
        'enum': 'VkComponentTypeKHR',
        'is_string': False,
    },
    'BType': {
        'type': CIntType('c_int'),
        'type_name': 'VkComponentTypeKHR',
        'enum': 'VkComponentTypeKHR',
        'is_string': False,
    },
    'CType': {
        'type': CIntType('c_int'),
        'type_name': 'VkComponentTypeKHR',
        'enum': 'VkComponentTypeKHR',
        'is_string': False,
    },
    'ResultType': {
        'type': CIntType('c_int'),
        'type_name': 'VkComponentTypeKHR',
        'enum': 'VkComponentTypeKHR',
        'is_string': False,
    },
    'saturatingAccumulation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'scope': {
        'type': CIntType('c_int'),
        'type_name': 'VkScopeKHR',
        'enum': 'VkScopeKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceCooperativeMatrixPropertiesKHR',
}
