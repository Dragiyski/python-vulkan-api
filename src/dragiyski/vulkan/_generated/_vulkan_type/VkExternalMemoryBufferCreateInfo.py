import ctypes

class VkExternalMemoryBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleTypes', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkBufferCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'handleTypes': 'handle_types',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'handleTypes': 'VkExternalMemoryHandleTypeFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkExternalMemoryBufferCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'handleTypes': ctypes.c_uint32,
}
