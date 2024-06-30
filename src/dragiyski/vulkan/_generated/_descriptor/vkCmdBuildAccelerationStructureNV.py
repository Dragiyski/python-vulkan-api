from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBuildAccelerationStructureNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo', 'instanceData', 'instanceOffset', 'update', 'dst', 'src', 'scratch', 'scratchOffset']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureInfoNV')),
        'is_string': False,
    },
    'instanceData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'instanceOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'update': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dst': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'src': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'scratch': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'scratchOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
