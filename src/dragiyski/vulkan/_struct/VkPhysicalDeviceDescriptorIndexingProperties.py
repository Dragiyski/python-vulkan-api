import ctypes, sys

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

sys.modules[__name__] = VkPhysicalDeviceDescriptorIndexingProperties
