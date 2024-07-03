from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBeginVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBeginInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pBeginInfo': {
        'type': CPointerType(CComplexType('VkVideoBeginCodingInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
