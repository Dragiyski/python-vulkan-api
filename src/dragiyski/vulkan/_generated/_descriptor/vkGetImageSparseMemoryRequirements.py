from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetImageSparseMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pSparseMemoryRequirementCount', 'pSparseMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSparseMemoryRequirementCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pSparseMemoryRequirements': {
        'type': CPointerType(CComplexType('VkSparseImageMemoryRequirements')),
        'is_string': False,
        'length': [['pSparseMemoryRequirementCount']],
        'output': True,
    },
}
_return_type_ = CVoidType()
