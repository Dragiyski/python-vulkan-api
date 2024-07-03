from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdWriteAccelerationStructuresPropertiesNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'accelerationStructureCount', 'pAccelerationStructures', 'queryType', 'queryPool', 'firstQuery']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'accelerationStructureCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pAccelerationStructures': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['accelerationStructureCount']],
        'output': False,
    },
    'queryType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
