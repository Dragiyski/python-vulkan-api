from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetFragmentShadingRateKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pFragmentSize', 'combinerOps']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pFragmentSize': {
        'type': CPointerType(CComplexType('VkExtent2D')),
        'is_string': False,
    },
    'combinerOps': {
        'type': CArrayType(CIntType('c_int'), 2),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
