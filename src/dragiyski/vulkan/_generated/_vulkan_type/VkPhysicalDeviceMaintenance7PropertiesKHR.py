import ctypes

class VkPhysicalDeviceMaintenance7PropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustFragmentShadingRateAttachmentAccess', ctypes.c_uint32),
        ('separateDepthStencilAttachmentAccess', ctypes.c_uint32),
        ('maxDescriptorSetTotalUniformBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetTotalStorageBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetTotalBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindTotalBuffersDynamic', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'robustFragmentShadingRateAttachmentAccess': 'robust_fragment_shading_rate_attachment_access',
        'separateDepthStencilAttachmentAccess': 'separate_depth_stencil_attachment_access',
        'maxDescriptorSetTotalUniformBuffersDynamic': 'max_descriptor_set_total_uniform_buffers_dynamic',
        'maxDescriptorSetTotalStorageBuffersDynamic': 'max_descriptor_set_total_storage_buffers_dynamic',
        'maxDescriptorSetTotalBuffersDynamic': 'max_descriptor_set_total_buffers_dynamic',
        'maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic': 'max_descriptor_set_update_after_bind_total_uniform_buffers_dynamic',
        'maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic': 'max_descriptor_set_update_after_bind_total_storage_buffers_dynamic',
        'maxDescriptorSetUpdateAfterBindTotalBuffersDynamic': 'max_descriptor_set_update_after_bind_total_buffers_dynamic',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance7',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_7_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_7_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceMaintenance7PropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'robustFragmentShadingRateAttachmentAccess': ctypes.c_uint32,
    'separateDepthStencilAttachmentAccess': ctypes.c_uint32,
    'maxDescriptorSetTotalUniformBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetTotalStorageBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetTotalBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindTotalBuffersDynamic': ctypes.c_uint32,
}
