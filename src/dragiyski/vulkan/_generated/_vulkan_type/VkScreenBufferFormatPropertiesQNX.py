import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('externalFormat', ctypes.c_uint64),
    ('screenUsage', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint32),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]

descriptor = {
    'extends': {
        'VkScreenBufferPropertiesQNX',
    },
    'extended_by': set(),
    'includes': {
        'VkComponentMapping',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SCREEN_BUFFER_FORMAT_PROPERTIES_QNX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'externalFormat': {'python_name': ['external', 'format']},
        'screenUsage': {'python_name': ['screen', 'usage']},
        'formatFeatures': {'python_name': ['format', 'features'], 'type': 'VkFormatFeatureFlags'},
        'samplerYcbcrConversionComponents': {'python_name': ['sampler', 'ycbcr', 'conversion', 'components'], 'type': 'VkComponentMapping'},
        'suggestedYcbcrModel': {'python_name': ['suggested', 'ycbcr', 'model'], 'type': 'VkSamplerYcbcrModelConversion'},
        'suggestedYcbcrRange': {'python_name': ['suggested', 'ycbcr', 'range'], 'type': 'VkSamplerYcbcrRange'},
        'suggestedXChromaOffset': {'python_name': ['suggested', 'xchroma', 'offset'], 'type': 'VkChromaLocation'},
        'suggestedYChromaOffset': {'python_name': ['suggested', 'ychroma', 'offset'], 'type': 'VkChromaLocation'},
    }
}
