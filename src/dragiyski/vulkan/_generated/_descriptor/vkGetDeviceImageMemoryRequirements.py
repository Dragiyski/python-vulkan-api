from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceImageMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkDeviceImageMemoryRequirements')),
        'is_string': False,
        'output': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements2')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
