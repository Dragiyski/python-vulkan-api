import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping
from .VkSysmemColorSpaceFUCHSIA import CType as VkSysmemColorSpaceFUCHSIA

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryTypeBits', ctypes.c_uint32),
    ('bufferCount', ctypes.c_uint32),
    ('createInfoIndex', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint32),
    ('sysmemColorSpaceIndex', VkSysmemColorSpaceFUCHSIA),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkComponentMapping',
        'VkSysmemColorSpaceFUCHSIA',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetBufferCollectionPropertiesFUCHSIA',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_PROPERTIES_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryTypeBits': {'python_name': ['memory', 'type', 'bits']},
        'bufferCount': {'python_name': ['buffer', 'count']},
        'createInfoIndex': {'python_name': ['create', 'info', 'index']},
        'sysmemPixelFormat': {'python_name': ['sysmem', 'pixel', 'format']},
        'formatFeatures': {'python_name': ['format', 'features'], 'type': 'VkFormatFeatureFlags'},
        'sysmemColorSpaceIndex': {'python_name': ['sysmem', 'color', 'space', 'index'], 'type': 'VkSysmemColorSpaceFUCHSIA'},
        'samplerYcbcrConversionComponents': {'python_name': ['sampler', 'ycbcr', 'conversion', 'components'], 'type': 'VkComponentMapping'},
        'suggestedYcbcrModel': {'python_name': ['suggested', 'ycbcr', 'model'], 'type': 'VkSamplerYcbcrModelConversion'},
        'suggestedYcbcrRange': {'python_name': ['suggested', 'ycbcr', 'range'], 'type': 'VkSamplerYcbcrRange'},
        'suggestedXChromaOffset': {'python_name': ['suggested', 'xchroma', 'offset'], 'type': 'VkChromaLocation'},
        'suggestedYChromaOffset': {'python_name': ['suggested', 'ychroma', 'offset'], 'type': 'VkChromaLocation'},
    }
}
