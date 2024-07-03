from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDynamicRenderingTilePropertiesQCOM'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pRenderingInfo', 'pProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pRenderingInfo': {
        'type': CPointerType(CComplexType('VkRenderingInfo')),
        'is_string': False,
        'output': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkTilePropertiesQCOM')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
