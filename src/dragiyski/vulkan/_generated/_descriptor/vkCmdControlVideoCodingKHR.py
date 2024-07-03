from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdControlVideoCodingKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCodingControlInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCodingControlInfo': {
        'type': CPointerType(CComplexType('VkVideoCodingControlInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
