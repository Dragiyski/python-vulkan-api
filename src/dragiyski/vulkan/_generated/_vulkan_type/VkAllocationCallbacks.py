import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkAllocationFunction, vkFreeFunction, vkInternalAllocationNotification, vkInternalFreeNotification, vkReallocationFunction

CType._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', vkAllocationFunction),
    ('pfnReallocation', vkReallocationFunction),
    ('pfnFree', vkFreeFunction),
    ('pfnInternalAllocation', vkInternalAllocationNotification),
    ('pfnInternalFree', vkInternalFreeNotification),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkAllocateMemory',
        'vkCreateAccelerationStructureKHR',
        'vkCreateAccelerationStructureNV',
        'vkCreateAndroidSurfaceKHR',
        'vkCreateBuffer',
        'vkCreateBufferCollectionFUCHSIA',
        'vkCreateBufferView',
        'vkCreateCommandPool',
        'vkCreateComputePipelines',
        'vkCreateCuFunctionNVX',
        'vkCreateCuModuleNVX',
        'vkCreateCudaFunctionNV',
        'vkCreateCudaModuleNV',
        'vkCreateDebugReportCallbackEXT',
        'vkCreateDebugUtilsMessengerEXT',
        'vkCreateDeferredOperationKHR',
        'vkCreateDescriptorPool',
        'vkCreateDescriptorSetLayout',
        'vkCreateDescriptorUpdateTemplate',
        'vkCreateDevice',
        'vkCreateDirectFBSurfaceEXT',
        'vkCreateDisplayModeKHR',
        'vkCreateDisplayPlaneSurfaceKHR',
        'vkCreateEvent',
        'vkCreateExecutionGraphPipelinesAMDX',
        'vkCreateFence',
        'vkCreateFramebuffer',
        'vkCreateGraphicsPipelines',
        'vkCreateHeadlessSurfaceEXT',
        'vkCreateIOSSurfaceMVK',
        'vkCreateImage',
        'vkCreateImagePipeSurfaceFUCHSIA',
        'vkCreateImageView',
        'vkCreateIndirectCommandsLayoutNV',
        'vkCreateInstance',
        'vkCreateMacOSSurfaceMVK',
        'vkCreateMetalSurfaceEXT',
        'vkCreateMicromapEXT',
        'vkCreateOpticalFlowSessionNV',
        'vkCreatePipelineCache',
        'vkCreatePipelineLayout',
        'vkCreatePrivateDataSlot',
        'vkCreateQueryPool',
        'vkCreateRayTracingPipelinesKHR',
        'vkCreateRayTracingPipelinesNV',
        'vkCreateRenderPass',
        'vkCreateRenderPass2',
        'vkCreateSampler',
        'vkCreateSamplerYcbcrConversion',
        'vkCreateScreenSurfaceQNX',
        'vkCreateSemaphore',
        'vkCreateSemaphoreSciSyncPoolNV',
        'vkCreateShaderModule',
        'vkCreateShadersEXT',
        'vkCreateSharedSwapchainsKHR',
        'vkCreateStreamDescriptorSurfaceGGP',
        'vkCreateSwapchainKHR',
        'vkCreateValidationCacheEXT',
        'vkCreateViSurfaceNN',
        'vkCreateVideoSessionKHR',
        'vkCreateVideoSessionParametersKHR',
        'vkCreateWaylandSurfaceKHR',
        'vkCreateWin32SurfaceKHR',
        'vkCreateXcbSurfaceKHR',
        'vkCreateXlibSurfaceKHR',
        'vkDestroyAccelerationStructureKHR',
        'vkDestroyAccelerationStructureNV',
        'vkDestroyBuffer',
        'vkDestroyBufferCollectionFUCHSIA',
        'vkDestroyBufferView',
        'vkDestroyCommandPool',
        'vkDestroyCuFunctionNVX',
        'vkDestroyCuModuleNVX',
        'vkDestroyCudaFunctionNV',
        'vkDestroyCudaModuleNV',
        'vkDestroyDebugReportCallbackEXT',
        'vkDestroyDebugUtilsMessengerEXT',
        'vkDestroyDeferredOperationKHR',
        'vkDestroyDescriptorPool',
        'vkDestroyDescriptorSetLayout',
        'vkDestroyDescriptorUpdateTemplate',
        'vkDestroyDevice',
        'vkDestroyEvent',
        'vkDestroyFence',
        'vkDestroyFramebuffer',
        'vkDestroyImage',
        'vkDestroyImageView',
        'vkDestroyIndirectCommandsLayoutNV',
        'vkDestroyInstance',
        'vkDestroyMicromapEXT',
        'vkDestroyOpticalFlowSessionNV',
        'vkDestroyPipeline',
        'vkDestroyPipelineCache',
        'vkDestroyPipelineLayout',
        'vkDestroyPrivateDataSlot',
        'vkDestroyQueryPool',
        'vkDestroyRenderPass',
        'vkDestroySampler',
        'vkDestroySamplerYcbcrConversion',
        'vkDestroySemaphore',
        'vkDestroySemaphoreSciSyncPoolNV',
        'vkDestroyShaderEXT',
        'vkDestroyShaderModule',
        'vkDestroySurfaceKHR',
        'vkDestroySwapchainKHR',
        'vkDestroyValidationCacheEXT',
        'vkDestroyVideoSessionKHR',
        'vkDestroyVideoSessionParametersKHR',
        'vkFreeMemory',
        'vkRegisterDeviceEventEXT',
        'vkRegisterDisplayEventEXT',
    },
    'output_of': set(),
    'member_map': {
        'pUserData': {'python_name': ['p', 'user', 'data']},
        'pfnAllocation': {'python_name': ['pfn', 'allocation']},
        'pfnReallocation': {'python_name': ['pfn', 'reallocation']},
        'pfnFree': {'python_name': ['pfn', 'free']},
        'pfnInternalAllocation': {'python_name': ['pfn', 'internal', 'allocation']},
        'pfnInternalFree': {'python_name': ['pfn', 'internal', 'free']},
    }
}
