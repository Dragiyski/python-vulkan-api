from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetSampleLocationsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSampleLocationsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSampleLocationsInfo': {
        'type': CPointerType(CComplexType('VkSampleLocationsInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
