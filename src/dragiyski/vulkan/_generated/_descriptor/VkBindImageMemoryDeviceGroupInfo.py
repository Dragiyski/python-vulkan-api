from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindImageMemoryDeviceGroupInfo'
_member_list_ = ['sType', 'pNext', 'deviceIndexCount', 'pDeviceIndices', 'splitInstanceBindRegionCount', 'pSplitInstanceBindRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDeviceIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['deviceIndexCount']],
        'is_string': False,
    },
    'splitInstanceBindRegionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSplitInstanceBindRegions': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['splitInstanceBindRegionCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBindImageMemoryInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
