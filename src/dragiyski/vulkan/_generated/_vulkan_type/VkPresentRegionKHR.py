import ctypes

class CType(ctypes.Structure):
    pass

from .VkRectLayerKHR import CType as VkRectLayerKHR

CType._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkRectLayerKHR',
    },
    'included_in': {
        'VkPresentRegionsKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'rectangleCount': {'python_name': ['rectangle', 'count']},
        'pRectangles': {'python_name': ['p', 'rectangles'], 'len': [['rectangleCount']], 'type': 'VkRectLayerKHR'},
    }
}
