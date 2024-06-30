from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBlitImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pBlitImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pBlitImageInfo': {
        'type': CPointerType(CComplexType('VkBlitImageInfo2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
