from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceGroupPeerMemoryFeatures'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'heapIndex', 'localDeviceIndex', 'remoteDeviceIndex', 'pPeerMemoryFeatures']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'heapIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'localDeviceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'remoteDeviceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pPeerMemoryFeatures': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
