import ctypes

class VkDebugUtilsMessengerCallbackDataEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'pMessageIdName': ctypes.c_char_p,
            'messageIdNumber': ctypes.c_int32,
            'pMessage': ctypes.c_char_p,
            'queueLabelCount': ctypes.c_uint32,
            'pQueueLabels': ctypes.POINTER(VkDebugUtilsLabelEXT),
            'cmdBufLabelCount': ctypes.c_uint32,
            'pCmdBufLabels': ctypes.POINTER(VkDebugUtilsLabelEXT),
            'objectCount': ctypes.c_uint32,
            'pObjects': ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT),
        }


from .VkDebugUtilsLabelEXT import VkDebugUtilsLabelEXT
from .VkDebugUtilsObjectNameInfoEXT import VkDebugUtilsObjectNameInfoEXT

VkDebugUtilsMessengerCallbackDataEXT._fields_ = [
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
