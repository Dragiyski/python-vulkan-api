import ctypes

class VkDebugUtilsMessengerCallbackDataEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceAddressBindingCallbackDataEXT',
    }
    _includes_ = {
        'VkDebugUtilsLabelEXT',
        'VkDebugUtilsObjectNameInfoEXT',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkSubmitDebugUtilsMessageEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pMessageIdName': 'message_id_name',
        'messageIdNumber': 'message_id_number',
        'pMessage': 'message',
        'queueLabelCount': 'queue_label_count',
        'pQueueLabels': 'queue_labels',
        'cmdBufLabelCount': 'cmd_buf_label_count',
        'pCmdBufLabels': 'cmd_buf_labels',
        'objectCount': 'object_count',
        'pObjects': 'objects',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_utils',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDebugUtilsMessengerCallbackDataFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkDebugUtilsMessengerCallbackDataEXT._type_ = {
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
