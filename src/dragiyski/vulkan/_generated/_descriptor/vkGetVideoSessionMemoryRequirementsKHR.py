from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetVideoSessionMemoryRequirementsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'videoSession', 'pMemoryRequirementsCount', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'videoSession': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pMemoryRequirementsCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkVideoSessionMemoryRequirementsKHR')),
        'is_string': False,
        'length': [['pMemoryRequirementsCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = set()
