from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkWriteAccelerationStructuresPropertiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'accelerationStructureCount', 'pAccelerationStructures', 'queryType', 'dataSize', 'pData', 'stride']
_argument_info_ = {
    'device': {
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
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
    },
    'stride': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
