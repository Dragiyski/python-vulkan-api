from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyMemoryToMicromapEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyMemoryToMicromapInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
