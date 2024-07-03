from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdTraceRaysNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'raygenShaderBindingTableBuffer', 'raygenShaderBindingOffset', 'missShaderBindingTableBuffer', 'missShaderBindingOffset', 'missShaderBindingStride', 'hitShaderBindingTableBuffer', 'hitShaderBindingOffset', 'hitShaderBindingStride', 'callableShaderBindingTableBuffer', 'callableShaderBindingOffset', 'callableShaderBindingStride', 'width', 'height', 'depth']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'raygenShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'raygenShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'missShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'missShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'missShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'hitShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'hitShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'hitShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'callableShaderBindingTableBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'callableShaderBindingOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'callableShaderBindingStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'depth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
