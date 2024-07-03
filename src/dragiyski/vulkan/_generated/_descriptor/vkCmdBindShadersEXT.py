from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindShadersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'stageCount', 'pStages', 'pShaders']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'stageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pStages': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['stageCount']],
        'output': False,
    },
    'pShaders': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['stageCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
