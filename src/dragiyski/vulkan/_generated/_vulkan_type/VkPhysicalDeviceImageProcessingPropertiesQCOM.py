import ctypes

class VkPhysicalDeviceImageProcessingPropertiesQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxWeightFilterPhases': 'max_weight_filter_phases',
        'maxWeightFilterDimension': 'max_weight_filter_dimension',
        'maxBlockMatchRegion': 'max_block_match_region',
        'maxBoxFilterBlockSize': 'max_box_filter_block_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_image_processing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_PROPERTIES_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_PROPERTIES_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceImageProcessingPropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxWeightFilterPhases', ctypes.c_uint32),
    ('maxWeightFilterDimension', VkExtent2D),
    ('maxBlockMatchRegion', VkExtent2D),
    ('maxBoxFilterBlockSize', VkExtent2D),
]

VkPhysicalDeviceImageProcessingPropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxWeightFilterPhases': ctypes.c_uint32,
    'maxWeightFilterDimension': VkExtent2D,
    'maxBlockMatchRegion': VkExtent2D,
    'maxBoxFilterBlockSize': VkExtent2D,
}
