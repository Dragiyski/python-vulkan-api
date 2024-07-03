from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetStencilWriteMask'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'faceMask', 'writeMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'faceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'writeMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
