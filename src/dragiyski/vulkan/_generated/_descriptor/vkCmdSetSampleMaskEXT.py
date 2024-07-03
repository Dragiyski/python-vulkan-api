from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetSampleMaskEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'samples', 'pSampleMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pSampleMask': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': False,
        'alt_length': '(samples + 31) / 32',
    },
}
_return_type_ = CVoidType()
