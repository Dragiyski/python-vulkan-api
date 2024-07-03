from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkUpdateDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorWriteCount', 'pDescriptorWrites', 'descriptorCopyCount', 'pDescriptorCopies']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorWriteCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDescriptorWrites': {
        'type': CPointerType(CComplexType('VkWriteDescriptorSet')),
        'is_string': False,
        'length': [['descriptorWriteCount']],
        'output': False,
    },
    'descriptorCopyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDescriptorCopies': {
        'type': CPointerType(CComplexType('VkCopyDescriptorSet')),
        'is_string': False,
        'length': [['descriptorCopyCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
