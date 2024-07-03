from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBuildAccelerationStructureNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pInfo', 'instanceData', 'instanceOffset', 'update', 'dst', 'src', 'scratch', 'scratchOffset']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkAccelerationStructureInfoNV')),
        'is_string': False,
        'output': False,
    },
    'instanceData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'instanceOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'update': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'dst': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'src': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'scratch': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'scratchOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
