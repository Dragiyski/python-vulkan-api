import ctypes, sys

class VkPipelineCreationFeedbackCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineCreationFeedbackCreateInfo

from . import VkPipelineCreationFeedback

VkPipelineCreationFeedbackCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pPipelineCreationFeedback', ctypes.POINTER(VkPipelineCreationFeedback)),
    ('pipelineStageCreationFeedbackCount', ctypes.c_uint32),
    ('pPipelineStageCreationFeedbacks', ctypes.POINTER(VkPipelineCreationFeedback)),
]
