from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdTraceRaysNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'raygenShaderBindingTableBuffer', 'raygenShaderBindingOffset', 'missShaderBindingTableBuffer', 'missShaderBindingOffset', 'missShaderBindingStride', 'hitShaderBindingTableBuffer', 'hitShaderBindingOffset', 'hitShaderBindingStride', 'callableShaderBindingTableBuffer', 'callableShaderBindingOffset', 'callableShaderBindingStride', 'width', 'height', 'depth']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'raygenShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'raygenShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'missShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'missShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'missShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hitShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'hitShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hitShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'callableShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'callableShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'callableShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
