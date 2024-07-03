from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindDescriptorBufferEmbeddedSamplers2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBindDescriptorBufferEmbeddedSamplersInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pBindDescriptorBufferEmbeddedSamplersInfo': {
        'type': CPointerType(CComplexType('VkBindDescriptorBufferEmbeddedSamplersInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
