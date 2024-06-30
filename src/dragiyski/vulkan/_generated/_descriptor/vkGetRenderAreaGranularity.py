from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRenderAreaGranularity'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'renderPass', 'pGranularity']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'renderPass': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pGranularity': {
        'type': CPointerType(CComplexType('VkExtent2D')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
