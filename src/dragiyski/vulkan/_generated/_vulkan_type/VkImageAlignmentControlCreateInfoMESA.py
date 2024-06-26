import ctypes

class VkImageAlignmentControlCreateInfoMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maximumRequestedAlignment', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maximumRequestedAlignment': 'maximum_requested_alignment',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_MESA_image_alignment_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_ALIGNMENT_CONTROL_CREATE_INFO_MESA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_ALIGNMENT_CONTROL_CREATE_INFO_MESA
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageAlignmentControlCreateInfoMESA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maximumRequestedAlignment': ctypes.c_uint32,
}
