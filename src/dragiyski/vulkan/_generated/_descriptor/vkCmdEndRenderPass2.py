from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdEndRenderPass2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSubpassEndInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSubpassEndInfo': {
        'type': CPointerType(CComplexType('VkSubpassEndInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
