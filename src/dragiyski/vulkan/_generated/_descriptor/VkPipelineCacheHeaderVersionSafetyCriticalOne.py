from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCacheHeaderVersionSafetyCriticalOne'
_member_list_ = ['headerVersionOne', 'validationVersion', 'implementationData', 'pipelineIndexCount', 'pipelineIndexStride', 'pipelineIndexOffset']
_member_info_ = {
    'headerVersionOne': {
        'type': CComplexType('VkPipelineCacheHeaderVersionOne'),
        'type_name': 'VkPipelineCacheHeaderVersionOne',
        'structure': 'VkPipelineCacheHeaderVersionOne',
        'is_string': False,
    },
    'validationVersion': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineCacheValidationVersion',
        'enum': 'VkPipelineCacheValidationVersion',
        'is_string': False,
    },
    'implementationData': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineIndexStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pipelineIndexOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkPipelineCacheHeaderVersionOne',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
