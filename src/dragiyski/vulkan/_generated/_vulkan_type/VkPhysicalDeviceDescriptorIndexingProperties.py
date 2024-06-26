import ctypes

class VkPhysicalDeviceDescriptorIndexingProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxUpdateAfterBindDescriptorsInAllPools', ctypes.c_uint32),
        ('shaderUniformBufferArrayNonUniformIndexingNative', ctypes.c_uint32),
        ('shaderSampledImageArrayNonUniformIndexingNative', ctypes.c_uint32),
        ('shaderStorageBufferArrayNonUniformIndexingNative', ctypes.c_uint32),
        ('shaderStorageImageArrayNonUniformIndexingNative', ctypes.c_uint32),
        ('shaderInputAttachmentArrayNonUniformIndexingNative', ctypes.c_uint32),
        ('robustBufferAccessUpdateAfterBind', ctypes.c_uint32),
        ('quadDivergentImplicitLod', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindSamplers', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindUniformBuffers', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindStorageBuffers', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindSampledImages', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindStorageImages', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindInputAttachments', ctypes.c_uint32),
        ('maxPerStageUpdateAfterBindResources', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindSamplers', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindUniformBuffers', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindUniformBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindStorageBuffers', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindStorageBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindSampledImages', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindStorageImages', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindInputAttachments', ctypes.c_uint32),
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
        'maxUpdateAfterBindDescriptorsInAllPools': 'max_update_after_bind_descriptors_in_all_pools',
        'shaderUniformBufferArrayNonUniformIndexingNative': 'shader_uniform_buffer_array_non_uniform_indexing_native',
        'shaderSampledImageArrayNonUniformIndexingNative': 'shader_sampled_image_array_non_uniform_indexing_native',
        'shaderStorageBufferArrayNonUniformIndexingNative': 'shader_storage_buffer_array_non_uniform_indexing_native',
        'shaderStorageImageArrayNonUniformIndexingNative': 'shader_storage_image_array_non_uniform_indexing_native',
        'shaderInputAttachmentArrayNonUniformIndexingNative': 'shader_input_attachment_array_non_uniform_indexing_native',
        'robustBufferAccessUpdateAfterBind': 'robust_buffer_access_update_after_bind',
        'quadDivergentImplicitLod': 'quad_divergent_implicit_lod',
        'maxPerStageDescriptorUpdateAfterBindSamplers': 'max_per_stage_descriptor_update_after_bind_samplers',
        'maxPerStageDescriptorUpdateAfterBindUniformBuffers': 'max_per_stage_descriptor_update_after_bind_uniform_buffers',
        'maxPerStageDescriptorUpdateAfterBindStorageBuffers': 'max_per_stage_descriptor_update_after_bind_storage_buffers',
        'maxPerStageDescriptorUpdateAfterBindSampledImages': 'max_per_stage_descriptor_update_after_bind_sampled_images',
        'maxPerStageDescriptorUpdateAfterBindStorageImages': 'max_per_stage_descriptor_update_after_bind_storage_images',
        'maxPerStageDescriptorUpdateAfterBindInputAttachments': 'max_per_stage_descriptor_update_after_bind_input_attachments',
        'maxPerStageUpdateAfterBindResources': 'max_per_stage_update_after_bind_resources',
        'maxDescriptorSetUpdateAfterBindSamplers': 'max_descriptor_set_update_after_bind_samplers',
        'maxDescriptorSetUpdateAfterBindUniformBuffers': 'max_descriptor_set_update_after_bind_uniform_buffers',
        'maxDescriptorSetUpdateAfterBindUniformBuffersDynamic': 'max_descriptor_set_update_after_bind_uniform_buffers_dynamic',
        'maxDescriptorSetUpdateAfterBindStorageBuffers': 'max_descriptor_set_update_after_bind_storage_buffers',
        'maxDescriptorSetUpdateAfterBindStorageBuffersDynamic': 'max_descriptor_set_update_after_bind_storage_buffers_dynamic',
        'maxDescriptorSetUpdateAfterBindSampledImages': 'max_descriptor_set_update_after_bind_sampled_images',
        'maxDescriptorSetUpdateAfterBindStorageImages': 'max_descriptor_set_update_after_bind_storage_images',
        'maxDescriptorSetUpdateAfterBindInputAttachments': 'max_descriptor_set_update_after_bind_input_attachments',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDescriptorIndexingProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxUpdateAfterBindDescriptorsInAllPools': ctypes.c_uint32,
    'shaderUniformBufferArrayNonUniformIndexingNative': ctypes.c_uint32,
    'shaderSampledImageArrayNonUniformIndexingNative': ctypes.c_uint32,
    'shaderStorageBufferArrayNonUniformIndexingNative': ctypes.c_uint32,
    'shaderStorageImageArrayNonUniformIndexingNative': ctypes.c_uint32,
    'shaderInputAttachmentArrayNonUniformIndexingNative': ctypes.c_uint32,
    'robustBufferAccessUpdateAfterBind': ctypes.c_uint32,
    'quadDivergentImplicitLod': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindSamplers': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindUniformBuffers': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindStorageBuffers': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindSampledImages': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindStorageImages': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindInputAttachments': ctypes.c_uint32,
    'maxPerStageUpdateAfterBindResources': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindSamplers': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindUniformBuffers': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindUniformBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindStorageBuffers': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindStorageBuffersDynamic': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindSampledImages': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindStorageImages': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindInputAttachments': ctypes.c_uint32,
}
