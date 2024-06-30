from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDescriptorSetHostMappingVALVE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorSet', 'ppData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorSet': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'ppData': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
