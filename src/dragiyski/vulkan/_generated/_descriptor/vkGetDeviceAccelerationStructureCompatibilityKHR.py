from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceAccelerationStructureCompatibilityKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pVersionInfo', 'pCompatibility']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pVersionInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureVersionInfoKHR')),
        'is_string': False,
    },
    'pCompatibility': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
