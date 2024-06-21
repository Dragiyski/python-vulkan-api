import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceNoDynamicHostAllocations', ctypes.c_uint32),
        ('deviceDestroyFreesMemory', ctypes.c_uint32),
        ('commandPoolMultipleCommandBuffersRecording', ctypes.c_uint32),
        ('commandPoolResetCommandBuffer', ctypes.c_uint32),
        ('commandBufferSimultaneousUse', ctypes.c_uint32),
        ('secondaryCommandBufferNullOrImagelessFramebuffer', ctypes.c_uint32),
        ('recycleDescriptorSetMemory', ctypes.c_uint32),
        ('recyclePipelineMemory', ctypes.c_uint32),
        ('maxRenderPassSubpasses', ctypes.c_uint32),
        ('maxRenderPassDependencies', ctypes.c_uint32),
        ('maxSubpassInputAttachments', ctypes.c_uint32),
        ('maxSubpassPreserveAttachments', ctypes.c_uint32),
        ('maxFramebufferAttachments', ctypes.c_uint32),
        ('maxDescriptorSetLayoutBindings', ctypes.c_uint32),
        ('maxQueryFaultCount', ctypes.c_uint32),
        ('maxCallbackFaultCount', ctypes.c_uint32),
        ('maxCommandPoolCommandBuffers', ctypes.c_uint32),
        ('maxCommandBufferSize', ctypes.c_uint64),
    ]
