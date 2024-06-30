from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindShadersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'stageCount', 'pStages', 'pShaders']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStages': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['stageCount']],
    },
    'pShaders': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['stageCount']],
    },
}
_return_type_ = CVoidType()
