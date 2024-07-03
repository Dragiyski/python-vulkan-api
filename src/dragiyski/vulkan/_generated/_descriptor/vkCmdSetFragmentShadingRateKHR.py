from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetFragmentShadingRateKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pFragmentSize', 'combinerOps']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pFragmentSize': {
        'type': CPointerType(CComplexType('VkExtent2D')),
        'is_string': False,
        'output': False,
    },
    'combinerOps': {
        'type': CArrayType(CIntType('c_int'), 2),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
