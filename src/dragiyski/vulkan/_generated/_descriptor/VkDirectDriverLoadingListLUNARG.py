from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDirectDriverLoadingListLUNARG'
_member_list_ = ['sType', 'pNext', 'mode', 'driverCount', 'pDrivers']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_LIST_LUNARG',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'type_name': 'VkDirectDriverLoadingModeLUNARG',
        'enum': 'VkDirectDriverLoadingModeLUNARG',
        'is_string': False,
    },
    'driverCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDrivers': {
        'type': CPointerType(CComplexType('VkDirectDriverLoadingInfoLUNARG')),
        'type_name': 'VkDirectDriverLoadingInfoLUNARG',
        'structure': 'VkDirectDriverLoadingInfoLUNARG',
        'length': [['driverCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkInstanceCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkDirectDriverLoadingInfoLUNARG',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
