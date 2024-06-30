from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUpdateDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorWriteCount', 'pDescriptorWrites', 'descriptorCopyCount', 'pDescriptorCopies']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorWriteCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorWrites': {
        'type': CPointerType(CComplexType('VkWriteDescriptorSet')),
        'is_string': False,
        'length': [['descriptorWriteCount']],
    },
    'descriptorCopyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorCopies': {
        'type': CPointerType(CComplexType('VkCopyDescriptorSet')),
        'is_string': False,
        'length': [['descriptorCopyCount']],
    },
}
_return_type_ = CVoidType()
