from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetImageMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
