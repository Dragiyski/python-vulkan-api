from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdWaitEvents2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'eventCount', 'pEvents', 'pDependencyInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'eventCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pEvents': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['eventCount']],
        'output': False,
    },
    'pDependencyInfos': {
        'type': CPointerType(CComplexType('VkDependencyInfo')),
        'is_string': False,
        'length': [['eventCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
