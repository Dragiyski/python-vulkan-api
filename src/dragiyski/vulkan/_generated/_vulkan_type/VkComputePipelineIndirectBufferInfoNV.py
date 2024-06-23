import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('pipelineDeviceAddressCaptureReplay', ctypes.c_uint64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_INDIRECT_BUFFER_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceAddress': {'python_name': ['device', 'address']},
        'size': {'python_name': ['size']},
        'pipelineDeviceAddressCaptureReplay': {'python_name': ['pipeline', 'device', 'address', 'capture', 'replay']},
    }
}
