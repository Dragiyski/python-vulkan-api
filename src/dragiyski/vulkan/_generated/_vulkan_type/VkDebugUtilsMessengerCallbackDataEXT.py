import ctypes

class CType(ctypes.Structure):
    pass

from .VkDebugUtilsLabelEXT import CType as VkDebugUtilsLabelEXT
from .VkDebugUtilsObjectNameInfoEXT import CType as VkDebugUtilsObjectNameInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pMessageIdName', ctypes.c_char_p),
    ('messageIdNumber', ctypes.c_int32),
    ('pMessage', ctypes.c_char_p),
    ('queueLabelCount', ctypes.c_uint32),
    ('pQueueLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)),
    ('cmdBufLabelCount', ctypes.c_uint32),
    ('pCmdBufLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT)),
]
