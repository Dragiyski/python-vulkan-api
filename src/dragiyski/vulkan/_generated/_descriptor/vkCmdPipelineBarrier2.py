from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPipelineBarrier2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pDependencyInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDependencyInfo': {
        'type': CPointerType(CComplexType('VkDependencyInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
