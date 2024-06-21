import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineCacheCreateInfo import CType as VkPipelineCacheCreateInfo
from .VkPipelinePoolSize import CType as VkPipelinePoolSize

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pipelineCacheCreateInfoCount', ctypes.c_uint32),
    ('pPipelineCacheCreateInfos', ctypes.POINTER(VkPipelineCacheCreateInfo)),
    ('pipelinePoolSizeCount', ctypes.c_uint32),
    ('pPipelinePoolSizes', ctypes.POINTER(VkPipelinePoolSize)),
    ('semaphoreRequestCount', ctypes.c_uint32),
    ('commandBufferRequestCount', ctypes.c_uint32),
    ('fenceRequestCount', ctypes.c_uint32),
    ('deviceMemoryRequestCount', ctypes.c_uint32),
    ('bufferRequestCount', ctypes.c_uint32),
    ('imageRequestCount', ctypes.c_uint32),
    ('eventRequestCount', ctypes.c_uint32),
    ('queryPoolRequestCount', ctypes.c_uint32),
    ('bufferViewRequestCount', ctypes.c_uint32),
    ('imageViewRequestCount', ctypes.c_uint32),
    ('layeredImageViewRequestCount', ctypes.c_uint32),
    ('pipelineCacheRequestCount', ctypes.c_uint32),
    ('pipelineLayoutRequestCount', ctypes.c_uint32),
    ('renderPassRequestCount', ctypes.c_uint32),
    ('graphicsPipelineRequestCount', ctypes.c_uint32),
    ('computePipelineRequestCount', ctypes.c_uint32),
    ('descriptorSetLayoutRequestCount', ctypes.c_uint32),
    ('samplerRequestCount', ctypes.c_uint32),
    ('descriptorPoolRequestCount', ctypes.c_uint32),
    ('descriptorSetRequestCount', ctypes.c_uint32),
    ('framebufferRequestCount', ctypes.c_uint32),
    ('commandPoolRequestCount', ctypes.c_uint32),
    ('samplerYcbcrConversionRequestCount', ctypes.c_uint32),
    ('surfaceRequestCount', ctypes.c_uint32),
    ('swapchainRequestCount', ctypes.c_uint32),
    ('displayModeRequestCount', ctypes.c_uint32),
    ('subpassDescriptionRequestCount', ctypes.c_uint32),
    ('attachmentDescriptionRequestCount', ctypes.c_uint32),
    ('descriptorSetLayoutBindingRequestCount', ctypes.c_uint32),
    ('descriptorSetLayoutBindingLimit', ctypes.c_uint32),
    ('maxImageViewMipLevels', ctypes.c_uint32),
    ('maxImageViewArrayLayers', ctypes.c_uint32),
    ('maxLayeredImageViewMipLevels', ctypes.c_uint32),
    ('maxOcclusionQueriesPerPool', ctypes.c_uint32),
    ('maxPipelineStatisticsQueriesPerPool', ctypes.c_uint32),
    ('maxTimestampQueriesPerPool', ctypes.c_uint32),
    ('maxImmutableSamplersPerDescriptorSetLayout', ctypes.c_uint32),
]
