from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeometryDataNV'
_member_list_ = ['triangles', 'aabbs']
_member_info_ = {
    'triangles': {
        'type': CComplexType('VkGeometryTrianglesNV'),
        'type_name': 'VkGeometryTrianglesNV',
        'structure': 'VkGeometryTrianglesNV',
        'is_string': False,
    },
    'aabbs': {
        'type': CComplexType('VkGeometryAABBNV'),
        'type_name': 'VkGeometryAABBNV',
        'structure': 'VkGeometryAABBNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkGeometryAABBNV',
    'VkGeometryTrianglesNV',
}
_included_in_ = {
    'VkGeometryNV',
}
_input_of_ = set()
_output_of_ = set()
