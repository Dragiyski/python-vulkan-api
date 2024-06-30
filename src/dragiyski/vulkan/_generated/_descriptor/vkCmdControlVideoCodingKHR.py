from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdControlVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCodingControlInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCodingControlInfo': {
        'type': CPointerType(CComplexType('VkVideoCodingControlInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
