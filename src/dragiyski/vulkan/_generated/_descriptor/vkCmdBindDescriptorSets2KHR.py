from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindDescriptorSets2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBindDescriptorSetsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pBindDescriptorSetsInfo': {
        'type': CPointerType(CComplexType('VkBindDescriptorSetsInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
