from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindTransformFeedbackBuffersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstBinding', 'bindingCount', 'pBuffers', 'pOffsets', 'pSizes']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstBinding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bindingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['bindingCount']],
    },
    'pOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['bindingCount']],
    },
    'pSizes': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['bindingCount']],
    },
}
_return_type_ = CVoidType()
