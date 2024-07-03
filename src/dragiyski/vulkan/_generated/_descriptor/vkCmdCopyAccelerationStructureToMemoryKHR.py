from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyAccelerationStructureToMemoryKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyAccelerationStructureToMemoryInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
