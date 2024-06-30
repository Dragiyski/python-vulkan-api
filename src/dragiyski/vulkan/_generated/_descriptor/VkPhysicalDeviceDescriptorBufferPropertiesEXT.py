from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDescriptorBufferPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'combinedImageSamplerDescriptorSingleArray', 'bufferlessPushDescriptors', 'allowSamplerImageViewPostSubmitCreation', 'descriptorBufferOffsetAlignment', 'maxDescriptorBufferBindings', 'maxResourceDescriptorBufferBindings', 'maxSamplerDescriptorBufferBindings', 'maxEmbeddedImmutableSamplerBindings', 'maxEmbeddedImmutableSamplers', 'bufferCaptureReplayDescriptorDataSize', 'imageCaptureReplayDescriptorDataSize', 'imageViewCaptureReplayDescriptorDataSize', 'samplerCaptureReplayDescriptorDataSize', 'accelerationStructureCaptureReplayDescriptorDataSize', 'samplerDescriptorSize', 'combinedImageSamplerDescriptorSize', 'sampledImageDescriptorSize', 'storageImageDescriptorSize', 'uniformTexelBufferDescriptorSize', 'robustUniformTexelBufferDescriptorSize', 'storageTexelBufferDescriptorSize', 'robustStorageTexelBufferDescriptorSize', 'uniformBufferDescriptorSize', 'robustUniformBufferDescriptorSize', 'storageBufferDescriptorSize', 'robustStorageBufferDescriptorSize', 'inputAttachmentDescriptorSize', 'accelerationStructureDescriptorSize', 'maxSamplerDescriptorBufferRange', 'maxResourceDescriptorBufferRange', 'samplerDescriptorBufferAddressSpaceSize', 'resourceDescriptorBufferAddressSpaceSize', 'descriptorBufferAddressSpaceSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'combinedImageSamplerDescriptorSingleArray': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferlessPushDescriptors': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'allowSamplerImageViewPostSubmitCreation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxDescriptorBufferBindings': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxResourceDescriptorBufferBindings': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSamplerDescriptorBufferBindings': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxEmbeddedImmutableSamplerBindings': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxEmbeddedImmutableSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferCaptureReplayDescriptorDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'imageCaptureReplayDescriptorDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'imageViewCaptureReplayDescriptorDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'samplerCaptureReplayDescriptorDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'accelerationStructureCaptureReplayDescriptorDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'samplerDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'combinedImageSamplerDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'sampledImageDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'storageImageDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'uniformTexelBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'robustUniformTexelBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'storageTexelBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'robustStorageTexelBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'uniformBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'robustUniformBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'storageBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'robustStorageBufferDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'inputAttachmentDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'accelerationStructureDescriptorSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'maxSamplerDescriptorBufferRange': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxResourceDescriptorBufferRange': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'samplerDescriptorBufferAddressSpaceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'resourceDescriptorBufferAddressSpaceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'descriptorBufferAddressSpaceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
