from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCopyImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCopyImageInfo': {
        'type': CPointerType(CComplexType('VkCopyImageInfo2')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
