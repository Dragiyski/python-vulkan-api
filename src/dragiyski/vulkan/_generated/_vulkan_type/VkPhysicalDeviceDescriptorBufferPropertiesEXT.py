import ctypes

class VkPhysicalDeviceDescriptorBufferPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('combinedImageSamplerDescriptorSingleArray', ctypes.c_uint32),
        ('bufferlessPushDescriptors', ctypes.c_uint32),
        ('allowSamplerImageViewPostSubmitCreation', ctypes.c_uint32),
        ('descriptorBufferOffsetAlignment', ctypes.c_uint64),
        ('maxDescriptorBufferBindings', ctypes.c_uint32),
        ('maxResourceDescriptorBufferBindings', ctypes.c_uint32),
        ('maxSamplerDescriptorBufferBindings', ctypes.c_uint32),
        ('maxEmbeddedImmutableSamplerBindings', ctypes.c_uint32),
        ('maxEmbeddedImmutableSamplers', ctypes.c_uint32),
        ('bufferCaptureReplayDescriptorDataSize', ctypes.c_size_t),
        ('imageCaptureReplayDescriptorDataSize', ctypes.c_size_t),
        ('imageViewCaptureReplayDescriptorDataSize', ctypes.c_size_t),
        ('samplerCaptureReplayDescriptorDataSize', ctypes.c_size_t),
        ('accelerationStructureCaptureReplayDescriptorDataSize', ctypes.c_size_t),
        ('samplerDescriptorSize', ctypes.c_size_t),
        ('combinedImageSamplerDescriptorSize', ctypes.c_size_t),
        ('sampledImageDescriptorSize', ctypes.c_size_t),
        ('storageImageDescriptorSize', ctypes.c_size_t),
        ('uniformTexelBufferDescriptorSize', ctypes.c_size_t),
        ('robustUniformTexelBufferDescriptorSize', ctypes.c_size_t),
        ('storageTexelBufferDescriptorSize', ctypes.c_size_t),
        ('robustStorageTexelBufferDescriptorSize', ctypes.c_size_t),
        ('uniformBufferDescriptorSize', ctypes.c_size_t),
        ('robustUniformBufferDescriptorSize', ctypes.c_size_t),
        ('storageBufferDescriptorSize', ctypes.c_size_t),
        ('robustStorageBufferDescriptorSize', ctypes.c_size_t),
        ('inputAttachmentDescriptorSize', ctypes.c_size_t),
        ('accelerationStructureDescriptorSize', ctypes.c_size_t),
        ('maxSamplerDescriptorBufferRange', ctypes.c_uint64),
        ('maxResourceDescriptorBufferRange', ctypes.c_uint64),
        ('samplerDescriptorBufferAddressSpaceSize', ctypes.c_uint64),
        ('resourceDescriptorBufferAddressSpaceSize', ctypes.c_uint64),
        ('descriptorBufferAddressSpaceSize', ctypes.c_uint64),
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
        'combinedImageSamplerDescriptorSingleArray': 'combined_image_sampler_descriptor_single_array',
        'bufferlessPushDescriptors': 'bufferless_push_descriptors',
        'allowSamplerImageViewPostSubmitCreation': 'allow_sampler_image_view_post_submit_creation',
        'descriptorBufferOffsetAlignment': 'descriptor_buffer_offset_alignment',
        'maxDescriptorBufferBindings': 'max_descriptor_buffer_bindings',
        'maxResourceDescriptorBufferBindings': 'max_resource_descriptor_buffer_bindings',
        'maxSamplerDescriptorBufferBindings': 'max_sampler_descriptor_buffer_bindings',
        'maxEmbeddedImmutableSamplerBindings': 'max_embedded_immutable_sampler_bindings',
        'maxEmbeddedImmutableSamplers': 'max_embedded_immutable_samplers',
        'bufferCaptureReplayDescriptorDataSize': 'buffer_capture_replay_descriptor_data_size',
        'imageCaptureReplayDescriptorDataSize': 'image_capture_replay_descriptor_data_size',
        'imageViewCaptureReplayDescriptorDataSize': 'image_view_capture_replay_descriptor_data_size',
        'samplerCaptureReplayDescriptorDataSize': 'sampler_capture_replay_descriptor_data_size',
        'accelerationStructureCaptureReplayDescriptorDataSize': 'acceleration_structure_capture_replay_descriptor_data_size',
        'samplerDescriptorSize': 'sampler_descriptor_size',
        'combinedImageSamplerDescriptorSize': 'combined_image_sampler_descriptor_size',
        'sampledImageDescriptorSize': 'sampled_image_descriptor_size',
        'storageImageDescriptorSize': 'storage_image_descriptor_size',
        'uniformTexelBufferDescriptorSize': 'uniform_texel_buffer_descriptor_size',
        'robustUniformTexelBufferDescriptorSize': 'robust_uniform_texel_buffer_descriptor_size',
        'storageTexelBufferDescriptorSize': 'storage_texel_buffer_descriptor_size',
        'robustStorageTexelBufferDescriptorSize': 'robust_storage_texel_buffer_descriptor_size',
        'uniformBufferDescriptorSize': 'uniform_buffer_descriptor_size',
        'robustUniformBufferDescriptorSize': 'robust_uniform_buffer_descriptor_size',
        'storageBufferDescriptorSize': 'storage_buffer_descriptor_size',
        'robustStorageBufferDescriptorSize': 'robust_storage_buffer_descriptor_size',
        'inputAttachmentDescriptorSize': 'input_attachment_descriptor_size',
        'accelerationStructureDescriptorSize': 'acceleration_structure_descriptor_size',
        'maxSamplerDescriptorBufferRange': 'max_sampler_descriptor_buffer_range',
        'maxResourceDescriptorBufferRange': 'max_resource_descriptor_buffer_range',
        'samplerDescriptorBufferAddressSpaceSize': 'sampler_descriptor_buffer_address_space_size',
        'resourceDescriptorBufferAddressSpaceSize': 'resource_descriptor_buffer_address_space_size',
        'descriptorBufferAddressSpaceSize': 'descriptor_buffer_address_space_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDescriptorBufferPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'combinedImageSamplerDescriptorSingleArray': ctypes.c_uint32,
    'bufferlessPushDescriptors': ctypes.c_uint32,
    'allowSamplerImageViewPostSubmitCreation': ctypes.c_uint32,
    'descriptorBufferOffsetAlignment': ctypes.c_uint64,
    'maxDescriptorBufferBindings': ctypes.c_uint32,
    'maxResourceDescriptorBufferBindings': ctypes.c_uint32,
    'maxSamplerDescriptorBufferBindings': ctypes.c_uint32,
    'maxEmbeddedImmutableSamplerBindings': ctypes.c_uint32,
    'maxEmbeddedImmutableSamplers': ctypes.c_uint32,
    'bufferCaptureReplayDescriptorDataSize': ctypes.c_size_t,
    'imageCaptureReplayDescriptorDataSize': ctypes.c_size_t,
    'imageViewCaptureReplayDescriptorDataSize': ctypes.c_size_t,
    'samplerCaptureReplayDescriptorDataSize': ctypes.c_size_t,
    'accelerationStructureCaptureReplayDescriptorDataSize': ctypes.c_size_t,
    'samplerDescriptorSize': ctypes.c_size_t,
    'combinedImageSamplerDescriptorSize': ctypes.c_size_t,
    'sampledImageDescriptorSize': ctypes.c_size_t,
    'storageImageDescriptorSize': ctypes.c_size_t,
    'uniformTexelBufferDescriptorSize': ctypes.c_size_t,
    'robustUniformTexelBufferDescriptorSize': ctypes.c_size_t,
    'storageTexelBufferDescriptorSize': ctypes.c_size_t,
    'robustStorageTexelBufferDescriptorSize': ctypes.c_size_t,
    'uniformBufferDescriptorSize': ctypes.c_size_t,
    'robustUniformBufferDescriptorSize': ctypes.c_size_t,
    'storageBufferDescriptorSize': ctypes.c_size_t,
    'robustStorageBufferDescriptorSize': ctypes.c_size_t,
    'inputAttachmentDescriptorSize': ctypes.c_size_t,
    'accelerationStructureDescriptorSize': ctypes.c_size_t,
    'maxSamplerDescriptorBufferRange': ctypes.c_uint64,
    'maxResourceDescriptorBufferRange': ctypes.c_uint64,
    'samplerDescriptorBufferAddressSpaceSize': ctypes.c_uint64,
    'resourceDescriptorBufferAddressSpaceSize': ctypes.c_uint64,
    'descriptorBufferAddressSpaceSize': ctypes.c_uint64,
}
