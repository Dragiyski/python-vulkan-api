import ctypes

class VkAllocationCallbacks(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
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
    }
    _output_of_ = set()
    _python_name_ = {
        'pUserData': 'user_data',
        'pfnAllocation': 'pfn_allocation',
        'pfnReallocation': 'pfn_reallocation',
        'pfnFree': 'pfn_free',
        'pfnInternalAllocation': 'pfn_internal_allocation',
        'pfnInternalFree': 'pfn_internal_free',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .._vulkan_callback.vkAllocationFunction import vkAllocationFunction
from .._vulkan_callback.vkFreeFunction import vkFreeFunction
from .._vulkan_callback.vkInternalAllocationNotification import vkInternalAllocationNotification
from .._vulkan_callback.vkInternalFreeNotification import vkInternalFreeNotification
from .._vulkan_callback.vkReallocationFunction import vkReallocationFunction

VkAllocationCallbacks._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', vkAllocationFunction),
    ('pfnReallocation', vkReallocationFunction),
    ('pfnFree', vkFreeFunction),
    ('pfnInternalAllocation', vkInternalAllocationNotification),
    ('pfnInternalFree', vkInternalFreeNotification),
]

VkAllocationCallbacks._type_ = {
    'pUserData': ctypes.c_void_p,
    'pfnAllocation': vkAllocationFunction,
    'pfnReallocation': vkReallocationFunction,
    'pfnFree': vkFreeFunction,
    'pfnInternalAllocation': vkInternalAllocationNotification,
    'pfnInternalFree': vkInternalFreeNotification,
}
