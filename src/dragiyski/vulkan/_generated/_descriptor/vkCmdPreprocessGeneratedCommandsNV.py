from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPreprocessGeneratedCommandsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pGeneratedCommandsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pGeneratedCommandsInfo': {
        'type': CPointerType(CComplexType('VkGeneratedCommandsInfoNV')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
