from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPreprocessGeneratedCommandsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pGeneratedCommandsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pGeneratedCommandsInfo': {
        'type': CPointerType(CComplexType('VkGeneratedCommandsInfoNV')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
