from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkReleaseSwapchainImagesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pReleaseInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pReleaseInfo': {
        'type': CPointerType(CComplexType('VkReleaseSwapchainImagesInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_SURFACE_LOST_KHR'}
