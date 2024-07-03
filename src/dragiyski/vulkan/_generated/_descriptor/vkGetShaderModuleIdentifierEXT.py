from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetShaderModuleIdentifierEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'shaderModule', 'pIdentifier']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'shaderModule': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pIdentifier': {
        'type': CPointerType(CComplexType('VkShaderModuleIdentifierEXT')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
