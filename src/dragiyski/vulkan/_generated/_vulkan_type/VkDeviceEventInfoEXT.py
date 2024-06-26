import ctypes

class VkDeviceEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceEvent', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkRegisterDeviceEventEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'deviceEvent': 'device_event',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_display_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'deviceEvent': 'VkDeviceEventTypeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_EVENT_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_EVENT_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceEventInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceEvent': ctypes.c_int,
}
