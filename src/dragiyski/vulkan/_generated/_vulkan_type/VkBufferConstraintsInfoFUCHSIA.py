import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCollectionConstraintsInfoFUCHSIA import CType as VkBufferCollectionConstraintsInfoFUCHSIA
from .VkBufferCreateInfo import CType as VkBufferCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('createInfo', VkBufferCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferCollectionConstraintsInfoFUCHSIA',
        'VkBufferCreateInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkSetBufferCollectionBufferConstraintsFUCHSIA',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_CONSTRAINTS_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'createInfo': {'python_name': ['create', 'info'], 'type': 'VkBufferCreateInfo'},
        'requiredFormatFeatures': {'python_name': ['required', 'format', 'features'], 'type': 'VkFormatFeatureFlags'},
        'bufferCollectionConstraints': {'python_name': ['buffer', 'collection', 'constraints'], 'type': 'VkBufferCollectionConstraintsInfoFUCHSIA'},
    }
}
