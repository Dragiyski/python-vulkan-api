from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDescriptorBufferOffsets2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSetDescriptorBufferOffsetsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSetDescriptorBufferOffsetsInfo': {
        'type': CPointerType(CComplexType('VkSetDescriptorBufferOffsetsInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
