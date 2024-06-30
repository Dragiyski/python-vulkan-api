from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceImageSparseMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo', 'pSparseMemoryRequirementCount', 'pSparseMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkDeviceImageMemoryRequirements')),
        'is_string': False,
    },
    'pSparseMemoryRequirementCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pSparseMemoryRequirements': {
        'type': CPointerType(CComplexType('VkSparseImageMemoryRequirements2')),
        'is_string': False,
        'length': [['pSparseMemoryRequirementCount']],
    },
}
_return_type_ = CVoidType()
