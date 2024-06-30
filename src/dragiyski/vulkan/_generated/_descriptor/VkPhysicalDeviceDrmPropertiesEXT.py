from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDrmPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'hasPrimary', 'hasRender', 'primaryMajor', 'primaryMinor', 'renderMajor', 'renderMinor']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRM_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'hasPrimary': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'hasRender': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primaryMajor': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
    'primaryMinor': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
    'renderMajor': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
    'renderMinor': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
