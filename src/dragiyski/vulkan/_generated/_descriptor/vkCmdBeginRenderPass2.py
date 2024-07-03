from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBeginRenderPass2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRenderPassBegin', 'pSubpassBeginInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pRenderPassBegin': {
        'type': CPointerType(CComplexType('VkRenderPassBeginInfo')),
        'is_string': False,
        'output': False,
    },
    'pSubpassBeginInfo': {
        'type': CPointerType(CComplexType('VkSubpassBeginInfo')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
