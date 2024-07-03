from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkFreeDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorPool', 'descriptorSetCount', 'pDescriptorSets']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDescriptorSets': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['descriptorSetCount']],
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
