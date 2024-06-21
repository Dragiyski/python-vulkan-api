import ctypes

class CType(ctypes.Structure):
    pass

from .VkConformanceVersion import CType as VkConformanceVersion

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
    ('denormBehaviorIndependence', ctypes.c_int),
    ('roundingModeIndependence', ctypes.c_int),
    ('shaderSignedZeroInfNanPreserveFloat16', ctypes.c_uint32),
    ('shaderSignedZeroInfNanPreserveFloat32', ctypes.c_uint32),
    ('shaderSignedZeroInfNanPreserveFloat64', ctypes.c_uint32),
    ('shaderDenormPreserveFloat16', ctypes.c_uint32),
    ('shaderDenormPreserveFloat32', ctypes.c_uint32),
    ('shaderDenormPreserveFloat64', ctypes.c_uint32),
    ('shaderDenormFlushToZeroFloat16', ctypes.c_uint32),
    ('shaderDenormFlushToZeroFloat32', ctypes.c_uint32),
    ('shaderDenormFlushToZeroFloat64', ctypes.c_uint32),
    ('shaderRoundingModeRTEFloat16', ctypes.c_uint32),
    ('shaderRoundingModeRTEFloat32', ctypes.c_uint32),
    ('shaderRoundingModeRTEFloat64', ctypes.c_uint32),
    ('shaderRoundingModeRTZFloat16', ctypes.c_uint32),
    ('shaderRoundingModeRTZFloat32', ctypes.c_uint32),
    ('shaderRoundingModeRTZFloat64', ctypes.c_uint32),
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
    ('supportedDepthResolveModes', ctypes.c_uint32),
    ('supportedStencilResolveModes', ctypes.c_uint32),
    ('independentResolveNone', ctypes.c_uint32),
    ('independentResolve', ctypes.c_uint32),
    ('filterMinmaxSingleComponentFormats', ctypes.c_uint32),
    ('filterMinmaxImageComponentMapping', ctypes.c_uint32),
    ('maxTimelineSemaphoreValueDifference', ctypes.c_uint64),
    ('framebufferIntegerColorSampleCounts', ctypes.c_uint32),
]
