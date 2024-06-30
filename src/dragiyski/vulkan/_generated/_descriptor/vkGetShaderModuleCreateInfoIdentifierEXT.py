from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetShaderModuleCreateInfoIdentifierEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pIdentifier']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkShaderModuleCreateInfo')),
        'is_string': False,
    },
    'pIdentifier': {
        'type': CPointerType(CComplexType('VkShaderModuleIdentifierEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
