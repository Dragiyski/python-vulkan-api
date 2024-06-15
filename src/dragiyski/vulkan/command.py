import ctypes
from ._vulkan_base import VKAPI_PTR, VKAPI_CALL
from ._struct import VkPrivateDataSlotCreateInfo, VkBindBufferMemoryInfo, VkDescriptorSetBindingReferenceVALVE, VkAccelerationStructureBuildRangeInfoKHR, VkStreamDescriptorSurfaceCreateInfoGGP, VkCheckpointDataNV, VkCopyBufferToImageInfo2, VkSemaphoreGetWin32HandleInfoKHR, VkImportFenceSciSyncInfoNV, VkSetDescriptorBufferOffsetsInfoEXT, VkMicromapCreateInfoEXT, VkCuLaunchInfoNVX, VkInitializePerformanceApiInfoINTEL, VkExportMetalObjectsInfoEXT, VkPhysicalDeviceExternalBufferInfo, VkImageSparseMemoryRequirementsInfo2, VkPhysicalDeviceFragmentShadingRateKHR, VkGraphicsPipelineCreateInfo, VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR, VkPhysicalDeviceSurfaceInfo2KHR, VkBlitImageInfo2, VkVertexInputBindingDescription2EXT, VkAccelerationStructureMemoryRequirementsInfoNV, VkPhysicalDeviceMemoryProperties2, VkVideoEncodeSessionParametersFeedbackInfoKHR, VkDescriptorPoolCreateInfo, VkGeneratedCommandsMemoryRequirementsInfoNV, VkVertexInputAttributeDescription2EXT, VkSubmitInfo, VkCheckpointData2NV, VkDescriptorSetLayoutHostMappingInfoVALVE, VkDebugUtilsLabelEXT, VkPhysicalDeviceGroupProperties, VkImportSemaphoreSciSyncInfoNV, VkRenderingInputAttachmentIndexInfoKHR, VkImageCreateInfo, VkCalibratedTimestampInfoKHR, VkAccelerationStructureDeviceAddressInfoKHR, VkOpticalFlowImageFormatInfoNV, VkInstanceCreateInfo, VkAccelerationStructureCreateInfoNV, VkSubmitInfo2, VkPushDescriptorSetInfoKHR, VkExtensionProperties, VkDependencyInfo, VkCudaLaunchInfoNV, VkImageResolve, VkDescriptorBufferBindingInfoEXT, VkViewport, VkWaylandSurfaceCreateInfoKHR, VkImageViewCreateInfo, VkBufferDeviceAddressInfo, VkDisplayPlaneCapabilitiesKHR, VkLatencySleepModeInfoNV, VkPhysicalDeviceFeatures2, VkDisplaySurfaceCreateInfoKHR, VkCopyMemoryToMicromapInfoEXT, VkMemorySciBufPropertiesNV, VkAccelerationStructureInfoNV, VkDebugMarkerObjectTagInfoEXT, VkPipelineIndirectDeviceAddressInfoNV, VkCopyMemoryToAccelerationStructureInfoKHR, VkValidationCacheCreateInfoEXT, VkVideoSessionParametersUpdateInfoKHR, VkCopyImageToImageInfoEXT, VkAccelerationStructureCreateInfoKHR, VkAccelerationStructureBuildGeometryInfoKHR, VkViewportWScalingNV, VkIOSSurfaceCreateInfoMVK, VkVideoEncodeSessionParametersGetInfoKHR, VkConditionalRenderingBeginInfoEXT, VkScreenSurfaceCreateInfoQNX, VkHeadlessSurfaceCreateInfoEXT, VkImageCopy, VkFenceGetWin32HandleInfoKHR, VkPhysicalDeviceProperties, VkDisplayEventInfoEXT, VkSetLatencyMarkerInfoNV, VkFaultData, VkDescriptorUpdateTemplateCreateInfo, VkPerformanceConfigurationAcquireInfoINTEL, VkCopyBufferInfo2, VkExternalSemaphoreProperties, VkPerformanceValueINTEL, VkCommandPoolMemoryConsumption, VkMemoryGetAndroidHardwareBufferInfoANDROID, VkImageSubresource2KHR, VkDebugUtilsObjectTagInfoEXT, VkMemoryRequirements, VkPerformanceOverrideInfoINTEL, VkColorBlendEquationEXT, VkSurfaceCapabilitiesKHR, VkVideoEncodeInfoKHR, VkVideoCapabilitiesKHR, VkVideoDecodeInfoKHR, VkMacOSSurfaceCreateInfoMVK, VkDescriptorSetLayoutCreateInfo, VkDebugUtilsMessengerCreateInfoEXT, VkDebugUtilsObjectNameInfoEXT, VkImagePipeSurfaceCreateInfoFUCHSIA, VkSamplerCaptureDescriptorDataInfoEXT, VkImageFormatProperties2, VkImageBlit, VkHdrMetadataEXT, VkFramebufferCreateInfo, VkAcquireNextImageInfoKHR, VkMemoryZirconHandlePropertiesFUCHSIA, VkSparseImageMemoryRequirements2, VkPhysicalDeviceImageFormatInfo2, VkDeviceGroupPresentCapabilitiesKHR, VkMemoryGetRemoteAddressInfoNV, VkClearRect, VkOpticalFlowExecuteInfoNV, VkBindImageMemoryInfo, VkSurfaceCapabilities2EXT, VkSampleLocationsInfoEXT, VkBufferConstraintsInfoFUCHSIA, VkEventCreateInfo, VkDisplayPlaneCapabilities2KHR, VkDeviceCreateInfo, VkPhysicalDeviceExternalFenceInfo, VkColorBlendAdvancedEXT, VkDisplayModeCreateInfoKHR, VkBufferMemoryBarrier, VkCopyAccelerationStructureToMemoryInfoKHR, VkViSurfaceCreateInfoNN, VkCopyMicromapInfoEXT, VkSemaphoreCreateInfo, VkVideoEncodeQualityLevelPropertiesKHR, VkPipelineLayoutCreateInfo, VkVideoEndCodingInfoKHR, VkStridedDeviceAddressRegionKHR, VkSubpassBeginInfo, VkPerformanceCounterKHR, VkImageSubresourceLayers, VkDeviceBufferMemoryRequirements, VkBindAccelerationStructureMemoryInfoNV, VkImageViewAddressPropertiesNVX, VkPhysicalDeviceProperties2, VkImageConstraintsInfoFUCHSIA, VkImageMemoryBarrier, VkDecompressMemoryRegionNV, VkPerformanceCounterDescriptionKHR, VkDisplayProperties2KHR, VkBufferCollectionPropertiesFUCHSIA, VkSemaphoreWaitInfo, VkLatencySleepInfoNV, VkScreenBufferPropertiesQNX, VkAccelerationStructureCaptureDescriptorDataInfoEXT, VkDeviceImageMemoryRequirements, VkImageSubresourceRange, VkPipelineExecutableStatisticKHR, VkFenceCreateInfo, VkRenderingAttachmentLocationInfoKHR, VkImageSubresource, VkRenderPassCreateInfo2, VkQueryPoolPerformanceCreateInfoKHR, VkPipelineExecutableInternalRepresentationKHR, VkDebugMarkerMarkerInfoEXT, VkMemoryFdPropertiesKHR, VkDeviceEventInfoEXT, VkDisplayPlanePropertiesKHR, VkAccelerationStructureBuildSizesInfoKHR, VkImportSemaphoreFdInfoKHR, VkSwapchainCreateInfoKHR, VkPerformanceMarkerInfoINTEL, VkDeviceQueueInfo2, VkPresentInfoKHR, VkBindDescriptorBufferEmbeddedSamplersInfoEXT, VkQueueFamilyProperties2, VkRayTracingPipelineCreateInfoKHR, VkPhysicalDeviceMemoryProperties, VkDisplayPlaneProperties2KHR, VkMemoryAllocateInfo, VkSparseImageFormatProperties, VkPipelineExecutablePropertiesKHR, VkClearDepthStencilValue, VkBindVideoSessionMemoryInfoKHR, VkCooperativeMatrixPropertiesKHR, VkCopyImageToMemoryInfoEXT, VkShaderModuleIdentifierEXT, VkDeviceMemoryOpaqueCaptureAddressInfo, VkMemoryRequirements2, VkIndirectCommandsLayoutCreateInfoNV, VkBindDescriptorSetsInfoKHR, VkQueueFamilyProperties, VkMemoryGetWin32HandleInfoKHR, VkImportSemaphoreWin32HandleInfoKHR, VkMultiDrawIndexedInfoEXT, VkImageViewCaptureDescriptorDataInfoEXT, VkMemoryGetSciBufInfoNV, VkPhysicalDeviceToolProperties, VkBufferImageCopy, VkDeviceImageSubresourceInfoKHR, VkRayTracingPipelineCreateInfoNV, VkVideoSessionParametersCreateInfoKHR, VkMemoryGetZirconHandleInfoFUCHSIA, VkDescriptorSetAllocateInfo, VkReleaseSwapchainImagesInfoEXT, VkCopyMemoryToImageInfoEXT, VkCudaModuleCreateInfoNV, VkBufferCreateInfo, VkBindSparseInfo, VkImageDrmFormatModifierPropertiesEXT, VkPerformanceStreamMarkerInfoINTEL, VkSemaphoreGetSciSyncInfoNV, VkImportFenceFdInfoKHR, VkBufferViewCreateInfo, VkPhysicalDeviceFeatures, VkAndroidSurfaceCreateInfoKHR, VkCopyImageInfo2, VkSurfaceCapabilities2KHR, VkVideoFormatPropertiesKHR, VkPhysicalDeviceSparseImageFormatInfo2, VkExternalBufferProperties, VkExecutionGraphPipelineCreateInfoAMDX, VkClearColorValue, VkQueryPoolCreateInfo, VkMetalSurfaceCreateInfoEXT, VkPushConstantsInfoKHR, VkMicromapBuildSizesInfoEXT, VkSemaphoreSignalInfo, VkDescriptorGetInfoEXT, VkSamplerCreateInfo, VkShadingRatePaletteNV, VkDisplayModeProperties2KHR, VkRect2D, VkSubpassEndInfo, VkViewportSwizzleNV, VkMemoryWin32HandlePropertiesKHR, VkVideoProfileInfoKHR, VkCommandBufferBeginInfo, VkExecutionGraphPipelineScratchSizeAMDX, VkPastPresentationTimingGOOGLE, VkImageCaptureDescriptorDataInfoEXT, VkSubresourceLayout2KHR, VkExternalFenceProperties, VkImageFormatProperties, VkCoarseSampleOrderCustomNV, VkImageMemoryRequirementsInfo2, VkFramebufferMixedSamplesCombinationNV, VkPipelineShaderStageNodeCreateInfoAMDX, VkDescriptorSetLayoutSupport, VkShaderModuleCreateInfo, VkImportSemaphoreZirconHandleInfoFUCHSIA, VkImportFenceWin32HandleInfoKHR, VkFenceGetFdInfoKHR, VkBaseOutStructure, VkFormatProperties, VkVideoCodingControlInfoKHR, VkHostImageLayoutTransitionInfoEXT, VkDebugReportCallbackCreateInfoEXT, VkDeviceFaultCountsEXT, VkDebugMarkerObjectNameInfoEXT, VkDebugUtilsMessengerCallbackDataEXT, VkSparseImageFormatProperties2, VkAcquireProfilingLockInfoKHR, VkCudaFunctionCreateInfoNV, VkOpticalFlowSessionCreateInfoNV, VkBufferMemoryRequirementsInfo2, VkPipelineCacheCreateInfo, VkCopyMicromapToMemoryInfoEXT, VkSamplerYcbcrConversionCreateInfo, VkVideoSessionMemoryRequirementsKHR, VkPipelineInfoKHR, VkComputePipelineCreateInfo, VkSciSyncAttributesInfoNV, VkCuModuleCreateInfoNVX, VkBufferCopy, VkImageViewHandleInfoNVX, VkSurfaceFormatKHR, VkDisplayPropertiesKHR, VkCuFunctionCreateInfoNVX, VkDirectFBSurfaceCreateInfoEXT, VkPhysicalDeviceVideoFormatInfoKHR, VkXcbSurfaceCreateInfoKHR, VkDisplayPlaneInfo2KHR, VkSemaphoreGetFdInfoKHR, VkDisplayModePropertiesKHR, VkPhysicalDeviceExternalSemaphoreInfo, VkClearAttachment, VkGeneratedCommandsInfoNV, VkCopyImageToBufferInfo2, VkAllocationCallbacks, VkRenderPassCreateInfo, VkXlibSurfaceCreateInfoKHR, VkFenceGetSciSyncInfoNV, VkSemaphoreSciSyncPoolCreateInfoNV, VkMicromapVersionInfoEXT, VkOpticalFlowImageFormatPropertiesNV, VkPushDescriptorSetWithTemplateInfoKHR, VkAccelerationStructureVersionInfoKHR, VkMultiDrawInfoEXT, VkCopyDescriptorSet, VkMultisamplePropertiesEXT, VkCopyAccelerationStructureInfoKHR, VkSemaphoreGetZirconHandleInfoFUCHSIA, VkRefreshCycleDurationGOOGLE, VkMemoryGetFdInfoKHR, VkBufferCollectionCreateInfoFUCHSIA, VkCooperativeMatrixPropertiesNV, VkMemoryUnmapInfoKHR, VkBufferCaptureDescriptorDataInfoEXT, VkGetLatencyMarkerInfoNV, VkCommandBufferAllocateInfo, VkWin32SurfaceCreateInfoKHR, VkOutOfBandQueueTypeInfoNV, VkTilePropertiesQCOM, VkPipelineExecutableInfoKHR, VkDepthBiasInfoEXT, VkAndroidHardwareBufferPropertiesANDROID, VkMappedMemoryRange, VkDisplayPowerInfoEXT, VkRefreshObjectListKHR, VkMemoryBarrier, VkVideoBeginCodingInfoKHR, VkMicromapBuildInfoEXT, VkLayerProperties, VkMemoryMapInfoKHR, VkDeviceFaultInfoEXT, VkWriteDescriptorSet, VkSurfaceFormat2KHR, VkRenderingInfo, VkSparseImageMemoryRequirements, VkRenderingAreaInfoKHR, VkCommandPoolCreateInfo, VkMemoryHostPointerPropertiesEXT, VkExtent2D, VkDispatchGraphCountInfoAMDX, VkResolveImageInfo2, VkExternalImageFormatPropertiesNV, VkRenderPassBeginInfo, VkShaderCreateInfoEXT, VkFormatProperties2, VkSubresourceLayout, VkVideoSessionCreateInfoKHR
from ._vulkan_callback import vkVoidFunction

