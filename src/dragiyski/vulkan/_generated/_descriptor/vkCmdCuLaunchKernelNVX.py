from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCuLaunchKernelNVX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pLaunchInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pLaunchInfo': {
        'type': CPointerType(CComplexType('VkCuLaunchInfoNVX')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
