import ctypes

class CType(ctypes.Structure):
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
