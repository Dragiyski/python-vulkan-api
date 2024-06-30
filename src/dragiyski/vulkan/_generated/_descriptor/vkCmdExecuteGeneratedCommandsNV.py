from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdExecuteGeneratedCommandsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'isPreprocessed', 'pGeneratedCommandsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'isPreprocessed': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pGeneratedCommandsInfo': {
        'type': CPointerType(CComplexType('VkGeneratedCommandsInfoNV')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
