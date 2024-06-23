import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPass', ctypes.c_void_p),
        ('subpass', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkComputePipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_SHADING_PIPELINE_CREATE_INFO_HUAWEI', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'renderPass': {'python_name': ['render', 'pass']},
        'subpass': {'python_name': ['subpass']},
    }
}
