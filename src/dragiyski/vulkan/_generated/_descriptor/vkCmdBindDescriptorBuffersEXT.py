from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindDescriptorBuffersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'bufferCount', 'pBindingInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBindingInfos': {
        'type': CPointerType(CComplexType('VkDescriptorBufferBindingInfoEXT')),
        'is_string': False,
        'length': [['bufferCount']],
    },
}
_return_type_ = CVoidType()
