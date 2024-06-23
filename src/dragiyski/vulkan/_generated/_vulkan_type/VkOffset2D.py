import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDisplayPlaneCapabilitiesKHR',
        'VkImageViewSampleWeightCreateInfoQCOM',
        'VkRect2D',
        'VkRectLayerKHR',
        'VkSubpassFragmentDensityMapOffsetEndInfoQCOM',
        'VkTilePropertiesQCOM',
        'VkVideoDecodeH264CapabilitiesKHR',
        'VkVideoPictureResourceInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x']},
        'y': {'python_name': ['y']},
    }
}
