from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdEndVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pEndCodingInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pEndCodingInfo': {
        'type': CPointerType(CComplexType('VkVideoEndCodingInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
