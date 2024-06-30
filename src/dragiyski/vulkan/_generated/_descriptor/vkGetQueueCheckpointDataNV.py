from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetQueueCheckpointDataNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'pCheckpointDataCount', 'pCheckpointData']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCheckpointDataCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pCheckpointData': {
        'type': CPointerType(CComplexType('VkCheckpointDataNV')),
        'is_string': False,
        'length': [['pCheckpointDataCount']],
    },
}
_return_type_ = CVoidType()
