from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdEncodeVideoKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pEncodeInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pEncodeInfo': {
        'type': CPointerType(CComplexType('VkVideoEncodeInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
