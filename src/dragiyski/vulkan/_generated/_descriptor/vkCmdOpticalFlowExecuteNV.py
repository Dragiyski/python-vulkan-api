from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdOpticalFlowExecuteNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'session', 'pExecuteInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'session': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pExecuteInfo': {
        'type': CPointerType(CComplexType('VkOpticalFlowExecuteInfoNV')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
