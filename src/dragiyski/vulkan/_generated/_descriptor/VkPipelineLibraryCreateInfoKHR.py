from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineLibraryCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'libraryCount', 'pLibraries']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'libraryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pLibraries': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['libraryCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkExecutionGraphPipelineCreateInfoAMDX',
    'VkRayTracingPipelineCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
