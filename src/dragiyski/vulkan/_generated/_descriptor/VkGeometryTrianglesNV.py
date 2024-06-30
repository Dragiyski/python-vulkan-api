from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeometryTrianglesNV'
_member_list_ = ['sType', 'pNext', 'vertexData', 'vertexOffset', 'vertexCount', 'vertexStride', 'vertexFormat', 'indexData', 'indexOffset', 'indexCount', 'indexType', 'transformData', 'transformOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'vertexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'vertexFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'indexData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'indexOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'indexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'indexType': {
        'type': CIntType('c_int'),
        'type_name': 'VkIndexType',
        'enum': 'VkIndexType',
        'is_string': False,
    },
    'transformData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'transformOffset': {
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
