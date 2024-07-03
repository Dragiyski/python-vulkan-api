from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyMicromapEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyMicromapInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
