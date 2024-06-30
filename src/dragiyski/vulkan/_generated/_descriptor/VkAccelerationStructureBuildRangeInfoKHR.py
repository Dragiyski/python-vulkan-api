from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureBuildRangeInfoKHR'
_member_list_ = ['primitiveCount', 'primitiveOffset', 'firstVertex', 'transformOffset']
_member_info_ = {
    'primitiveCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primitiveOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstVertex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transformOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkBuildAccelerationStructuresKHR',
    'vkCmdBuildAccelerationStructuresKHR',
}
_output_of_ = set()
