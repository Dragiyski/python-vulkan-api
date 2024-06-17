import ctypes, sys

class VkPipelineColorBlendStateCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineColorBlendStateCreateInfo

from . import VkPipelineColorBlendAttachmentState

VkPipelineColorBlendStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('logicOpEnable', ctypes.c_uint32),
    ('logicOp', ctypes.c_int),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkPipelineColorBlendAttachmentState)),
    ('blendConstants', ctypes.ARRAY(ctypes.c_float, 4)),
]
