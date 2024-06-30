from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDepthBias2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pDepthBiasInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDepthBiasInfo': {
        'type': CPointerType(CComplexType('VkDepthBiasInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
