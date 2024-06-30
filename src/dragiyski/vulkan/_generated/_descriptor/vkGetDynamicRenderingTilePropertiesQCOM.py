from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDynamicRenderingTilePropertiesQCOM'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pRenderingInfo', 'pProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRenderingInfo': {
        'type': CPointerType(CComplexType('VkRenderingInfo')),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkTilePropertiesQCOM')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
