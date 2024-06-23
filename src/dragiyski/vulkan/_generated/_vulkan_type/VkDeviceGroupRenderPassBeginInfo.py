import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceMask', ctypes.c_uint32),
    ('deviceRenderAreaCount', ctypes.c_uint32),
    ('pDeviceRenderAreas', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceMask': {'python_name': ['device', 'mask']},
        'deviceRenderAreaCount': {'python_name': ['device', 'render', 'area', 'count']},
        'pDeviceRenderAreas': {'python_name': ['p', 'device', 'render', 'areas'], 'len': [['deviceRenderAreaCount']], 'type': 'VkRect2D'},
    }
}
