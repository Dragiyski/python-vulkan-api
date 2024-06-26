import ctypes

class VkPhysicalDeviceImageProcessingFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('textureSampleWeighted', ctypes.c_uint32),
        ('textureBoxFilter', ctypes.c_uint32),
        ('textureBlockMatch', ctypes.c_uint32),
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
        'textureSampleWeighted': 'texture_sample_weighted',
        'textureBoxFilter': 'texture_box_filter',
        'textureBlockMatch': 'texture_block_match',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_image_processing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_FEATURES_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_FEATURES_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceImageProcessingFeaturesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'textureSampleWeighted': ctypes.c_uint32,
    'textureBoxFilter': ctypes.c_uint32,
    'textureBlockMatch': ctypes.c_uint32,
}
