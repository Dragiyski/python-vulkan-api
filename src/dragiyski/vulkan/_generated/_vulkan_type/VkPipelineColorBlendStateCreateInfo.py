import ctypes

class VkPipelineColorBlendStateCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'logicOpEnable': ctypes.c_uint32,
            'logicOp': ctypes.c_int,
            'attachmentCount': ctypes.c_uint32,
            'pAttachments': ctypes.POINTER(VkPipelineColorBlendAttachmentState),
            'blendConstants': ctypes.ARRAY(ctypes.c_float, 4),
        }


from .VkPipelineColorBlendAttachmentState import VkPipelineColorBlendAttachmentState

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
