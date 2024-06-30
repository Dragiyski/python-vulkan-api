from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSpecializationInfo'
_member_list_ = ['mapEntryCount', 'pMapEntries', 'dataSize', 'pData']
_member_info_ = {
    'mapEntryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMapEntries': {
        'type': CPointerType(CComplexType('VkSpecializationMapEntry')),
        'type_name': 'VkSpecializationMapEntry',
        'structure': 'VkSpecializationMapEntry',
        'length': [['mapEntryCount']],
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'length': [['dataSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSpecializationMapEntry',
}
_included_in_ = {
    'VkPipelineShaderStageCreateInfo',
    'VkShaderCreateInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
