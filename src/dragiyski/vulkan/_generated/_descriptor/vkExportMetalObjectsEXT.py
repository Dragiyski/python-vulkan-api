from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkExportMetalObjectsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pMetalObjectsInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pMetalObjectsInfo': {
        'type': CPointerType(CComplexType('VkExportMetalObjectsInfoEXT')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
