import ctypes

class VkMemoryOpaqueCaptureAddressAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opaqueCaptureAddress', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkMemoryAllocateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'opaqueCaptureAddress': 'opaque_capture_address',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryOpaqueCaptureAddressAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'opaqueCaptureAddress': ctypes.c_uint64,
}
