import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('ycbcrModel', ctypes.c_int),
    ('ycbcrRange', ctypes.c_int),
    ('components', VkComponentMapping),
    ('xChromaOffset', ctypes.c_int),
    ('yChromaOffset', ctypes.c_int),
    ('chromaFilter', ctypes.c_int),
    ('forceExplicitReconstruction', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExternalFormatANDROID',
        'VkExternalFormatQNX',
        'VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM',
    },
    'includes': {
        'VkComponentMapping',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateSamplerYcbcrConversion',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'ycbcrModel': {'python_name': ['ycbcr', 'model'], 'type': 'VkSamplerYcbcrModelConversion'},
        'ycbcrRange': {'python_name': ['ycbcr', 'range'], 'type': 'VkSamplerYcbcrRange'},
        'components': {'python_name': ['components'], 'type': 'VkComponentMapping'},
        'xChromaOffset': {'python_name': ['x', 'chroma', 'offset'], 'type': 'VkChromaLocation'},
        'yChromaOffset': {'python_name': ['y', 'chroma', 'offset'], 'type': 'VkChromaLocation'},
        'chromaFilter': {'python_name': ['chroma', 'filter'], 'type': 'VkFilter'},
        'forceExplicitReconstruction': {'python_name': ['force', 'explicit', 'reconstruction']},
    }
}
