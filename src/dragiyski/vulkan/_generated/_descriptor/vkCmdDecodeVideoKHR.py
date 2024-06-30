from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDecodeVideoKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pDecodeInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDecodeInfo': {
        'type': CPointerType(CComplexType('VkVideoDecodeInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
