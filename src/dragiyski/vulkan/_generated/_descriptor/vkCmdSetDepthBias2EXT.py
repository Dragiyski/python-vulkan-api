from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetDepthBias2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pDepthBiasInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pDepthBiasInfo': {
        'type': CPointerType(CComplexType('VkDepthBiasInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