vkCreateInstance = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(VkInstanceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyInstance = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkEnumeratePhysicalDevices = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkGetDeviceProcAddr = VKAPI_CALL(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)
vkGetInstanceProcAddr = VKAPI_CALL(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)
vkGetPhysicalDeviceProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceProperties))
vkGetPhysicalDeviceQueueFamilyProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties))
vkGetPhysicalDeviceMemoryProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties))
vkGetPhysicalDeviceFeatures = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures))
vkGetPhysicalDeviceFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties))
vkGetPhysicalDeviceImageFormatProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkImageFormatProperties))
vkCreateDevice = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDevice = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkEnumerateInstanceVersion = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32))
vkEnumerateInstanceLayerProperties = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateInstanceExtensionProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkEnumerateDeviceLayerProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateDeviceExtensionProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkGetDeviceQueue = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkQueueSubmit = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo), ctypes.c_void_p)
vkQueueWaitIdle = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkDeviceWaitIdle = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkAllocateMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryAllocateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkFreeMemory = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkMapMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkUnmapMemory = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p)
vkFlushMappedMemoryRanges = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkInvalidateMappedMemoryRanges = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkGetDeviceMemoryCommitment = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkMemoryRequirements))
vkBindBufferMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkGetImageMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkMemoryRequirements))
vkBindImageMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkGetImageSparseMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements))
vkGetPhysicalDeviceSparseImageFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties))
vkQueueBindSparse = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindSparseInfo), ctypes.c_void_p)
vkCreateFence = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyFence = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkResetFences = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetFenceStatus = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkWaitForFences = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_uint64)
vkCreateSemaphore = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySemaphore = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkEventCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetEventStatus = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkSetEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkResetEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkCreateQueryPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetQueryPoolResults = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkResetQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCreateBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateBufferView = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyBufferView = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateImage = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetImageSubresourceLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource), ctypes.POINTER(VkSubresourceLayout))
vkCreateImageView = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyImageView = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateShaderModule = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyShaderModule = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreatePipelineCache = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineCacheCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyPipelineCache = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetPipelineCacheData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkMergePipelineCaches = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkCreateGraphicsPipelines = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkGraphicsPipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateComputePipelines = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExtent2D))
vkDestroyPipeline = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreatePipelineLayout = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyPipelineLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateSampler = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySampler = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateDescriptorSetLayout = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDescriptorSetLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateDescriptorPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDescriptorPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkResetDescriptorPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkAllocateDescriptorSets = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetAllocateInfo), ctypes.POINTER(ctypes.c_void_p))
vkFreeDescriptorSets = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkUpdateDescriptorSets = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet), ctypes.c_uint32, ctypes.POINTER(VkCopyDescriptorSet))
vkCreateFramebuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFramebufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyFramebuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateRenderPass = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyRenderPass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetRenderAreaGranularity = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExtent2D))
vkGetRenderingAreaGranularityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingAreaInfoKHR), ctypes.POINTER(VkExtent2D))
vkCreateCommandPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyCommandPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkResetCommandPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkAllocateCommandBuffers = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandBufferAllocateInfo), ctypes.POINTER(ctypes.c_void_p))
vkFreeCommandBuffers = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkBeginCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandBufferBeginInfo))
vkEndCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkResetCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdBindPipeline = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
vkCmdSetAttachmentFeedbackLoopEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetViewport = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSetScissor = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetLineWidth = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float)
vkCmdSetDepthBias = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)
vkCmdSetBlendConstants = VKAPI_CALL(None, ctypes.c_void_p, ctypes.ARRAY(ctypes.c_float, 4))
vkCmdSetDepthBounds = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)
vkCmdSetStencilCompareMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetStencilWriteMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetStencilReference = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdBindDescriptorSets = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdBindIndexBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_int)
vkCmdBindVertexBuffers = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdDraw = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexed = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)
vkCmdDrawMultiEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMultiIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawIndexedInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int32))
vkCmdDrawIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexedIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatch = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatchIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdSubpassShadingHUAWEI = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdDrawClusterHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawClusterIndirectHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdUpdatePipelineIndirectBufferNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
vkCmdCopyBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBufferCopy))
vkCmdCopyImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageCopy))
vkCmdBlitImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageBlit), ctypes.c_int)
vkCmdCopyBufferToImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyImageToBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyMemoryIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdCopyMemoryToImageIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkImageSubresourceLayers))
vkCmdUpdateBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p)
vkCmdFillBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCmdClearColorImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearColorValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdClearDepthStencilImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearDepthStencilValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdClearAttachments = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkClearAttachment), ctypes.c_uint32, ctypes.POINTER(VkClearRect))
vkCmdResolveImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageResolve))
vkCmdSetEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdResetEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWaitEvents = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdPipelineBarrier = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdBeginQuery = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdEndQuery = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdBeginConditionalRenderingEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkConditionalRenderingBeginInfoEXT))
vkCmdEndConditionalRenderingEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdResetQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdWriteTimestamp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkCmdCopyQueryPoolResults = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCmdPushConstants = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)
vkCmdBeginRenderPass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.c_int)
vkCmdNextSubpass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdEndRenderPass = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdExecuteCommands = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkCreateAndroidSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAndroidSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceDisplayPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPropertiesKHR))
vkGetPhysicalDeviceDisplayPlanePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlanePropertiesKHR))
vkGetDisplayPlaneSupportedDisplaysKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkGetDisplayModePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModePropertiesKHR))
vkCreateDisplayModeKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayModeCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetDisplayPlaneCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDisplayPlaneCapabilitiesKHR))
vkCreateDisplayPlaneSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplaySurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSharedSwapchainsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySurfaceKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetPhysicalDeviceSurfaceSupportKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkGetPhysicalDeviceSurfaceCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSurfaceCapabilitiesKHR))
vkGetPhysicalDeviceSurfaceFormatsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormatKHR))
vkGetPhysicalDeviceSurfacePresentModesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkCreateSwapchainKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySwapchainKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetSwapchainImagesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkAcquireNextImageKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkQueuePresentKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPresentInfoKHR))
vkCreateViSurfaceNN = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkViSurfaceCreateInfoNN), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateWaylandSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkWaylandSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceWaylandPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkCreateWin32SurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkWin32SurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceWin32PresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkCreateXlibSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkXlibSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceXlibPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkCreateXcbSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkXcbSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceXcbPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkCreateDirectFBSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDirectFBSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceDirectFBPresentationSupportEXT = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkCreateImagePipeSurfaceFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImagePipeSurfaceCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateStreamDescriptorSurfaceGGP = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkStreamDescriptorSurfaceCreateInfoGGP), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateScreenSurfaceQNX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkScreenSurfaceCreateInfoQNX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceScreenPresentationSupportQNX = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkCreateDebugReportCallbackEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugReportCallbackCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDebugReportCallbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDebugReportMessageEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p)
vkDebugMarkerSetObjectNameEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerObjectNameInfoEXT))
vkDebugMarkerSetObjectTagEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerObjectTagInfoEXT))
vkCmdDebugMarkerBeginEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkCmdDebugMarkerEndEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdDebugMarkerInsertEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkGetPhysicalDeviceExternalImageFormatPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkExternalImageFormatPropertiesNV))
vkGetMemoryWin32HandleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkCmdExecuteGeneratedCommandsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdPreprocessGeneratedCommandsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdBindPipelineShaderGroupNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkGetGeneratedCommandsMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
vkCreateIndirectCommandsLayoutNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIndirectCommandsLayoutCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyIndirectCommandsLayoutNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetPhysicalDeviceFeatures2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures2))
vkGetPhysicalDeviceProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceProperties2))
vkGetPhysicalDeviceFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties2))
vkGetPhysicalDeviceImageFormatProperties2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceImageFormatInfo2), ctypes.POINTER(VkImageFormatProperties2))
vkGetPhysicalDeviceQueueFamilyProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties2))
vkGetPhysicalDeviceMemoryProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties2))
vkGetPhysicalDeviceSparseImageFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSparseImageFormatInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties2))
vkCmdPushDescriptorSetKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet))
vkTrimCommandPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkGetPhysicalDeviceExternalBufferProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalBufferInfo), ctypes.POINTER(VkExternalBufferProperties))
vkGetMemoryWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkGetMemoryWin32HandlePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemoryWin32HandlePropertiesKHR))
vkGetMemoryFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetMemoryFdPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(VkMemoryFdPropertiesKHR))
vkGetMemoryZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
vkGetMemoryZirconHandlePropertiesFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryZirconHandlePropertiesFUCHSIA))
vkGetMemoryRemoteAddressNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetRemoteAddressInfoNV), ctypes.POINTER(ctypes.c_void_p))
vkGetMemorySciBufNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetSciBufInfoNV), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceExternalMemorySciBufPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemorySciBufPropertiesNV))
vkGetPhysicalDeviceSciBufAttributesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetPhysicalDeviceExternalSemaphoreProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalSemaphoreInfo), ctypes.POINTER(VkExternalSemaphoreProperties))
vkGetSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkImportSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreWin32HandleInfoKHR))
vkGetSemaphoreFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkImportSemaphoreFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreFdInfoKHR))
vkGetSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
vkImportSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreZirconHandleInfoFUCHSIA))
vkGetPhysicalDeviceExternalFenceProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalFenceInfo), ctypes.POINTER(VkExternalFenceProperties))
vkGetFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkImportFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceWin32HandleInfoKHR))
vkGetFenceFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkImportFenceFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceFdInfoKHR))
vkGetFenceSciSyncFenceNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetSciSyncInfoNV), ctypes.c_void_p)
vkGetFenceSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetSciSyncInfoNV), ctypes.c_void_p)
vkImportFenceSciSyncFenceNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceSciSyncInfoNV))
vkImportFenceSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceSciSyncInfoNV))
vkGetSemaphoreSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetSciSyncInfoNV), ctypes.c_void_p)
vkImportSemaphoreSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreSciSyncInfoNV))
vkGetPhysicalDeviceSciSyncAttributesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSciSyncAttributesInfoNV), ctypes.c_void_p)
vkCreateSemaphoreSciSyncPoolNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreSciSyncPoolCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySemaphoreSciSyncPoolNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkReleaseDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkAcquireXlibDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
vkGetRandROutputDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkAcquireWinrtDisplayNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetWinrtDisplayNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkDisplayPowerControlEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayPowerInfoEXT))
vkRegisterDeviceEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkRegisterDisplayEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetSwapchainCounterEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64))
vkGetPhysicalDeviceSurfaceCapabilities2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSurfaceCapabilities2EXT))
vkEnumeratePhysicalDeviceGroups = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceGroupProperties))
vkGetDeviceGroupPeerMemoryFeatures = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkBindBufferMemory2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindBufferMemoryInfo))
vkBindImageMemory2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindImageMemoryInfo))
vkCmdSetDeviceMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkGetDeviceGroupPresentCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceGroupPresentCapabilitiesKHR))
vkGetDeviceGroupSurfacePresentModesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkAcquireNextImage2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAcquireNextImageInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkCmdDispatchBase = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkGetPhysicalDevicePresentRectanglesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkRect2D))
vkCreateDescriptorUpdateTemplate = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorUpdateTemplateCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDescriptorUpdateTemplate = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkUpdateDescriptorSetWithTemplate = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
vkCmdPushDescriptorSetWithTemplateKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkSetHdrMetadataEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(VkHdrMetadataEXT))
vkGetSwapchainStatusKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetRefreshCycleDurationGOOGLE = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkRefreshCycleDurationGOOGLE))
vkGetPastPresentationTimingGOOGLE = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPastPresentationTimingGOOGLE))
vkCreateIOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateMacOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMacOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateMetalSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMetalSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdSetViewportWScalingNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportWScalingNV))
vkCmdSetDiscardRectangleEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetDiscardRectangleEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDiscardRectangleModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetSampleLocationsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSampleLocationsInfoEXT))
vkGetPhysicalDeviceMultisamplePropertiesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultisamplePropertiesEXT))
vkGetPhysicalDeviceSurfaceCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(VkSurfaceCapabilities2KHR))
vkGetPhysicalDeviceSurfaceFormats2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormat2KHR))
vkGetPhysicalDeviceDisplayProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayProperties2KHR))
vkGetPhysicalDeviceDisplayPlaneProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlaneProperties2KHR))
vkGetDisplayModeProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModeProperties2KHR))
vkGetDisplayPlaneCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplayPlaneInfo2KHR), ctypes.POINTER(VkDisplayPlaneCapabilities2KHR))
vkGetBufferMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBufferMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetImageMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetImageSparseMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageSparseMemoryRequirementsInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
vkGetDeviceBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceBufferMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
vkGetDeviceImageMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
vkGetDeviceImageSparseMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
vkCreateSamplerYcbcrConversion = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerYcbcrConversionCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroySamplerYcbcrConversion = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetDeviceQueue2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceQueueInfo2), ctypes.POINTER(ctypes.c_void_p))
vkCreateValidationCacheEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkValidationCacheCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyValidationCacheEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetValidationCacheDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkMergeValidationCachesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetDescriptorSetLayoutSupport = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkDescriptorSetLayoutSupport))
vkGetSwapchainGrallocUsageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int))
vkGetSwapchainGrallocUsage2ANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkAcquireImageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkQueueSignalReleaseImageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))
vkGetShaderInfoAMD = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkSetLocalDimmingAMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkGetPhysicalDeviceCalibrateableTimeDomainsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetCalibratedTimestampsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkCalibratedTimestampInfoKHR), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkSetDebugUtilsObjectNameEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT))
vkSetDebugUtilsObjectTagEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsObjectTagInfoEXT))
vkQueueBeginDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkQueueEndDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkQueueInsertDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdBeginDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdEndDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdInsertDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCreateDebugUtilsMessengerEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsMessengerCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDebugUtilsMessengerEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkSubmitDebugUtilsMessageEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT))
vkGetMemoryHostPointerPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemoryHostPointerPropertiesEXT))
vkCmdWriteBufferMarkerAMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkCreateRenderPass2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo2), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdBeginRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.POINTER(VkSubpassBeginInfo))
vkCmdNextSubpass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassBeginInfo), ctypes.POINTER(VkSubpassEndInfo))
vkCmdEndRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassEndInfo))
vkGetSemaphoreCounterValue = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkWaitSemaphores = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreWaitInfo), ctypes.c_uint64)
vkSignalSemaphore = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreSignalInfo))
vkGetAndroidHardwareBufferPropertiesANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAndroidHardwareBufferPropertiesANDROID))
vkGetMemoryAndroidHardwareBufferANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetAndroidHardwareBufferInfoANDROID), ctypes.POINTER(ctypes.c_void_p))
vkCmdDrawIndirectCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexedIndirectCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetCheckpointNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p)
vkGetQueueCheckpointDataNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointDataNV))
vkCmdBindTransformFeedbackBuffersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkCmdBeginTransformFeedbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdEndTransformFeedbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdBeginQueryIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdEndQueryIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirectByteCountEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetExclusiveScissorNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetExclusiveScissorEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdBindShadingRateImageNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkCmdSetViewportShadingRatePaletteNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkShadingRatePaletteNV))
vkCmdSetCoarseSampleOrderNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkCoarseSampleOrderCustomNV))
vkCmdDrawMeshTasksNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectCountNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectCountEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCompileDeferredNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCreateAccelerationStructureNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdBindInvocationMaskHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkDestroyAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetAccelerationStructureMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
vkBindAccelerationStructureMemoryNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindAccelerationStructureMemoryInfoNV))
vkCmdCopyAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkCmdCopyAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCopyAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCmdCopyAccelerationStructureToMemoryKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCopyAccelerationStructureToMemoryKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCmdCopyMemoryToAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCopyMemoryToAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCmdWriteAccelerationStructuresPropertiesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteAccelerationStructuresPropertiesNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdBuildAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureInfoNV), ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkWriteAccelerationStructuresPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)
vkCmdTraceRaysKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdTraceRaysNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkGetRayTracingShaderGroupHandlesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetRayTracingCaptureReplayShaderGroupHandlesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetAccelerationStructureHandleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p)
vkCreateRayTracingPipelinesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateRayTracingPipelinesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceCooperativeMatrixPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCooperativeMatrixPropertiesNV))
vkCmdTraceRaysIndirectKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint64)
vkCmdTraceRaysIndirect2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64)
vkGetDeviceAccelerationStructureCompatibilityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureVersionInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetRayTracingShaderGroupStackSizeKHR = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int)
vkCmdSetRayTracingPipelineStackSizeKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkGetImageViewHandleNVX = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkImageViewHandleInfoNVX))
vkGetImageViewAddressNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageViewAddressPropertiesNVX))
vkGetPhysicalDeviceSurfacePresentModes2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetDeviceGroupSurfacePresentModes2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32))
vkAcquireFullScreenExclusiveModeEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkReleaseFullScreenExclusiveModeEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPerformanceCounterKHR), ctypes.POINTER(VkPerformanceCounterDescriptionKHR))
vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolPerformanceCreateInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkAcquireProfilingLockKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAcquireProfilingLockInfoKHR))
vkReleaseProfilingLockKHR = VKAPI_CALL(None, ctypes.c_void_p)
vkGetImageDrmFormatModifierPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageDrmFormatModifierPropertiesEXT))
vkGetBufferOpaqueCaptureAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkGetBufferDeviceAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkCreateHeadlessSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkHeadlessSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkFramebufferMixedSamplesCombinationNV))
vkInitializePerformanceApiINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkInitializePerformanceApiInfoINTEL))
vkUninitializePerformanceApiINTEL = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdSetPerformanceMarkerINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceMarkerInfoINTEL))
vkCmdSetPerformanceStreamMarkerINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceStreamMarkerInfoINTEL))
vkCmdSetPerformanceOverrideINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceOverrideInfoINTEL))
vkAcquirePerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceConfigurationAcquireInfoINTEL), ctypes.POINTER(ctypes.c_void_p))
vkReleasePerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkQueueSetPerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetPerformanceParameterINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkPerformanceValueINTEL))
vkGetDeviceMemoryOpaqueCaptureAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkDeviceMemoryOpaqueCaptureAddressInfo))
vkGetPipelineExecutablePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutablePropertiesKHR))
vkGetPipelineExecutableStatisticsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableStatisticKHR))
vkGetPipelineExecutableInternalRepresentationsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableInternalRepresentationKHR))
vkCmdSetLineStippleKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint16)
vkGetFaultData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkFaultData))
vkGetPhysicalDeviceToolProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceToolProperties))
vkCreateAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdBuildAccelerationStructuresKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkCmdBuildAccelerationStructuresIndirectKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint32)))
vkBuildAccelerationStructuresKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkGetAccelerationStructureDeviceAddressKHR = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureDeviceAddressInfoKHR))
vkCreateDeferredOperationKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyDeferredOperationKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetDeferredOperationMaxConcurrencyKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)
vkGetDeferredOperationResultKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkDeferredOperationJoinKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetPipelineIndirectMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkMemoryRequirements2))
vkGetPipelineIndirectDeviceAddressNV = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkPipelineIndirectDeviceAddressInfoNV))
vkCmdSetCullMode = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetFrontFace = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetPrimitiveTopology = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetViewportWithCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSetScissorWithCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdBindIndexBuffer2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_int)
vkCmdBindVertexBuffers2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkCmdSetDepthTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthWriteEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthCompareOp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetDepthBoundsTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetStencilTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetStencilOp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
vkCmdSetPatchControlPointsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetRasterizerDiscardEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthBiasEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetLogicOpEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetPrimitiveRestartEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetTessellationDomainOriginEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetDepthClampEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetPolygonModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetRasterizationSamplesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetSampleMaskEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetAlphaToCoverageEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetAlphaToOneEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetLogicOpEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetColorBlendEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetColorBlendEquationEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkColorBlendEquationEXT))
vkCmdSetColorWriteMaskEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetRasterizationStreamEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetConservativeRasterizationModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetExtraPrimitiveOverestimationSizeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float)
vkCmdSetDepthClipEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetSampleLocationsEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetColorBlendAdvancedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkColorBlendAdvancedEXT))
vkCmdSetProvokingVertexModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetLineRasterizationModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetLineStippleEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthClipNegativeOneToOneEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetViewportWScalingEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetViewportSwizzleNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportSwizzleNV))
vkCmdSetCoverageToColorEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageToColorLocationNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageModulationModeNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetCoverageModulationTableEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageModulationTableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_float))
vkCmdSetShadingRateImageEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageReductionModeNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetRepresentativeFragmentTestEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCreatePrivateDataSlot = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPrivateDataSlotCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyPrivateDataSlot = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkSetPrivateData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64)
vkGetPrivateData = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkCmdCopyBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferInfo2))
vkCmdCopyImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageInfo2))
vkCmdBlitImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBlitImageInfo2))
vkCmdCopyBufferToImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferToImageInfo2))
vkCmdCopyImageToBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToBufferInfo2))
vkCmdResolveImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkResolveImageInfo2))
vkCmdRefreshObjectsKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRefreshObjectListKHR))
vkGetPhysicalDeviceRefreshableObjectTypesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkCmdSetFragmentShadingRateKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExtent2D), ctypes.ARRAY(ctypes.c_int, 2))
vkGetPhysicalDeviceFragmentShadingRatesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceFragmentShadingRateKHR))
vkCmdSetFragmentShadingRateEnumNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.ARRAY(ctypes.c_int, 2))
vkGetAccelerationStructureBuildSizesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkAccelerationStructureBuildSizesInfoKHR))
vkCmdSetVertexInputEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkVertexInputBindingDescription2EXT), ctypes.c_uint32, ctypes.POINTER(VkVertexInputAttributeDescription2EXT))
vkCmdSetColorWriteEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetEvent2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDependencyInfo))
vkCmdResetEvent2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdWaitEvents2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(VkDependencyInfo))
vkCmdPipelineBarrier2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDependencyInfo))
vkQueueSubmit2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo2), ctypes.c_void_p)
vkCmdWriteTimestamp2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteBufferMarker2AMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkGetQueueCheckpointData2NV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointData2NV))
vkCopyMemoryToImageEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToImageInfoEXT))
vkCopyImageToMemoryEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToMemoryInfoEXT))
vkCopyImageToImageEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToImageInfoEXT))
vkTransitionImageLayoutEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkHostImageLayoutTransitionInfoEXT))
vkGetCommandPoolMemoryConsumption = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCommandPoolMemoryConsumption))
vkGetPhysicalDeviceVideoCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoProfileInfoKHR), ctypes.POINTER(VkVideoCapabilitiesKHR))
vkGetPhysicalDeviceVideoFormatPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoFormatInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkVideoFormatPropertiesKHR))
vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR), ctypes.POINTER(VkVideoEncodeQualityLevelPropertiesKHR))
vkCreateVideoSessionKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyVideoSessionKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCreateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkUpdateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersUpdateInfoKHR))
vkGetEncodedVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoEncodeSessionParametersGetInfoKHR), ctypes.POINTER(VkVideoEncodeSessionParametersFeedbackInfoKHR), ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkDestroyVideoSessionParametersKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetVideoSessionMemoryRequirementsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkVideoSessionMemoryRequirementsKHR))
vkBindVideoSessionMemoryKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindVideoSessionMemoryInfoKHR))
vkCmdDecodeVideoKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoDecodeInfoKHR))
vkCmdBeginVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoBeginCodingInfoKHR))
vkCmdControlVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoCodingControlInfoKHR))
vkCmdEndVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEndCodingInfoKHR))
vkCmdEncodeVideoKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEncodeInfoKHR))
vkCmdDecompressMemoryNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDecompressMemoryRegionNV))
vkCmdDecompressMemoryIndirectCountNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCreateCuModuleNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuModuleCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCuFunctionNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuFunctionCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyCuModuleNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCuFunctionNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCmdCuLaunchKernelNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCuLaunchInfoNVX))
vkGetDescriptorSetLayoutSizeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetDescriptorSetLayoutBindingOffsetEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64))
vkGetDescriptorEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorGetInfoEXT), ctypes.c_size_t, ctypes.c_void_p)
vkCmdBindDescriptorBuffersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDescriptorBufferBindingInfoEXT))
vkCmdSetDescriptorBufferOffsetsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint64))
vkCmdBindDescriptorBufferEmbeddedSamplersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkGetBufferOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetImageOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetImageViewOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageViewCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetSamplerOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkSetDeviceMemoryPriorityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)
vkAcquireDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p)
vkGetDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkWaitForPresentKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64)
vkCreateBufferCollectionFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCollectionCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkSetBufferCollectionBufferConstraintsFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkBufferConstraintsInfoFUCHSIA))
vkSetBufferCollectionImageConstraintsFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageConstraintsInfoFUCHSIA))
vkDestroyBufferCollectionFUCHSIA = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetBufferCollectionPropertiesFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkBufferCollectionPropertiesFUCHSIA))
vkCreateCudaModuleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaModuleCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkGetCudaModuleCacheNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkCreateCudaFunctionNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaFunctionCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyCudaModuleNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCudaFunctionNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCmdCudaLaunchKernelNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCudaLaunchInfoNV))
vkCmdBeginRendering = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo))
vkCmdEndRendering = VKAPI_CALL(None, ctypes.c_void_p)
vkGetDescriptorSetLayoutHostMappingInfoVALVE = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetBindingReferenceVALVE), ctypes.POINTER(VkDescriptorSetLayoutHostMappingInfoVALVE))
vkGetDescriptorSetHostMappingVALVE = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
vkCreateMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMicromapCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdBuildMicromapsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMicromapBuildInfoEXT))
vkBuildMicromapsEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMicromapBuildInfoEXT))
vkDestroyMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkCmdCopyMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapInfoEXT))
vkCopyMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapInfoEXT))
vkCmdCopyMicromapToMemoryEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
vkCopyMicromapToMemoryEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
vkCmdCopyMemoryToMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToMicromapInfoEXT))
vkCopyMemoryToMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToMicromapInfoEXT))
vkCmdWriteMicromapsPropertiesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkWriteMicromapsPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)
vkGetDeviceMicromapCompatibilityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkMicromapVersionInfoEXT), ctypes.POINTER(ctypes.c_int))
vkGetMicromapBuildSizesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkMicromapBuildInfoEXT), ctypes.POINTER(VkMicromapBuildSizesInfoEXT))
vkGetShaderModuleIdentifierEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleIdentifierEXT))
vkGetShaderModuleCreateInfoIdentifierEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkShaderModuleIdentifierEXT))
vkGetImageSubresourceLayout2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource2KHR), ctypes.POINTER(VkSubresourceLayout2KHR))
vkGetPipelinePropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(VkBaseOutStructure))
vkExportMetalObjectsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExportMetalObjectsInfoEXT))
vkGetFramebufferTilePropertiesQCOM = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkTilePropertiesQCOM))
vkGetDynamicRenderingTilePropertiesQCOM = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo), ctypes.POINTER(VkTilePropertiesQCOM))
vkGetPhysicalDeviceOpticalFlowImageFormatsNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowImageFormatInfoNV), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkOpticalFlowImageFormatPropertiesNV))
vkCreateOpticalFlowSessionNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowSessionCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyOpticalFlowSessionNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkBindOpticalFlowSessionImageNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
vkCmdOpticalFlowExecuteNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowExecuteInfoNV))
vkGetDeviceFaultInfoEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceFaultCountsEXT), ctypes.POINTER(VkDeviceFaultInfoEXT))
vkCmdSetDepthBias2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDepthBiasInfoEXT))
vkReleaseSwapchainImagesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkReleaseSwapchainImagesInfoEXT))
vkGetDeviceImageSubresourceLayoutKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageSubresourceInfoKHR), ctypes.POINTER(VkSubresourceLayout2KHR))
vkMapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryMapInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkUnmapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryUnmapInfoKHR))
vkCreateShadersEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkShaderCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDestroyShaderEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetShaderBinaryDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkCmdBindShadersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkGetScreenBufferPropertiesQNX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkScreenBufferPropertiesQNX))
vkGetPhysicalDeviceCooperativeMatrixPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCooperativeMatrixPropertiesKHR))
vkGetExecutionGraphPipelineScratchSizeAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExecutionGraphPipelineScratchSizeAMDX))
vkGetExecutionGraphPipelineNodeIndexAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkPipelineShaderStageNodeCreateInfoAMDX), ctypes.POINTER(ctypes.c_uint32))
vkCreateExecutionGraphPipelinesAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkExecutionGraphPipelineCreateInfoAMDX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCmdInitializeGraphScratchMemoryAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64)
vkCmdDispatchGraphAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VkDispatchGraphCountInfoAMDX))
vkCmdDispatchGraphIndirectAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VkDispatchGraphCountInfoAMDX))
vkCmdDispatchGraphIndirectCountAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64)
vkCmdBindDescriptorSets2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorSetsInfoKHR))
vkCmdPushConstants2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushConstantsInfoKHR))
vkCmdPushDescriptorSet2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetInfoKHR))
vkCmdPushDescriptorSetWithTemplate2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetWithTemplateInfoKHR))
vkCmdSetDescriptorBufferOffsets2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSetDescriptorBufferOffsetsInfoEXT))
vkCmdBindDescriptorBufferEmbeddedSamplers2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorBufferEmbeddedSamplersInfoEXT))
vkSetLatencySleepModeNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkLatencySleepModeInfoNV))
vkLatencySleepNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkLatencySleepInfoNV))
vkSetLatencyMarkerNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSetLatencyMarkerInfoNV))
vkGetLatencyTimingsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkGetLatencyMarkerInfoNV))
vkQueueNotifyOutOfBandNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkOutOfBandQueueTypeInfoNV))
vkCmdSetRenderingAttachmentLocationsKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingAttachmentLocationInfoKHR))
vkCmdSetRenderingInputAttachmentIndicesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInputAttachmentIndexInfoKHR))

