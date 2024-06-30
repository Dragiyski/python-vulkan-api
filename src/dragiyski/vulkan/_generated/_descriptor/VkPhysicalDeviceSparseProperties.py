from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceSparseProperties'
_member_list_ = ['residencyStandard2DBlockShape', 'residencyStandard2DMultisampleBlockShape', 'residencyStandard3DBlockShape', 'residencyAlignedMipSize', 'residencyNonResidentStrict']
_member_info_ = {
    'residencyStandard2DBlockShape': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'residencyStandard2DMultisampleBlockShape': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'residencyStandard3DBlockShape': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'residencyAlignedMipSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'residencyNonResidentStrict': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPhysicalDeviceProperties',
}
_input_of_ = set()
_output_of_ = set()
