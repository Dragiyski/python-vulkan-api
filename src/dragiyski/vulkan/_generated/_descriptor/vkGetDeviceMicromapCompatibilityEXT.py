from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceMicromapCompatibilityEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pVersionInfo', 'pCompatibility']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pVersionInfo': {
        'type': CPointerType(CComplexType('VkMicromapVersionInfoEXT')),
        'is_string': False,
        'output': False,
    },
    'pCompatibility': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
