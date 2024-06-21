import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineCreationFeedback import CType as VkPipelineCreationFeedback

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pPipelineCreationFeedback', ctypes.POINTER(VkPipelineCreationFeedback)),
    ('pipelineStageCreationFeedbackCount', ctypes.c_uint32),
    ('pPipelineStageCreationFeedbacks', ctypes.POINTER(VkPipelineCreationFeedback)),
]
