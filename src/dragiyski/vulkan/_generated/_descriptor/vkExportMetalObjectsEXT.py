from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkExportMetalObjectsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pMetalObjectsInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMetalObjectsInfo': {
        'type': CPointerType(CComplexType('VkExportMetalObjectsInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