__all__ = [
    'vkCreateInstance',
    'vkDestroyInstance',
    'vkEnumeratePhysicalDevices',
    'vkGetDeviceProcAddr',
    'vkGetInstanceProcAddr',
    'vkGetPhysicalDeviceProperties',
    'vkGetPhysicalDeviceQueueFamilyProperties',
    'vkGetPhysicalDeviceMemoryProperties',
    'vkGetPhysicalDeviceFeatures',
    'vkGetPhysicalDeviceFormatProperties',
    'vkGetPhysicalDeviceImageFormatProperties',
    'vkCreateDevice',
    'vkDestroyDevice',
    'vkEnumerateInstanceVersion',
    'vkEnumerateInstanceLayerProperties',
    'vkEnumerateInstanceExtensionProperties',
    'vkEnumerateDeviceLayerProperties',
    'vkEnumerateDeviceExtensionProperties',
    'vkGetDeviceQueue',
    'vkQueueSubmit',
    'vkQueueWaitIdle',
    'vkDeviceWaitIdle',
    'vkAllocateMemory',
    'vkFreeMemory',
    'vkMapMemory',
    'vkUnmapMemory',
    'vkFlushMappedMemoryRanges',
    'vkInvalidateMappedMemoryRanges',
    'vkGetDeviceMemoryCommitment',
    'vkGetBufferMemoryRequirements',
    'vkBindBufferMemory',
    'vkGetImageMemoryRequirements',
    'vkBindImageMemory',
    'vkGetImageSparseMemoryRequirements',
    'vkGetPhysicalDeviceSparseImageFormatProperties',
    'vkQueueBindSparse',
    'vkCreateFence',
    'vkDestroyFence',
    'vkResetFences',
    'vkGetFenceStatus',
    'vkWaitForFences',
    'vkCreateSemaphore',
    'vkDestroySemaphore',
    'vkCreateEvent',
    'vkDestroyEvent',
    'vkGetEventStatus',
    'vkSetEvent',
    'vkResetEvent',
    'vkCreateQueryPool',
    'vkDestroyQueryPool',
    'vkGetQueryPoolResults',
    'vkResetQueryPool',
    'vkCreateBuffer',
    'vkDestroyBuffer',
    'vkCreateBufferView',
    'vkDestroyBufferView',
    'vkCreateImage',
    'vkDestroyImage',
    'vkGetImageSubresourceLayout',
    'vkCreateImageView',
    'vkDestroyImageView',
    'vkCreateShaderModule',
    'vkDestroyShaderModule',
    'vkCreatePipelineCache',
    'vkDestroyPipelineCache',
    'vkGetPipelineCacheData',
    'vkMergePipelineCaches',
    'vkCreateGraphicsPipelines',
    'vkCreateComputePipelines',
    'vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI',
    'vkDestroyPipeline',
    'vkCreatePipelineLayout',
    'vkDestroyPipelineLayout',
    'vkCreateSampler',
    'vkDestroySampler',
    'vkCreateDescriptorSetLayout',
    'vkDestroyDescriptorSetLayout',
    'vkCreateDescriptorPool',
    'vkDestroyDescriptorPool',
    'vkResetDescriptorPool',
    'vkAllocateDescriptorSets',
    'vkFreeDescriptorSets',
    'vkUpdateDescriptorSets',
    'vkCreateFramebuffer',
    'vkDestroyFramebuffer',
    'vkCreateRenderPass',
    'vkDestroyRenderPass',
    'vkGetRenderAreaGranularity',
    'vkGetRenderingAreaGranularityKHR',
    'vkCreateCommandPool',
    'vkDestroyCommandPool',
    'vkResetCommandPool',
    'vkAllocateCommandBuffers',
    'vkFreeCommandBuffers',
    'vkBeginCommandBuffer',
    'vkEndCommandBuffer',
    'vkResetCommandBuffer',
    'vkCmdBindPipeline',
    'vkCmdSetAttachmentFeedbackLoopEnableEXT',
    'vkCmdSetViewport',
    'vkCmdSetScissor',
    'vkCmdSetLineWidth',
    'vkCmdSetDepthBias',
    'vkCmdSetBlendConstants',
    'vkCmdSetDepthBounds',
    'vkCmdSetStencilCompareMask',
    'vkCmdSetStencilWriteMask',
    'vkCmdSetStencilReference',
    'vkCmdBindDescriptorSets',
    'vkCmdBindIndexBuffer',
    'vkCmdBindVertexBuffers',
    'vkCmdDraw',
    'vkCmdDrawIndexed',
    'vkCmdDrawMultiEXT',
    'vkCmdDrawMultiIndexedEXT',
    'vkCmdDrawIndirect',
    'vkCmdDrawIndexedIndirect',
    'vkCmdDispatch',
    'vkCmdDispatchIndirect',
    'vkCmdSubpassShadingHUAWEI',
    'vkCmdDrawClusterHUAWEI',
    'vkCmdDrawClusterIndirectHUAWEI',
    'vkCmdUpdatePipelineIndirectBufferNV',
    'vkCmdCopyBuffer',
    'vkCmdCopyImage',
    'vkCmdBlitImage',
    'vkCmdCopyBufferToImage',
    'vkCmdCopyImageToBuffer',
    'vkCmdCopyMemoryIndirectNV',
    'vkCmdCopyMemoryToImageIndirectNV',
    'vkCmdUpdateBuffer',
    'vkCmdFillBuffer',
    'vkCmdClearColorImage',
    'vkCmdClearDepthStencilImage',
    'vkCmdClearAttachments',
    'vkCmdResolveImage',
    'vkCmdSetEvent',
    'vkCmdResetEvent',
    'vkCmdWaitEvents',
    'vkCmdPipelineBarrier',
    'vkCmdBeginQuery',
    'vkCmdEndQuery',
    'vkCmdBeginConditionalRenderingEXT',
    'vkCmdEndConditionalRenderingEXT',
    'vkCmdResetQueryPool',
    'vkCmdWriteTimestamp',
    'vkCmdCopyQueryPoolResults',
    'vkCmdPushConstants',
    'vkCmdBeginRenderPass',
    'vkCmdNextSubpass',
    'vkCmdEndRenderPass',
    'vkCmdExecuteCommands',
    'vkCreateAndroidSurfaceKHR',
    'vkGetPhysicalDeviceDisplayPropertiesKHR',
    'vkGetPhysicalDeviceDisplayPlanePropertiesKHR',
    'vkGetDisplayPlaneSupportedDisplaysKHR',
    'vkGetDisplayModePropertiesKHR',
    'vkCreateDisplayModeKHR',
    'vkGetDisplayPlaneCapabilitiesKHR',
    'vkCreateDisplayPlaneSurfaceKHR',
    'vkCreateSharedSwapchainsKHR',
    'vkDestroySurfaceKHR',
    'vkGetPhysicalDeviceSurfaceSupportKHR',
    'vkGetPhysicalDeviceSurfaceCapabilitiesKHR',
    'vkGetPhysicalDeviceSurfaceFormatsKHR',
    'vkGetPhysicalDeviceSurfacePresentModesKHR',
    'vkCreateSwapchainKHR',
    'vkDestroySwapchainKHR',
    'vkGetSwapchainImagesKHR',
    'vkAcquireNextImageKHR',
    'vkQueuePresentKHR',
    'vkCreateViSurfaceNN',
    'vkCreateWaylandSurfaceKHR',
    'vkGetPhysicalDeviceWaylandPresentationSupportKHR',
    'vkCreateWin32SurfaceKHR',
    'vkGetPhysicalDeviceWin32PresentationSupportKHR',
    'vkCreateXlibSurfaceKHR',
    'vkGetPhysicalDeviceXlibPresentationSupportKHR',
    'vkCreateXcbSurfaceKHR',
    'vkGetPhysicalDeviceXcbPresentationSupportKHR',
    'vkCreateDirectFBSurfaceEXT',
    'vkGetPhysicalDeviceDirectFBPresentationSupportEXT',
    'vkCreateImagePipeSurfaceFUCHSIA',
    'vkCreateStreamDescriptorSurfaceGGP',
    'vkCreateScreenSurfaceQNX',
    'vkGetPhysicalDeviceScreenPresentationSupportQNX',
    'vkCreateDebugReportCallbackEXT',
    'vkDestroyDebugReportCallbackEXT',
    'vkDebugReportMessageEXT',
    'vkDebugMarkerSetObjectNameEXT',
    'vkDebugMarkerSetObjectTagEXT',
    'vkCmdDebugMarkerBeginEXT',
    'vkCmdDebugMarkerEndEXT',
    'vkCmdDebugMarkerInsertEXT',
    'vkGetPhysicalDeviceExternalImageFormatPropertiesNV',
    'vkGetMemoryWin32HandleNV',
    'vkCmdExecuteGeneratedCommandsNV',
    'vkCmdPreprocessGeneratedCommandsNV',
    'vkCmdBindPipelineShaderGroupNV',
    'vkGetGeneratedCommandsMemoryRequirementsNV',
    'vkCreateIndirectCommandsLayoutNV',
    'vkDestroyIndirectCommandsLayoutNV',
    'vkGetPhysicalDeviceFeatures2',
    'vkGetPhysicalDeviceProperties2',
    'vkGetPhysicalDeviceFormatProperties2',
    'vkGetPhysicalDeviceImageFormatProperties2',
    'vkGetPhysicalDeviceQueueFamilyProperties2',
    'vkGetPhysicalDeviceMemoryProperties2',
    'vkGetPhysicalDeviceSparseImageFormatProperties2',
    'vkCmdPushDescriptorSetKHR',
    'vkTrimCommandPool',
    'vkGetPhysicalDeviceExternalBufferProperties',
    'vkGetMemoryWin32HandleKHR',
    'vkGetMemoryWin32HandlePropertiesKHR',
    'vkGetMemoryFdKHR',
    'vkGetMemoryFdPropertiesKHR',
    'vkGetMemoryZirconHandleFUCHSIA',
    'vkGetMemoryZirconHandlePropertiesFUCHSIA',
    'vkGetMemoryRemoteAddressNV',
    'vkGetMemorySciBufNV',
    'vkGetPhysicalDeviceExternalMemorySciBufPropertiesNV',
    'vkGetPhysicalDeviceSciBufAttributesNV',
    'vkGetPhysicalDeviceExternalSemaphoreProperties',
    'vkGetSemaphoreWin32HandleKHR',
    'vkImportSemaphoreWin32HandleKHR',
    'vkGetSemaphoreFdKHR',
    'vkImportSemaphoreFdKHR',
    'vkGetSemaphoreZirconHandleFUCHSIA',
    'vkImportSemaphoreZirconHandleFUCHSIA',
    'vkGetPhysicalDeviceExternalFenceProperties',
    'vkGetFenceWin32HandleKHR',
    'vkImportFenceWin32HandleKHR',
    'vkGetFenceFdKHR',
    'vkImportFenceFdKHR',
    'vkGetFenceSciSyncFenceNV',
    'vkGetFenceSciSyncObjNV',
    'vkImportFenceSciSyncFenceNV',
    'vkImportFenceSciSyncObjNV',
    'vkGetSemaphoreSciSyncObjNV',
    'vkImportSemaphoreSciSyncObjNV',
    'vkGetPhysicalDeviceSciSyncAttributesNV',
    'vkCreateSemaphoreSciSyncPoolNV',
    'vkDestroySemaphoreSciSyncPoolNV',
    'vkReleaseDisplayEXT',
    'vkAcquireXlibDisplayEXT',
    'vkGetRandROutputDisplayEXT',
    'vkAcquireWinrtDisplayNV',
    'vkGetWinrtDisplayNV',
    'vkDisplayPowerControlEXT',
    'vkRegisterDeviceEventEXT',
    'vkRegisterDisplayEventEXT',
    'vkGetSwapchainCounterEXT',
    'vkGetPhysicalDeviceSurfaceCapabilities2EXT',
    'vkEnumeratePhysicalDeviceGroups',
    'vkGetDeviceGroupPeerMemoryFeatures',
    'vkBindBufferMemory2',
    'vkBindImageMemory2',
    'vkCmdSetDeviceMask',
    'vkGetDeviceGroupPresentCapabilitiesKHR',
    'vkGetDeviceGroupSurfacePresentModesKHR',
    'vkAcquireNextImage2KHR',
    'vkCmdDispatchBase',
    'vkGetPhysicalDevicePresentRectanglesKHR',
    'vkCreateDescriptorUpdateTemplate',
    'vkDestroyDescriptorUpdateTemplate',
    'vkUpdateDescriptorSetWithTemplate',
    'vkCmdPushDescriptorSetWithTemplateKHR',
    'vkSetHdrMetadataEXT',
    'vkGetSwapchainStatusKHR',
    'vkGetRefreshCycleDurationGOOGLE',
    'vkGetPastPresentationTimingGOOGLE',
    'vkCreateIOSSurfaceMVK',
    'vkCreateMacOSSurfaceMVK',
    'vkCreateMetalSurfaceEXT',
    'vkCmdSetViewportWScalingNV',
    'vkCmdSetDiscardRectangleEXT',
    'vkCmdSetDiscardRectangleEnableEXT',
    'vkCmdSetDiscardRectangleModeEXT',
    'vkCmdSetSampleLocationsEXT',
    'vkGetPhysicalDeviceMultisamplePropertiesEXT',
    'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
    'vkGetPhysicalDeviceSurfaceFormats2KHR',
    'vkGetPhysicalDeviceDisplayProperties2KHR',
    'vkGetPhysicalDeviceDisplayPlaneProperties2KHR',
    'vkGetDisplayModeProperties2KHR',
    'vkGetDisplayPlaneCapabilities2KHR',
    'vkGetBufferMemoryRequirements2',
    'vkGetImageMemoryRequirements2',
    'vkGetImageSparseMemoryRequirements2',
    'vkGetDeviceBufferMemoryRequirements',
    'vkGetDeviceImageMemoryRequirements',
    'vkGetDeviceImageSparseMemoryRequirements',
    'vkCreateSamplerYcbcrConversion',
    'vkDestroySamplerYcbcrConversion',
    'vkGetDeviceQueue2',
    'vkCreateValidationCacheEXT',
    'vkDestroyValidationCacheEXT',
    'vkGetValidationCacheDataEXT',
    'vkMergeValidationCachesEXT',
    'vkGetDescriptorSetLayoutSupport',
    'vkGetSwapchainGrallocUsageANDROID',
    'vkGetSwapchainGrallocUsage2ANDROID',
    'vkAcquireImageANDROID',
    'vkQueueSignalReleaseImageANDROID',
    'vkGetShaderInfoAMD',
    'vkSetLocalDimmingAMD',
    'vkGetPhysicalDeviceCalibrateableTimeDomainsKHR',
    'vkGetCalibratedTimestampsKHR',
    'vkSetDebugUtilsObjectNameEXT',
    'vkSetDebugUtilsObjectTagEXT',
    'vkQueueBeginDebugUtilsLabelEXT',
    'vkQueueEndDebugUtilsLabelEXT',
    'vkQueueInsertDebugUtilsLabelEXT',
    'vkCmdBeginDebugUtilsLabelEXT',
    'vkCmdEndDebugUtilsLabelEXT',
    'vkCmdInsertDebugUtilsLabelEXT',
    'vkCreateDebugUtilsMessengerEXT',
    'vkDestroyDebugUtilsMessengerEXT',
    'vkSubmitDebugUtilsMessageEXT',
    'vkGetMemoryHostPointerPropertiesEXT',
    'vkCmdWriteBufferMarkerAMD',
    'vkCreateRenderPass2',
    'vkCmdBeginRenderPass2',
    'vkCmdNextSubpass2',
    'vkCmdEndRenderPass2',
    'vkGetSemaphoreCounterValue',
    'vkWaitSemaphores',
    'vkSignalSemaphore',
    'vkGetAndroidHardwareBufferPropertiesANDROID',
    'vkGetMemoryAndroidHardwareBufferANDROID',
    'vkCmdDrawIndirectCount',
    'vkCmdDrawIndexedIndirectCount',
    'vkCmdSetCheckpointNV',
    'vkGetQueueCheckpointDataNV',
    'vkCmdBindTransformFeedbackBuffersEXT',
    'vkCmdBeginTransformFeedbackEXT',
    'vkCmdEndTransformFeedbackEXT',
    'vkCmdBeginQueryIndexedEXT',
    'vkCmdEndQueryIndexedEXT',
    'vkCmdDrawIndirectByteCountEXT',
    'vkCmdSetExclusiveScissorNV',
    'vkCmdSetExclusiveScissorEnableNV',
    'vkCmdBindShadingRateImageNV',
    'vkCmdSetViewportShadingRatePaletteNV',
    'vkCmdSetCoarseSampleOrderNV',
    'vkCmdDrawMeshTasksNV',
    'vkCmdDrawMeshTasksIndirectNV',
    'vkCmdDrawMeshTasksIndirectCountNV',
    'vkCmdDrawMeshTasksEXT',
    'vkCmdDrawMeshTasksIndirectEXT',
    'vkCmdDrawMeshTasksIndirectCountEXT',
    'vkCompileDeferredNV',
    'vkCreateAccelerationStructureNV',
    'vkCmdBindInvocationMaskHUAWEI',
    'vkDestroyAccelerationStructureKHR',
    'vkDestroyAccelerationStructureNV',
    'vkGetAccelerationStructureMemoryRequirementsNV',
    'vkBindAccelerationStructureMemoryNV',
    'vkCmdCopyAccelerationStructureNV',
    'vkCmdCopyAccelerationStructureKHR',
    'vkCopyAccelerationStructureKHR',
    'vkCmdCopyAccelerationStructureToMemoryKHR',
    'vkCopyAccelerationStructureToMemoryKHR',
    'vkCmdCopyMemoryToAccelerationStructureKHR',
    'vkCopyMemoryToAccelerationStructureKHR',
    'vkCmdWriteAccelerationStructuresPropertiesKHR',
    'vkCmdWriteAccelerationStructuresPropertiesNV',
    'vkCmdBuildAccelerationStructureNV',
    'vkWriteAccelerationStructuresPropertiesKHR',
    'vkCmdTraceRaysKHR',
    'vkCmdTraceRaysNV',
    'vkGetRayTracingShaderGroupHandlesKHR',
    'vkGetRayTracingCaptureReplayShaderGroupHandlesKHR',
    'vkGetAccelerationStructureHandleNV',
    'vkCreateRayTracingPipelinesNV',
    'vkCreateRayTracingPipelinesKHR',
    'vkGetPhysicalDeviceCooperativeMatrixPropertiesNV',
    'vkCmdTraceRaysIndirectKHR',
    'vkCmdTraceRaysIndirect2KHR',
    'vkGetDeviceAccelerationStructureCompatibilityKHR',
    'vkGetRayTracingShaderGroupStackSizeKHR',
    'vkCmdSetRayTracingPipelineStackSizeKHR',
    'vkGetImageViewHandleNVX',
    'vkGetImageViewAddressNVX',
    'vkGetPhysicalDeviceSurfacePresentModes2EXT',
    'vkGetDeviceGroupSurfacePresentModes2EXT',
    'vkAcquireFullScreenExclusiveModeEXT',
    'vkReleaseFullScreenExclusiveModeEXT',
    'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR',
    'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR',
    'vkAcquireProfilingLockKHR',
    'vkReleaseProfilingLockKHR',
    'vkGetImageDrmFormatModifierPropertiesEXT',
    'vkGetBufferOpaqueCaptureAddress',
    'vkGetBufferDeviceAddress',
    'vkCreateHeadlessSurfaceEXT',
    'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV',
    'vkInitializePerformanceApiINTEL',
    'vkUninitializePerformanceApiINTEL',
    'vkCmdSetPerformanceMarkerINTEL',
    'vkCmdSetPerformanceStreamMarkerINTEL',
    'vkCmdSetPerformanceOverrideINTEL',
    'vkAcquirePerformanceConfigurationINTEL',
    'vkReleasePerformanceConfigurationINTEL',
    'vkQueueSetPerformanceConfigurationINTEL',
    'vkGetPerformanceParameterINTEL',
    'vkGetDeviceMemoryOpaqueCaptureAddress',
    'vkGetPipelineExecutablePropertiesKHR',
    'vkGetPipelineExecutableStatisticsKHR',
    'vkGetPipelineExecutableInternalRepresentationsKHR',
    'vkCmdSetLineStippleKHR',
    'vkGetFaultData',
    'vkGetPhysicalDeviceToolProperties',
    'vkCreateAccelerationStructureKHR',
    'vkCmdBuildAccelerationStructuresKHR',
    'vkCmdBuildAccelerationStructuresIndirectKHR',
    'vkBuildAccelerationStructuresKHR',
    'vkGetAccelerationStructureDeviceAddressKHR',
    'vkCreateDeferredOperationKHR',
    'vkDestroyDeferredOperationKHR',
    'vkGetDeferredOperationMaxConcurrencyKHR',
    'vkGetDeferredOperationResultKHR',
    'vkDeferredOperationJoinKHR',
    'vkGetPipelineIndirectMemoryRequirementsNV',
    'vkGetPipelineIndirectDeviceAddressNV',
    'vkCmdSetCullMode',
    'vkCmdSetFrontFace',
    'vkCmdSetPrimitiveTopology',
    'vkCmdSetViewportWithCount',
    'vkCmdSetScissorWithCount',
    'vkCmdBindIndexBuffer2KHR',
    'vkCmdBindVertexBuffers2',
    'vkCmdSetDepthTestEnable',
    'vkCmdSetDepthWriteEnable',
    'vkCmdSetDepthCompareOp',
    'vkCmdSetDepthBoundsTestEnable',
    'vkCmdSetStencilTestEnable',
    'vkCmdSetStencilOp',
    'vkCmdSetPatchControlPointsEXT',
    'vkCmdSetRasterizerDiscardEnable',
    'vkCmdSetDepthBiasEnable',
    'vkCmdSetLogicOpEXT',
    'vkCmdSetPrimitiveRestartEnable',
    'vkCmdSetTessellationDomainOriginEXT',
    'vkCmdSetDepthClampEnableEXT',
    'vkCmdSetPolygonModeEXT',
    'vkCmdSetRasterizationSamplesEXT',
    'vkCmdSetSampleMaskEXT',
    'vkCmdSetAlphaToCoverageEnableEXT',
    'vkCmdSetAlphaToOneEnableEXT',
    'vkCmdSetLogicOpEnableEXT',
    'vkCmdSetColorBlendEnableEXT',
    'vkCmdSetColorBlendEquationEXT',
    'vkCmdSetColorWriteMaskEXT',
    'vkCmdSetRasterizationStreamEXT',
    'vkCmdSetConservativeRasterizationModeEXT',
    'vkCmdSetExtraPrimitiveOverestimationSizeEXT',
    'vkCmdSetDepthClipEnableEXT',
    'vkCmdSetSampleLocationsEnableEXT',
    'vkCmdSetColorBlendAdvancedEXT',
    'vkCmdSetProvokingVertexModeEXT',
    'vkCmdSetLineRasterizationModeEXT',
    'vkCmdSetLineStippleEnableEXT',
    'vkCmdSetDepthClipNegativeOneToOneEXT',
    'vkCmdSetViewportWScalingEnableNV',
    'vkCmdSetViewportSwizzleNV',
    'vkCmdSetCoverageToColorEnableNV',
    'vkCmdSetCoverageToColorLocationNV',
    'vkCmdSetCoverageModulationModeNV',
    'vkCmdSetCoverageModulationTableEnableNV',
    'vkCmdSetCoverageModulationTableNV',
    'vkCmdSetShadingRateImageEnableNV',
    'vkCmdSetCoverageReductionModeNV',
    'vkCmdSetRepresentativeFragmentTestEnableNV',
    'vkCreatePrivateDataSlot',
    'vkDestroyPrivateDataSlot',
    'vkSetPrivateData',
    'vkGetPrivateData',
    'vkCmdCopyBuffer2',
    'vkCmdCopyImage2',
    'vkCmdBlitImage2',
    'vkCmdCopyBufferToImage2',
    'vkCmdCopyImageToBuffer2',
    'vkCmdResolveImage2',
    'vkCmdRefreshObjectsKHR',
    'vkGetPhysicalDeviceRefreshableObjectTypesKHR',
    'vkCmdSetFragmentShadingRateKHR',
    'vkGetPhysicalDeviceFragmentShadingRatesKHR',
    'vkCmdSetFragmentShadingRateEnumNV',
    'vkGetAccelerationStructureBuildSizesKHR',
    'vkCmdSetVertexInputEXT',
    'vkCmdSetColorWriteEnableEXT',
    'vkCmdSetEvent2',
    'vkCmdResetEvent2',
    'vkCmdWaitEvents2',
    'vkCmdPipelineBarrier2',
    'vkQueueSubmit2',
    'vkCmdWriteTimestamp2',
    'vkCmdWriteBufferMarker2AMD',
    'vkGetQueueCheckpointData2NV',
    'vkCopyMemoryToImageEXT',
    'vkCopyImageToMemoryEXT',
    'vkCopyImageToImageEXT',
    'vkTransitionImageLayoutEXT',
    'vkGetCommandPoolMemoryConsumption',
    'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
    'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
    'vkCreateVideoSessionKHR',
    'vkDestroyVideoSessionKHR',
    'vkCreateVideoSessionParametersKHR',
    'vkUpdateVideoSessionParametersKHR',
    'vkGetEncodedVideoSessionParametersKHR',
    'vkDestroyVideoSessionParametersKHR',
    'vkGetVideoSessionMemoryRequirementsKHR',
    'vkBindVideoSessionMemoryKHR',
    'vkCmdDecodeVideoKHR',
    'vkCmdBeginVideoCodingKHR',
    'vkCmdControlVideoCodingKHR',
    'vkCmdEndVideoCodingKHR',
    'vkCmdEncodeVideoKHR',
    'vkCmdDecompressMemoryNV',
    'vkCmdDecompressMemoryIndirectCountNV',
    'vkCreateCuModuleNVX',
    'vkCreateCuFunctionNVX',
    'vkDestroyCuModuleNVX',
    'vkDestroyCuFunctionNVX',
    'vkCmdCuLaunchKernelNVX',
    'vkGetDescriptorSetLayoutSizeEXT',
    'vkGetDescriptorSetLayoutBindingOffsetEXT',
    'vkGetDescriptorEXT',
    'vkCmdBindDescriptorBuffersEXT',
    'vkCmdSetDescriptorBufferOffsetsEXT',
    'vkCmdBindDescriptorBufferEmbeddedSamplersEXT',
    'vkGetBufferOpaqueCaptureDescriptorDataEXT',
    'vkGetImageOpaqueCaptureDescriptorDataEXT',
    'vkGetImageViewOpaqueCaptureDescriptorDataEXT',
    'vkGetSamplerOpaqueCaptureDescriptorDataEXT',
    'vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT',
    'vkSetDeviceMemoryPriorityEXT',
    'vkAcquireDrmDisplayEXT',
    'vkGetDrmDisplayEXT',
    'vkWaitForPresentKHR',
    'vkCreateBufferCollectionFUCHSIA',
    'vkSetBufferCollectionBufferConstraintsFUCHSIA',
    'vkSetBufferCollectionImageConstraintsFUCHSIA',
    'vkDestroyBufferCollectionFUCHSIA',
    'vkGetBufferCollectionPropertiesFUCHSIA',
    'vkCreateCudaModuleNV',
    'vkGetCudaModuleCacheNV',
    'vkCreateCudaFunctionNV',
    'vkDestroyCudaModuleNV',
    'vkDestroyCudaFunctionNV',
    'vkCmdCudaLaunchKernelNV',
    'vkCmdBeginRendering',
    'vkCmdEndRendering',
    'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    'vkGetDescriptorSetHostMappingVALVE',
    'vkCreateMicromapEXT',
    'vkCmdBuildMicromapsEXT',
    'vkBuildMicromapsEXT',
    'vkDestroyMicromapEXT',
    'vkCmdCopyMicromapEXT',
    'vkCopyMicromapEXT',
    'vkCmdCopyMicromapToMemoryEXT',
    'vkCopyMicromapToMemoryEXT',
    'vkCmdCopyMemoryToMicromapEXT',
    'vkCopyMemoryToMicromapEXT',
    'vkCmdWriteMicromapsPropertiesEXT',
    'vkWriteMicromapsPropertiesEXT',
    'vkGetDeviceMicromapCompatibilityEXT',
    'vkGetMicromapBuildSizesEXT',
    'vkGetShaderModuleIdentifierEXT',
    'vkGetShaderModuleCreateInfoIdentifierEXT',
    'vkGetImageSubresourceLayout2KHR',
    'vkGetPipelinePropertiesEXT',
    'vkExportMetalObjectsEXT',
    'vkGetFramebufferTilePropertiesQCOM',
    'vkGetDynamicRenderingTilePropertiesQCOM',
    'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
    'vkCreateOpticalFlowSessionNV',
    'vkDestroyOpticalFlowSessionNV',
    'vkBindOpticalFlowSessionImageNV',
    'vkCmdOpticalFlowExecuteNV',
    'vkGetDeviceFaultInfoEXT',
    'vkCmdSetDepthBias2EXT',
    'vkReleaseSwapchainImagesEXT',
    'vkGetDeviceImageSubresourceLayoutKHR',
    'vkMapMemory2KHR',
    'vkUnmapMemory2KHR',
    'vkCreateShadersEXT',
    'vkDestroyShaderEXT',
    'vkGetShaderBinaryDataEXT',
    'vkCmdBindShadersEXT',
    'vkGetScreenBufferPropertiesQNX',
    'vkGetPhysicalDeviceCooperativeMatrixPropertiesKHR',
    'vkGetExecutionGraphPipelineScratchSizeAMDX',
    'vkGetExecutionGraphPipelineNodeIndexAMDX',
    'vkCreateExecutionGraphPipelinesAMDX',
    'vkCmdInitializeGraphScratchMemoryAMDX',
    'vkCmdDispatchGraphAMDX',
    'vkCmdDispatchGraphIndirectAMDX',
    'vkCmdDispatchGraphIndirectCountAMDX',
    'vkCmdBindDescriptorSets2KHR',
    'vkCmdPushConstants2KHR',
    'vkCmdPushDescriptorSet2KHR',
    'vkCmdPushDescriptorSetWithTemplate2KHR',
    'vkCmdSetDescriptorBufferOffsets2EXT',
    'vkCmdBindDescriptorBufferEmbeddedSamplers2EXT',
    'vkSetLatencySleepModeNV',
    'vkLatencySleepNV',
    'vkSetLatencyMarkerNV',
    'vkGetLatencyTimingsNV',
    'vkQueueNotifyOutOfBandNV',
    'vkCmdSetRenderingAttachmentLocationsKHR',
    'vkCmdSetRenderingInputAttachmentIndicesKHR',
]
