import ctypes

class VkPhysicalDeviceRenderPassStripedPropertiesARM(ctypes.Structure):
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
        'renderPassStripeGranularity': 'render_pass_stripe_granularity',
        'maxRenderPassStripes': 'max_render_pass_stripes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ARM_render_pass_striped',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RENDER_PASS_STRIPED_PROPERTIES_ARM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RENDER_PASS_STRIPED_PROPERTIES_ARM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceRenderPassStripedPropertiesARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
]

VkPhysicalDeviceRenderPassStripedPropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPassStripeGranularity': VkExtent2D,
    'maxRenderPassStripes': ctypes.c_uint32,
}
