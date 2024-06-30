from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindAccelerationStructureMemoryInfoNV'
_member_list_ = ['sType', 'pNext', 'accelerationStructure', 'memory', 'memoryOffset', 'deviceIndexCount', 'pDeviceIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_ACCELERATION_STRUCTURE_MEMORY_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'accelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryOffset': {
        'type': CIntType('c_uint64'),
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkBindAccelerationStructureMemoryNV',
}
_output_of_ = set()
