import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('libraryCount', ctypes.c_uint32),
        ('pLibraries', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkRayTracingPipelineCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'libraryCount': {'python_name': ['library', 'count']},
        'pLibraries': {'python_name': ['p', 'libraries'], 'len': [['libraryCount']]},
    }
}
