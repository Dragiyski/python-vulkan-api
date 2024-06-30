from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUpdateDescriptorSetWithTemplate'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorSet', 'descriptorUpdateTemplate', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorSet': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorUpdateTemplate': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
