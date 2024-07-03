from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetFramebufferTilePropertiesQCOM'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'framebuffer', 'pPropertiesCount', 'pProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'framebuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPropertiesCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkTilePropertiesQCOM')),
        'is_string': False,
        'length': [['pPropertiesCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = set()
