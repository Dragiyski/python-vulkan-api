from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeometryNV'
_member_list_ = ['sType', 'pNext', 'geometryType', 'geometry', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GEOMETRY_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'geometryType': {
        'type': CIntType('c_int'),
        'type_name': 'VkGeometryTypeKHR',
        'enum': 'VkGeometryTypeKHR',
        'is_string': False,
    },
    'geometry': {
        'type': CComplexType('VkGeometryDataNV'),
        'type_name': 'VkGeometryDataNV',
        'structure': 'VkGeometryDataNV',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkGeometryFlagsKHR',
        'enum': 'VkGeometryFlagsKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkGeometryDataNV',
}
_included_in_ = {
    'VkAccelerationStructureInfoNV',
}
_input_of_ = set()
_output_of_ = set()
