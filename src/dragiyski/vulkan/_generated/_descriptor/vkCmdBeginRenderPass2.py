from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBeginRenderPass2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRenderPassBegin', 'pSubpassBeginInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRenderPassBegin': {
        'type': CPointerType(CComplexType('VkRenderPassBeginInfo')),
        'is_string': False,
    },
    'pSubpassBeginInfo': {
        'type': CPointerType(CComplexType('VkSubpassBeginInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
