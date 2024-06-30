from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBeginConditionalRenderingEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pConditionalRenderingBegin']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pConditionalRenderingBegin': {
        'type': CPointerType(CComplexType('VkConditionalRenderingBeginInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
