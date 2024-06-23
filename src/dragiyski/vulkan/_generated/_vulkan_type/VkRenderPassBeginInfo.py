import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearValue import CType as VkClearValue
from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('framebuffer', ctypes.c_void_p),
    ('renderArea', VkRect2D),
    ('clearValueCount', ctypes.c_uint32),
    ('pClearValues', ctypes.POINTER(VkClearValue)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupRenderPassBeginInfo',
        'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM',
        'VkRenderPassAttachmentBeginInfo',
        'VkRenderPassSampleLocationsBeginInfoEXT',
        'VkRenderPassStripeBeginInfoARM',
        'VkRenderPassTransformBeginInfoQCOM',
    },
    'includes': {
        'VkClearValue',
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdBeginRenderPass',
        'vkCmdBeginRenderPass2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'renderPass': {'python_name': ['render', 'pass']},
        'framebuffer': {'python_name': ['framebuffer']},
        'renderArea': {'python_name': ['render', 'area'], 'type': 'VkRect2D'},
        'clearValueCount': {'python_name': ['clear', 'value', 'count']},
        'pClearValues': {'python_name': ['p', 'clear', 'values'], 'len': [['clearValueCount']], 'type': 'VkClearValue'},
    }
}
