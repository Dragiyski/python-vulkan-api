from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCacheSafetyCriticalIndexEntry'
_member_list_ = ['pipelineIdentifier', 'pipelineMemorySize', 'jsonSize', 'jsonOffset', 'stageIndexCount', 'stageIndexStride', 'stageIndexOffset']
_member_info_ = {
    'pipelineIdentifier': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'pipelineMemorySize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'jsonSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'jsonOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'stageIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stageIndexStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stageIndexOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
