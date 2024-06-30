from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdWriteAccelerationStructuresPropertiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'accelerationStructureCount', 'pAccelerationStructures', 'queryType', 'queryPool', 'firstQuery']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'accelerationStructureCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAccelerationStructures': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['accelerationStructureCount']],
    },
    'queryType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
