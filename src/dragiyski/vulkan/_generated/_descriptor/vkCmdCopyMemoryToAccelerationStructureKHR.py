from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyMemoryToAccelerationStructureKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyMemoryToAccelerationStructureInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
