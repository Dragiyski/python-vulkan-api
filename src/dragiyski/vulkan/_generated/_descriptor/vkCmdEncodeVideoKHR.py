from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdEncodeVideoKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pEncodeInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pEncodeInfo': {
        'type': CPointerType(CComplexType('VkVideoEncodeInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
