from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceLimits'
_member_list_ = ['maxImageDimension1D', 'maxImageDimension2D', 'maxImageDimension3D', 'maxImageDimensionCube', 'maxImageArrayLayers', 'maxTexelBufferElements', 'maxUniformBufferRange', 'maxStorageBufferRange', 'maxPushConstantsSize', 'maxMemoryAllocationCount', 'maxSamplerAllocationCount', 'bufferImageGranularity', 'sparseAddressSpaceSize', 'maxBoundDescriptorSets', 'maxPerStageDescriptorSamplers', 'maxPerStageDescriptorUniformBuffers', 'maxPerStageDescriptorStorageBuffers', 'maxPerStageDescriptorSampledImages', 'maxPerStageDescriptorStorageImages', 'maxPerStageDescriptorInputAttachments', 'maxPerStageResources', 'maxDescriptorSetSamplers', 'maxDescriptorSetUniformBuffers', 'maxDescriptorSetUniformBuffersDynamic', 'maxDescriptorSetStorageBuffers', 'maxDescriptorSetStorageBuffersDynamic', 'maxDescriptorSetSampledImages', 'maxDescriptorSetStorageImages', 'maxDescriptorSetInputAttachments', 'maxVertexInputAttributes', 'maxVertexInputBindings', 'maxVertexInputAttributeOffset', 'maxVertexInputBindingStride', 'maxVertexOutputComponents', 'maxTessellationGenerationLevel', 'maxTessellationPatchSize', 'maxTessellationControlPerVertexInputComponents', 'maxTessellationControlPerVertexOutputComponents', 'maxTessellationControlPerPatchOutputComponents', 'maxTessellationControlTotalOutputComponents', 'maxTessellationEvaluationInputComponents', 'maxTessellationEvaluationOutputComponents', 'maxGeometryShaderInvocations', 'maxGeometryInputComponents', 'maxGeometryOutputComponents', 'maxGeometryOutputVertices', 'maxGeometryTotalOutputComponents', 'maxFragmentInputComponents', 'maxFragmentOutputAttachments', 'maxFragmentDualSrcAttachments', 'maxFragmentCombinedOutputResources', 'maxComputeSharedMemorySize', 'maxComputeWorkGroupCount', 'maxComputeWorkGroupInvocations', 'maxComputeWorkGroupSize', 'subPixelPrecisionBits', 'subTexelPrecisionBits', 'mipmapPrecisionBits', 'maxDrawIndexedIndexValue', 'maxDrawIndirectCount', 'maxSamplerLodBias', 'maxSamplerAnisotropy', 'maxViewports', 'maxViewportDimensions', 'viewportBoundsRange', 'viewportSubPixelBits', 'minMemoryMapAlignment', 'minTexelBufferOffsetAlignment', 'minUniformBufferOffsetAlignment', 'minStorageBufferOffsetAlignment', 'minTexelOffset', 'maxTexelOffset', 'minTexelGatherOffset', 'maxTexelGatherOffset', 'minInterpolationOffset', 'maxInterpolationOffset', 'subPixelInterpolationOffsetBits', 'maxFramebufferWidth', 'maxFramebufferHeight', 'maxFramebufferLayers', 'framebufferColorSampleCounts', 'framebufferDepthSampleCounts', 'framebufferStencilSampleCounts', 'framebufferNoAttachmentsSampleCounts', 'maxColorAttachments', 'sampledImageColorSampleCounts', 'sampledImageIntegerSampleCounts', 'sampledImageDepthSampleCounts', 'sampledImageStencilSampleCounts', 'storageImageSampleCounts', 'maxSampleMaskWords', 'timestampComputeAndGraphics', 'timestampPeriod', 'maxClipDistances', 'maxCullDistances', 'maxCombinedClipAndCullDistances', 'discreteQueuePriorities', 'pointSizeRange', 'lineWidthRange', 'pointSizeGranularity', 'lineWidthGranularity', 'strictLines', 'standardSampleLocations', 'optimalBufferCopyOffsetAlignment', 'optimalBufferCopyRowPitchAlignment', 'nonCoherentAtomSize']
_member_info_ = {
    'maxImageDimension1D': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxImageDimension2D': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxImageDimension3D': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxImageDimensionCube': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxImageArrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTexelBufferElements': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxUniformBufferRange': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxStorageBufferRange': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPushConstantsSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMemoryAllocationCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSamplerAllocationCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferImageGranularity': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'sparseAddressSpaceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxBoundDescriptorSets': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUniformBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorStorageBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorSampledImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorStorageImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorInputAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageResources': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUniformBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUniformBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetStorageBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetStorageBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetSampledImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetStorageImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetInputAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVertexInputAttributes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVertexInputBindings': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVertexInputAttributeOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVertexInputBindingStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVertexOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationGenerationLevel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationPatchSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationControlPerVertexInputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationControlPerVertexOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationControlPerPatchOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationControlTotalOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationEvaluationInputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTessellationEvaluationOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryShaderInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryInputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryOutputVertices': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxGeometryTotalOutputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentInputComponents': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentOutputAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentDualSrcAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentCombinedOutputResources': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxComputeSharedMemorySize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxComputeWorkGroupCount': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'maxComputeWorkGroupInvocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxComputeWorkGroupSize': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
    'subPixelPrecisionBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subTexelPrecisionBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'mipmapPrecisionBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDrawIndexedIndexValue': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDrawIndirectCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSamplerLodBias': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxSamplerAnisotropy': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxViewports': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxViewportDimensions': {
        'type': CArrayType(CIntType('c_uint32'), 2),
        'is_string': False,
    },
    'viewportBoundsRange': {
        'type': CArrayType(CFloatType('c_float'), 2),
        'is_string': False,
    },
    'viewportSubPixelBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minMemoryMapAlignment': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'minTexelBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'minUniformBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'minStorageBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'minTexelOffset': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'maxTexelOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minTexelGatherOffset': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'maxTexelGatherOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minInterpolationOffset': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxInterpolationOffset': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'subPixelInterpolationOffsetBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFramebufferWidth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFramebufferHeight': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFramebufferLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'framebufferColorSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'framebufferDepthSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'framebufferStencilSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'framebufferNoAttachmentsSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'maxColorAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sampledImageColorSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'sampledImageIntegerSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'sampledImageDepthSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'sampledImageStencilSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'storageImageSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'maxSampleMaskWords': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'timestampComputeAndGraphics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'timestampPeriod': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxClipDistances': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxCullDistances': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxCombinedClipAndCullDistances': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'discreteQueuePriorities': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pointSizeRange': {
        'type': CArrayType(CFloatType('c_float'), 2),
        'is_string': False,
    },
    'lineWidthRange': {
        'type': CArrayType(CFloatType('c_float'), 2),
        'is_string': False,
    },
    'pointSizeGranularity': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'lineWidthGranularity': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'strictLines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'standardSampleLocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'optimalBufferCopyOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'optimalBufferCopyRowPitchAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'nonCoherentAtomSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPhysicalDeviceProperties',
}
_input_of_ = set()
_output_of_ = set()
