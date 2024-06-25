import ctypes

class VkPipelineCreationFeedbackCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pPipelineCreationFeedback': ctypes.POINTER(VkPipelineCreationFeedback),
            'pipelineStageCreationFeedbackCount': ctypes.c_uint32,
            'pPipelineStageCreationFeedbacks': ctypes.POINTER(VkPipelineCreationFeedback),
        }


from .VkPipelineCreationFeedback import VkPipelineCreationFeedback

VkPipelineCreationFeedbackCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pPipelineCreationFeedback', ctypes.POINTER(VkPipelineCreationFeedback)),
    ('pipelineStageCreationFeedbackCount', ctypes.c_uint32),
    ('pPipelineStageCreationFeedbacks', ctypes.POINTER(VkPipelineCreationFeedback)),
]
