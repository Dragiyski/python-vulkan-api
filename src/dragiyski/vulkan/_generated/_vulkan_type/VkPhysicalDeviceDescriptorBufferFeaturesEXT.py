import ctypes

class VkPhysicalDeviceDescriptorBufferFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorBuffer', ctypes.c_uint32),
        ('descriptorBufferCaptureReplay', ctypes.c_uint32),
        ('descriptorBufferImageLayoutIgnored', ctypes.c_uint32),
        ('descriptorBufferPushDescriptors', ctypes.c_uint32),
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
        'descriptorBuffer': 'descriptor_buffer',
        'descriptorBufferCaptureReplay': 'descriptor_buffer_capture_replay',
        'descriptorBufferImageLayoutIgnored': 'descriptor_buffer_image_layout_ignored',
        'descriptorBufferPushDescriptors': 'descriptor_buffer_push_descriptors',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDescriptorBufferFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorBuffer': ctypes.c_uint32,
    'descriptorBufferCaptureReplay': ctypes.c_uint32,
    'descriptorBufferImageLayoutIgnored': ctypes.c_uint32,
    'descriptorBufferPushDescriptors': ctypes.c_uint32,
}
