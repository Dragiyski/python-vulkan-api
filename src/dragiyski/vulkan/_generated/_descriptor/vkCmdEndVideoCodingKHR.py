from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdEndVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pEndCodingInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pEndCodingInfo': {
        'type': CPointerType(CComplexType('VkVideoEndCodingInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
