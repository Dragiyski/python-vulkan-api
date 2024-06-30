from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBeginVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBeginInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pBeginInfo': {
        'type': CPointerType(CComplexType('VkVideoBeginCodingInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
