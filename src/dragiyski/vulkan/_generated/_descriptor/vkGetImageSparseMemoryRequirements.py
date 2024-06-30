from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetImageSparseMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pSparseMemoryRequirementCount', 'pSparseMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSparseMemoryRequirementCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pSparseMemoryRequirements': {
        'type': CPointerType(CComplexType('VkSparseImageMemoryRequirements')),
        'is_string': False,
        'length': [['pSparseMemoryRequirementCount']],
    },
}
_return_type_ = CVoidType()
