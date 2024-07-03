from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPushDescriptorSetKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'layout', 'set', 'descriptorWriteCount', 'pDescriptorWrites']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'set': {
        'type': CIntType('c_uint32'),
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
}
_return_type_ = CVoidType()
