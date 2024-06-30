from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkLayerProperties'
_member_list_ = ['layerName', 'specVersion', 'implementationVersion', 'description']
_member_info_ = {
    'layerName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'specVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'implementationVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkEnumerateDeviceLayerProperties',
    'vkEnumerateInstanceLayerProperties',
}
