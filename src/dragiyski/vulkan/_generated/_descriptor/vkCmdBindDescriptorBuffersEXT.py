from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindDescriptorBuffersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'bufferCount', 'pBindingInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'bufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pBindingInfos': {
        'type': CPointerType(CComplexType('VkDescriptorBufferBindingInfoEXT')),
        'is_string': False,
        'length': [['bufferCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
