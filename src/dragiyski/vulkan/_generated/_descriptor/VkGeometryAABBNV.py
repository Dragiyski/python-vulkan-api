from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeometryAABBNV'
_member_list_ = ['sType', 'pNext', 'aabbData', 'numAABBs', 'stride', 'offset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GEOMETRY_AABB_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'aabbData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'numAABBs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkGeometryDataNV',
}
_input_of_ = set()
_output_of_ = set()
