import ctypes

class CType(ctypes.Structure):
    pass

from .VkXYColorEXT import CType as VkXYColorEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPrimaryRed', VkXYColorEXT),
    ('displayPrimaryGreen', VkXYColorEXT),
    ('displayPrimaryBlue', VkXYColorEXT),
    ('whitePoint', VkXYColorEXT),
    ('maxLuminance', ctypes.c_float),
    ('minLuminance', ctypes.c_float),
    ('maxContentLightLevel', ctypes.c_float),
    ('maxFrameAverageLightLevel', ctypes.c_float),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkXYColorEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkSetHdrMetadataEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_HDR_METADATA_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'displayPrimaryRed': {'python_name': ['display', 'primary', 'red'], 'type': 'VkXYColorEXT'},
        'displayPrimaryGreen': {'python_name': ['display', 'primary', 'green'], 'type': 'VkXYColorEXT'},
        'displayPrimaryBlue': {'python_name': ['display', 'primary', 'blue'], 'type': 'VkXYColorEXT'},
        'whitePoint': {'python_name': ['white', 'point'], 'type': 'VkXYColorEXT'},
        'maxLuminance': {'python_name': ['max', 'luminance']},
        'minLuminance': {'python_name': ['min', 'luminance']},
        'maxContentLightLevel': {'python_name': ['max', 'content', 'light', 'level']},
        'maxFrameAverageLightLevel': {'python_name': ['max', 'frame', 'average', 'light', 'level']},
    }
}
