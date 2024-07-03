from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkUpdateDescriptorSetWithTemplate'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorSet', 'descriptorUpdateTemplate', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorSet': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorUpdateTemplate': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
