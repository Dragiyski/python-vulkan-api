import ctypes

class CType(ctypes.Structure):
    pass

from .VkSpecializationMapEntry import CType as VkSpecializationMapEntry

CType._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSpecializationMapEntry',
    },
    'included_in': {
        'VkPipelineShaderStageCreateInfo',
        'VkShaderCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'mapEntryCount': {'python_name': ['map', 'entry', 'count']},
        'pMapEntries': {'python_name': ['p', 'map', 'entries'], 'len': [['mapEntryCount']], 'type': 'VkSpecializationMapEntry'},
        'dataSize': {'python_name': ['data', 'size']},
        'pData': {'python_name': ['p', 'data'], 'len': [['dataSize']]},
    }
}
