import ctypes

class VkBufferViewCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkExportMetalObjectCreateInfoEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateBufferView',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'buffer': 'buffer',
        'format': 'format',
        'offset': 'offset',
        'range': 'range',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkBufferViewCreateFlags',
        'format': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferViewCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'buffer': ctypes.c_void_p,
    'format': ctypes.c_int,
    'offset': ctypes.c_uint64,
    'range': ctypes.c_uint64,
}
