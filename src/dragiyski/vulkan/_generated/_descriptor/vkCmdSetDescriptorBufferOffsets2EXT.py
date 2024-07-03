from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetDescriptorBufferOffsets2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSetDescriptorBufferOffsetsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSetDescriptorBufferOffsetsInfo': {
        'type': CPointerType(CComplexType('VkSetDescriptorBufferOffsetsInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
