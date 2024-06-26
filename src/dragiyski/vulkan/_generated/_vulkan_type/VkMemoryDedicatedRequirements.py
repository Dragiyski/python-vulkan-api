import ctypes

class VkMemoryDedicatedRequirements(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('prefersDedicatedAllocation', ctypes.c_uint32),
        ('requiresDedicatedAllocation', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkMemoryRequirements2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'prefersDedicatedAllocation': 'prefers_dedicated_allocation',
        'requiresDedicatedAllocation': 'requires_dedicated_allocation',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryDedicatedRequirements._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'prefersDedicatedAllocation': ctypes.c_uint32,
    'requiresDedicatedAllocation': ctypes.c_uint32,
}
