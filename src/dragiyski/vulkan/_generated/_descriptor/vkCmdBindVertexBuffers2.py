from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindVertexBuffers2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstBinding', 'bindingCount', 'pBuffers', 'pOffsets', 'pSizes', 'pStrides']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstBinding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'bindingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['bindingCount']],
        'output': False,
    },
    'pOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['bindingCount']],
        'output': False,
    },
    'pSizes': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['bindingCount']],
        'output': False,
    },
    'pStrides': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['bindingCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
