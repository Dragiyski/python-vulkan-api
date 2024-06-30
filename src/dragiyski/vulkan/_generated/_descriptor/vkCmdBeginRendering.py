from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBeginRendering'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pRenderingInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRenderingInfo': {
        'type': CPointerType(CComplexType('VkRenderingInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
