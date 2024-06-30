from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapUsageEXT'
_member_list_ = ['count', 'subdivisionLevel', 'format']
_member_info_ = {
    'count': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subdivisionLevel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkAccelerationStructureTrianglesDisplacementMicromapNV',
    'VkAccelerationStructureTrianglesOpacityMicromapEXT',
    'VkMicromapBuildInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
