from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkTraceRaysIndirectCommand2KHR'
_member_list_ = ['raygenShaderRecordAddress', 'raygenShaderRecordSize', 'missShaderBindingTableAddress', 'missShaderBindingTableSize', 'missShaderBindingTableStride', 'hitShaderBindingTableAddress', 'hitShaderBindingTableSize', 'hitShaderBindingTableStride', 'callableShaderBindingTableAddress', 'callableShaderBindingTableSize', 'callableShaderBindingTableStride', 'width', 'height', 'depth']
_member_info_ = {
    'raygenShaderRecordAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'raygenShaderRecordSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'missShaderBindingTableAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'missShaderBindingTableSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'missShaderBindingTableStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hitShaderBindingTableAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hitShaderBindingTableSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hitShaderBindingTableStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'callableShaderBindingTableAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'callableShaderBindingTableSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'callableShaderBindingTableStride': {
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
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
