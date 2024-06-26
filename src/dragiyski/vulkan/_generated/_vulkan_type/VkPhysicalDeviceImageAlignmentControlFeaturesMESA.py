import ctypes

class VkPhysicalDeviceImageAlignmentControlFeaturesMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageAlignmentControl', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageAlignmentControl': 'image_alignment_control',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_MESA_image_alignment_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ALIGNMENT_CONTROL_FEATURES_MESA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ALIGNMENT_CONTROL_FEATURES_MESA
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceImageAlignmentControlFeaturesMESA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageAlignmentControl': ctypes.c_uint32,
}
