from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyMicromapToMemoryEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyMicromapToMemoryInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
