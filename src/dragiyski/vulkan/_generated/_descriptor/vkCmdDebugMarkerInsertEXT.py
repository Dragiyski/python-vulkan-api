from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDebugMarkerInsertEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pMarkerInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pMarkerInfo': {
        'type': CPointerType(CComplexType('VkDebugMarkerMarkerInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
