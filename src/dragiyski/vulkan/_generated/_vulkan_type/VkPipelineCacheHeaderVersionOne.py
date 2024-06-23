import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineCacheHeaderVersionSafetyCriticalOne',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'headerSize': {'python_name': ['header', 'size']},
        'headerVersion': {'python_name': ['header', 'version'], 'type': 'VkPipelineCacheHeaderVersion'},
        'vendorID': {'python_name': ['vendor', 'id']},
        'deviceID': {'python_name': ['device', 'id']},
        'pipelineCacheUUID': {'python_name': ['pipeline', 'cache', 'uuid']},
    }
}
