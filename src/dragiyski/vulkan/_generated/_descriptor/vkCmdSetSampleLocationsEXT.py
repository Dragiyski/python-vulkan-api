from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetSampleLocationsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pSampleLocationsInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSampleLocationsInfo': {
        'type': CPointerType(CComplexType('VkSampleLocationsInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
