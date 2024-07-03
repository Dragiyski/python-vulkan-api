from ..._ctypes import *

category = 'callback'
_name_ = 'vkDeviceMemoryReportCallbackEXT'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['pCallbackData', 'pUserData']
_argument_info_ = {
    'pCallbackData': {
        'type': CPointerType(CComplexType('VkDeviceMemoryReportCallbackDataEXT')),
    },
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
}
_return_type_ = CVoidType()
