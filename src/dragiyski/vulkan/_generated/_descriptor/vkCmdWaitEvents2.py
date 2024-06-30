from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdWaitEvents2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'eventCount', 'pEvents', 'pDependencyInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'eventCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pEvents': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['eventCount']],
    },
    'pDependencyInfos': {
        'type': CPointerType(CComplexType('VkDependencyInfo')),
        'is_string': False,
        'length': [['eventCount']],
    },
}
_return_type_ = CVoidType()
