import ctypes, sys

class VkPhysicalDeviceLimits(ctypes.Structure):
    _fields_ = [
        ('maxImageDimension1D', ctypes.c_uint32),
        ('maxImageDimension2D', ctypes.c_uint32),
        ('maxImageDimension3D', ctypes.c_uint32),
        ('maxImageDimensionCube', ctypes.c_uint32),
        ('maxImageArrayLayers', ctypes.c_uint32),
        ('maxTexelBufferElements', ctypes.c_uint32),
        ('maxUniformBufferRange', ctypes.c_uint32),
        ('maxStorageBufferRange', ctypes.c_uint32),
        ('maxPushConstantsSize', ctypes.c_uint32),
        ('maxMemoryAllocationCount', ctypes.c_uint32),
        ('maxSamplerAllocationCount', ctypes.c_uint32),
        ('bufferImageGranularity', ctypes.c_uint64),
        ('sparseAddressSpaceSize', ctypes.c_uint64),
        ('maxBoundDescriptorSets', ctypes.c_uint32),
        ('maxPerStageDescriptorSamplers', ctypes.c_uint32),
        ('maxPerStageDescriptorUniformBuffers', ctypes.c_uint32),
        ('maxPerStageDescriptorStorageBuffers', ctypes.c_uint32),
        ('maxPerStageDescriptorSampledImages', ctypes.c_uint32),
        ('maxPerStageDescriptorStorageImages', ctypes.c_uint32),
        ('maxPerStageDescriptorInputAttachments', ctypes.c_uint32),
        ('maxPerStageResources', ctypes.c_uint32),
        ('maxDescriptorSetSamplers', ctypes.c_uint32),
        ('maxDescriptorSetUniformBuffers', ctypes.c_uint32),
        ('maxDescriptorSetUniformBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetStorageBuffers', ctypes.c_uint32),
        ('maxDescriptorSetStorageBuffersDynamic', ctypes.c_uint32),
        ('maxDescriptorSetSampledImages', ctypes.c_uint32),
        ('maxDescriptorSetStorageImages', ctypes.c_uint32),
        ('maxDescriptorSetInputAttachments', ctypes.c_uint32),
        ('maxVertexInputAttributes', ctypes.c_uint32),
        ('maxVertexInputBindings', ctypes.c_uint32),
        ('maxVertexInputAttributeOffset', ctypes.c_uint32),
        ('maxVertexInputBindingStride', ctypes.c_uint32),
        ('maxVertexOutputComponents', ctypes.c_uint32),
        ('maxTessellationGenerationLevel', ctypes.c_uint32),
        ('maxTessellationPatchSize', ctypes.c_uint32),
        ('maxTessellationControlPerVertexInputComponents', ctypes.c_uint32),
        ('maxTessellationControlPerVertexOutputComponents', ctypes.c_uint32),
        ('maxTessellationControlPerPatchOutputComponents', ctypes.c_uint32),
        ('maxTessellationControlTotalOutputComponents', ctypes.c_uint32),
        ('maxTessellationEvaluationInputComponents', ctypes.c_uint32),
        ('maxTessellationEvaluationOutputComponents', ctypes.c_uint32),
        ('maxGeometryShaderInvocations', ctypes.c_uint32),
        ('maxGeometryInputComponents', ctypes.c_uint32),
        ('maxGeometryOutputComponents', ctypes.c_uint32),
        ('maxGeometryOutputVertices', ctypes.c_uint32),
        ('maxGeometryTotalOutputComponents', ctypes.c_uint32),
        ('maxFragmentInputComponents', ctypes.c_uint32),
        ('maxFragmentOutputAttachments', ctypes.c_uint32),
        ('maxFragmentDualSrcAttachments', ctypes.c_uint32),
        ('maxFragmentCombinedOutputResources', ctypes.c_uint32),
        ('maxComputeSharedMemorySize', ctypes.c_uint32),
        ('maxComputeWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxComputeWorkGroupInvocations', ctypes.c_uint32),
        ('maxComputeWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('subPixelPrecisionBits', ctypes.c_uint32),
        ('subTexelPrecisionBits', ctypes.c_uint32),
        ('mipmapPrecisionBits', ctypes.c_uint32),
        ('maxDrawIndexedIndexValue', ctypes.c_uint32),
        ('maxDrawIndirectCount', ctypes.c_uint32),
        ('maxSamplerLodBias', ctypes.c_float),
        ('maxSamplerAnisotropy', ctypes.c_float),
        ('maxViewports', ctypes.c_uint32),
        ('maxViewportDimensions', ctypes.ARRAY(ctypes.c_uint32, 2)),
        ('viewportBoundsRange', ctypes.ARRAY(ctypes.c_float, 2)),
        ('viewportSubPixelBits', ctypes.c_uint32),
        ('minMemoryMapAlignment', ctypes.c_size_t),
        ('minTexelBufferOffsetAlignment', ctypes.c_uint64),
        ('minUniformBufferOffsetAlignment', ctypes.c_uint64),
        ('minStorageBufferOffsetAlignment', ctypes.c_uint64),
        ('minTexelOffset', ctypes.c_int32),
        ('maxTexelOffset', ctypes.c_uint32),
        ('minTexelGatherOffset', ctypes.c_int32),
        ('maxTexelGatherOffset', ctypes.c_uint32),
        ('minInterpolationOffset', ctypes.c_float),
        ('maxInterpolationOffset', ctypes.c_float),
        ('subPixelInterpolationOffsetBits', ctypes.c_uint32),
        ('maxFramebufferWidth', ctypes.c_uint32),
        ('maxFramebufferHeight', ctypes.c_uint32),
        ('maxFramebufferLayers', ctypes.c_uint32),
        ('framebufferColorSampleCounts', ctypes.c_uint32),
        ('framebufferDepthSampleCounts', ctypes.c_uint32),
        ('framebufferStencilSampleCounts', ctypes.c_uint32),
        ('framebufferNoAttachmentsSampleCounts', ctypes.c_uint32),
        ('maxColorAttachments', ctypes.c_uint32),
        ('sampledImageColorSampleCounts', ctypes.c_uint32),
        ('sampledImageIntegerSampleCounts', ctypes.c_uint32),
        ('sampledImageDepthSampleCounts', ctypes.c_uint32),
        ('sampledImageStencilSampleCounts', ctypes.c_uint32),
        ('storageImageSampleCounts', ctypes.c_uint32),
        ('maxSampleMaskWords', ctypes.c_uint32),
        ('timestampComputeAndGraphics', ctypes.c_uint32),
        ('timestampPeriod', ctypes.c_float),
        ('maxClipDistances', ctypes.c_uint32),
        ('maxCullDistances', ctypes.c_uint32),
        ('maxCombinedClipAndCullDistances', ctypes.c_uint32),
        ('discreteQueuePriorities', ctypes.c_uint32),
        ('pointSizeRange', ctypes.ARRAY(ctypes.c_float, 2)),
        ('lineWidthRange', ctypes.ARRAY(ctypes.c_float, 2)),
        ('pointSizeGranularity', ctypes.c_float),
        ('lineWidthGranularity', ctypes.c_float),
        ('strictLines', ctypes.c_uint32),
        ('standardSampleLocations', ctypes.c_uint32),
        ('optimalBufferCopyOffsetAlignment', ctypes.c_uint64),
        ('optimalBufferCopyRowPitchAlignment', ctypes.c_uint64),
        ('nonCoherentAtomSize', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceLimits
