from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDescriptorSetHostMappingVALVE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorSet', 'ppData']
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
    'ppData': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
