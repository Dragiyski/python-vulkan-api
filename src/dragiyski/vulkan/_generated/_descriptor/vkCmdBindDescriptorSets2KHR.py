from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindDescriptorSets2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBindDescriptorSetsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pBindDescriptorSetsInfo': {
        'type': CPointerType(CComplexType('VkBindDescriptorSetsInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
