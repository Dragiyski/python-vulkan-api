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

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_SC_1_0_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceNoDynamicHostAllocations': {'python_name': ['device', 'no', 'dynamic', 'host', 'allocations']},
        'deviceDestroyFreesMemory': {'python_name': ['device', 'destroy', 'frees', 'memory']},
        'commandPoolMultipleCommandBuffersRecording': {'python_name': ['command', 'pool', 'multiple', 'command', 'buffers', 'recording']},
        'commandPoolResetCommandBuffer': {'python_name': ['command', 'pool', 'reset', 'command', 'buffer']},
        'commandBufferSimultaneousUse': {'python_name': ['command', 'buffer', 'simultaneous', 'use']},
        'secondaryCommandBufferNullOrImagelessFramebuffer': {'python_name': ['secondary', 'command', 'buffer', 'null', 'or', 'imageless', 'framebuffer']},
        'recycleDescriptorSetMemory': {'python_name': ['recycle', 'descriptor', 'set', 'memory']},
        'recyclePipelineMemory': {'python_name': ['recycle', 'pipeline', 'memory']},
        'maxRenderPassSubpasses': {'python_name': ['max', 'render', 'pass', 'subpasses']},
        'maxRenderPassDependencies': {'python_name': ['max', 'render', 'pass', 'dependencies']},
        'maxSubpassInputAttachments': {'python_name': ['max', 'subpass', 'input', 'attachments']},
        'maxSubpassPreserveAttachments': {'python_name': ['max', 'subpass', 'preserve', 'attachments']},
        'maxFramebufferAttachments': {'python_name': ['max', 'framebuffer', 'attachments']},
        'maxDescriptorSetLayoutBindings': {'python_name': ['max', 'descriptor', 'set', 'layout', 'bindings']},
        'maxQueryFaultCount': {'python_name': ['max', 'query', 'fault', 'count']},
        'maxCallbackFaultCount': {'python_name': ['max', 'callback', 'fault', 'count']},
        'maxCommandPoolCommandBuffers': {'python_name': ['max', 'command', 'pool', 'command', 'buffers']},
        'maxCommandBufferSize': {'python_name': ['max', 'command', 'buffer', 'size']},
    }
}
