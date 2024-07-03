from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCuLaunchKernelNVX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pLaunchInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pLaunchInfo': {
        'type': CPointerType(CComplexType('VkCuLaunchInfoNVX')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
