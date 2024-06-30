from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindDescriptorBufferEmbeddedSamplers2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBindDescriptorBufferEmbeddedSamplersInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pBindDescriptorBufferEmbeddedSamplersInfo': {
        'type': CPointerType(CComplexType('VkBindDescriptorBufferEmbeddedSamplersInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
