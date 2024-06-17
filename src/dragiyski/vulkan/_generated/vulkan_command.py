import ctypes
from .vulkan_base import VKAPI_PTR, VKAPI_CALL
from ._vulkan_type import (
    VkAccelerationStructureBuildGeometryInfoKHR,
    VkAccelerationStructureBuildRangeInfoKHR,
    VkAccelerationStructureBuildSizesInfoKHR,
    VkAccelerationStructureCaptureDescriptorDataInfoEXT,
    VkAccelerationStructureCreateInfoKHR,
    VkAccelerationStructureCreateInfoNV,
    VkAccelerationStructureDeviceAddressInfoKHR,
    VkAccelerationStructureInfoNV,
    VkAccelerationStructureMemoryRequirementsInfoNV,
    VkAccelerationStructureVersionInfoKHR,
    VkAcquireNextImageInfoKHR,
    VkAcquireProfilingLockInfoKHR,
    VkAllocationCallbacks,
    VkAndroidHardwareBufferPropertiesANDROID,
    VkAndroidSurfaceCreateInfoKHR,
    VkBaseOutStructure,
    VkBindAccelerationStructureMemoryInfoNV,
    VkBindBufferMemoryInfo,
    VkBindDescriptorBufferEmbeddedSamplersInfoEXT,
    VkBindDescriptorSetsInfoKHR,
    VkBindImageMemoryInfo,
    VkBindSparseInfo,
    VkBindVideoSessionMemoryInfoKHR,
    VkBlitImageInfo2,
    VkBufferCaptureDescriptorDataInfoEXT,
    VkBufferCollectionCreateInfoFUCHSIA,
    VkBufferCollectionPropertiesFUCHSIA,
    VkBufferConstraintsInfoFUCHSIA,
    VkBufferCopy,
    VkBufferCreateInfo,
    VkBufferDeviceAddressInfo,
    VkBufferImageCopy,
    VkBufferMemoryBarrier,
    VkBufferMemoryRequirementsInfo2,
    VkBufferViewCreateInfo,
    VkCalibratedTimestampInfoKHR,
    VkCheckpointData2NV,
    VkCheckpointDataNV,
    VkClearAttachment,
    VkClearColorValue,
    VkClearDepthStencilValue,
    VkClearRect,
    VkCoarseSampleOrderCustomNV,
    VkColorBlendAdvancedEXT,
    VkColorBlendEquationEXT,
    VkCommandBufferAllocateInfo,
    VkCommandBufferBeginInfo,
    VkCommandPoolCreateInfo,
    VkCommandPoolMemoryConsumption,
    VkComputePipelineCreateInfo,
    VkConditionalRenderingBeginInfoEXT,
    VkCooperativeMatrixPropertiesKHR,
    VkCooperativeMatrixPropertiesNV,
    VkCopyAccelerationStructureInfoKHR,
    VkCopyAccelerationStructureToMemoryInfoKHR,
    VkCopyBufferInfo2,
    VkCopyBufferToImageInfo2,
    VkCopyDescriptorSet,
    VkCopyImageInfo2,
    VkCopyImageToBufferInfo2,
    VkCopyImageToImageInfoEXT,
    VkCopyImageToMemoryInfoEXT,
    VkCopyMemoryToAccelerationStructureInfoKHR,
    VkCopyMemoryToImageInfoEXT,
    VkCopyMemoryToMicromapInfoEXT,
    VkCopyMicromapInfoEXT,
    VkCopyMicromapToMemoryInfoEXT,
    VkCuFunctionCreateInfoNVX,
    VkCuLaunchInfoNVX,
    VkCuModuleCreateInfoNVX,
    VkCudaFunctionCreateInfoNV,
    VkCudaLaunchInfoNV,
    VkCudaModuleCreateInfoNV,
    VkDebugMarkerMarkerInfoEXT,
    VkDebugMarkerObjectNameInfoEXT,
    VkDebugMarkerObjectTagInfoEXT,
    VkDebugReportCallbackCreateInfoEXT,
    VkDebugUtilsLabelEXT,
    VkDebugUtilsMessengerCallbackDataEXT,
    VkDebugUtilsMessengerCreateInfoEXT,
    VkDebugUtilsObjectNameInfoEXT,
    VkDebugUtilsObjectTagInfoEXT,
    VkDecompressMemoryRegionNV,
    VkDependencyInfo,
    VkDepthBiasInfoEXT,
    VkDescriptorBufferBindingInfoEXT,
    VkDescriptorGetInfoEXT,
    VkDescriptorPoolCreateInfo,
    VkDescriptorSetAllocateInfo,
    VkDescriptorSetBindingReferenceVALVE,
    VkDescriptorSetLayoutCreateInfo,
    VkDescriptorSetLayoutHostMappingInfoVALVE,
    VkDescriptorSetLayoutSupport,
    VkDescriptorUpdateTemplateCreateInfo,
    VkDeviceBufferMemoryRequirements,
    VkDeviceCreateInfo,
    VkDeviceEventInfoEXT,
    VkDeviceFaultCountsEXT,
    VkDeviceFaultInfoEXT,
    VkDeviceGroupPresentCapabilitiesKHR,
    VkDeviceImageMemoryRequirements,
    VkDeviceImageSubresourceInfoKHR,
    VkDeviceMemoryOpaqueCaptureAddressInfo,
    VkDeviceQueueInfo2,
    VkDirectFBSurfaceCreateInfoEXT,
    VkDispatchGraphCountInfoAMDX,
    VkDisplayEventInfoEXT,
    VkDisplayModeCreateInfoKHR,
    VkDisplayModeProperties2KHR,
    VkDisplayModePropertiesKHR,
    VkDisplayPlaneCapabilities2KHR,
    VkDisplayPlaneCapabilitiesKHR,
    VkDisplayPlaneInfo2KHR,
    VkDisplayPlaneProperties2KHR,
    VkDisplayPlanePropertiesKHR,
    VkDisplayPowerInfoEXT,
    VkDisplayProperties2KHR,
    VkDisplayPropertiesKHR,
    VkDisplaySurfaceCreateInfoKHR,
    VkEventCreateInfo,
    VkExecutionGraphPipelineCreateInfoAMDX,
    VkExecutionGraphPipelineScratchSizeAMDX,
    VkExportMetalObjectsInfoEXT,
    VkExtensionProperties,
    VkExtent2D,
    VkExternalBufferProperties,
    VkExternalFenceProperties,
    VkExternalImageFormatPropertiesNV,
    VkExternalSemaphoreProperties,
    VkFaultData,
    VkFenceCreateInfo,
    VkFenceGetFdInfoKHR,
    VkFenceGetSciSyncInfoNV,
    VkFenceGetWin32HandleInfoKHR,
    VkFormatProperties,
    VkFormatProperties2,
    VkFramebufferCreateInfo,
    VkFramebufferMixedSamplesCombinationNV,
    VkGeneratedCommandsInfoNV,
    VkGeneratedCommandsMemoryRequirementsInfoNV,
    VkGetLatencyMarkerInfoNV,
    VkGraphicsPipelineCreateInfo,
    VkHdrMetadataEXT,
    VkHeadlessSurfaceCreateInfoEXT,
    VkHostImageLayoutTransitionInfoEXT,
    VkIOSSurfaceCreateInfoMVK,
    VkImageBlit,
    VkImageCaptureDescriptorDataInfoEXT,
    VkImageConstraintsInfoFUCHSIA,
    VkImageCopy,
    VkImageCreateInfo,
    VkImageDrmFormatModifierPropertiesEXT,
    VkImageFormatProperties,
    VkImageFormatProperties2,
    VkImageMemoryBarrier,
    VkImageMemoryRequirementsInfo2,
    VkImagePipeSurfaceCreateInfoFUCHSIA,
    VkImageResolve,
    VkImageSparseMemoryRequirementsInfo2,
    VkImageSubresource,
    VkImageSubresource2KHR,
    VkImageSubresourceLayers,
    VkImageSubresourceRange,
    VkImageViewAddressPropertiesNVX,
    VkImageViewCaptureDescriptorDataInfoEXT,
    VkImageViewCreateInfo,
    VkImageViewHandleInfoNVX,
    VkImportFenceFdInfoKHR,
    VkImportFenceSciSyncInfoNV,
    VkImportFenceWin32HandleInfoKHR,
    VkImportSemaphoreFdInfoKHR,
    VkImportSemaphoreSciSyncInfoNV,
    VkImportSemaphoreWin32HandleInfoKHR,
    VkImportSemaphoreZirconHandleInfoFUCHSIA,
    VkIndirectCommandsLayoutCreateInfoNV,
    VkInitializePerformanceApiInfoINTEL,
    VkInstanceCreateInfo,
    VkLatencySleepInfoNV,
    VkLatencySleepModeInfoNV,
    VkLayerProperties,
    VkMacOSSurfaceCreateInfoMVK,
    VkMappedMemoryRange,
    VkMemoryAllocateInfo,
    VkMemoryBarrier,
    VkMemoryFdPropertiesKHR,
    VkMemoryGetAndroidHardwareBufferInfoANDROID,
    VkMemoryGetFdInfoKHR,
    VkMemoryGetRemoteAddressInfoNV,
    VkMemoryGetSciBufInfoNV,
    VkMemoryGetWin32HandleInfoKHR,
    VkMemoryGetZirconHandleInfoFUCHSIA,
    VkMemoryHostPointerPropertiesEXT,
    VkMemoryMapInfoKHR,
    VkMemoryRequirements,
    VkMemoryRequirements2,
    VkMemorySciBufPropertiesNV,
    VkMemoryUnmapInfoKHR,
    VkMemoryWin32HandlePropertiesKHR,
    VkMemoryZirconHandlePropertiesFUCHSIA,
    VkMetalSurfaceCreateInfoEXT,
    VkMicromapBuildInfoEXT,
    VkMicromapBuildSizesInfoEXT,
    VkMicromapCreateInfoEXT,
    VkMicromapVersionInfoEXT,
    VkMultiDrawIndexedInfoEXT,
    VkMultiDrawInfoEXT,
    VkMultisamplePropertiesEXT,
    VkOpticalFlowExecuteInfoNV,
    VkOpticalFlowImageFormatInfoNV,
    VkOpticalFlowImageFormatPropertiesNV,
    VkOpticalFlowSessionCreateInfoNV,
    VkOutOfBandQueueTypeInfoNV,
    VkPastPresentationTimingGOOGLE,
    VkPerformanceConfigurationAcquireInfoINTEL,
    VkPerformanceCounterDescriptionKHR,
    VkPerformanceCounterKHR,
    VkPerformanceMarkerInfoINTEL,
    VkPerformanceOverrideInfoINTEL,
    VkPerformanceStreamMarkerInfoINTEL,
    VkPerformanceValueINTEL,
    VkPhysicalDeviceExternalBufferInfo,
    VkPhysicalDeviceExternalFenceInfo,
    VkPhysicalDeviceExternalSemaphoreInfo,
    VkPhysicalDeviceFeatures,
    VkPhysicalDeviceFeatures2,
    VkPhysicalDeviceFragmentShadingRateKHR,
    VkPhysicalDeviceGroupProperties,
    VkPhysicalDeviceImageFormatInfo2,
    VkPhysicalDeviceMemoryProperties,
    VkPhysicalDeviceMemoryProperties2,
    VkPhysicalDeviceProperties,
    VkPhysicalDeviceProperties2,
    VkPhysicalDeviceSparseImageFormatInfo2,
    VkPhysicalDeviceSurfaceInfo2KHR,
    VkPhysicalDeviceToolProperties,
    VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR,
    VkPhysicalDeviceVideoFormatInfoKHR,
    VkPipelineCacheCreateInfo,
    VkPipelineExecutableInfoKHR,
    VkPipelineExecutableInternalRepresentationKHR,
    VkPipelineExecutablePropertiesKHR,
    VkPipelineExecutableStatisticKHR,
    VkPipelineIndirectDeviceAddressInfoNV,
    VkPipelineInfoKHR,
    VkPipelineLayoutCreateInfo,
    VkPipelineShaderStageNodeCreateInfoAMDX,
    VkPresentInfoKHR,
    VkPrivateDataSlotCreateInfo,
    VkPushConstantsInfoKHR,
    VkPushDescriptorSetInfoKHR,
    VkPushDescriptorSetWithTemplateInfoKHR,
    VkQueryPoolCreateInfo,
    VkQueryPoolPerformanceCreateInfoKHR,
    VkQueueFamilyProperties,
    VkQueueFamilyProperties2,
    VkRayTracingPipelineCreateInfoKHR,
    VkRayTracingPipelineCreateInfoNV,
    VkRect2D,
    VkRefreshCycleDurationGOOGLE,
    VkRefreshObjectListKHR,
    VkReleaseSwapchainImagesInfoEXT,
    VkRenderPassBeginInfo,
    VkRenderPassCreateInfo,
    VkRenderPassCreateInfo2,
    VkRenderingAreaInfoKHR,
    VkRenderingAttachmentLocationInfoKHR,
    VkRenderingInfo,
    VkRenderingInputAttachmentIndexInfoKHR,
    VkResolveImageInfo2,
    VkSampleLocationsInfoEXT,
    VkSamplerCaptureDescriptorDataInfoEXT,
    VkSamplerCreateInfo,
    VkSamplerYcbcrConversionCreateInfo,
    VkSciSyncAttributesInfoNV,
    VkScreenBufferPropertiesQNX,
    VkScreenSurfaceCreateInfoQNX,
    VkSemaphoreCreateInfo,
    VkSemaphoreGetFdInfoKHR,
    VkSemaphoreGetSciSyncInfoNV,
    VkSemaphoreGetWin32HandleInfoKHR,
    VkSemaphoreGetZirconHandleInfoFUCHSIA,
    VkSemaphoreSciSyncPoolCreateInfoNV,
    VkSemaphoreSignalInfo,
    VkSemaphoreWaitInfo,
    VkSetDescriptorBufferOffsetsInfoEXT,
    VkSetLatencyMarkerInfoNV,
    VkShaderCreateInfoEXT,
    VkShaderModuleCreateInfo,
    VkShaderModuleIdentifierEXT,
    VkShadingRatePaletteNV,
    VkSparseImageFormatProperties,
    VkSparseImageFormatProperties2,
    VkSparseImageMemoryRequirements,
    VkSparseImageMemoryRequirements2,
    VkStreamDescriptorSurfaceCreateInfoGGP,
    VkStridedDeviceAddressRegionKHR,
    VkSubmitInfo,
    VkSubmitInfo2,
    VkSubpassBeginInfo,
    VkSubpassEndInfo,
    VkSubresourceLayout,
    VkSubresourceLayout2KHR,
    VkSurfaceCapabilities2EXT,
    VkSurfaceCapabilities2KHR,
    VkSurfaceCapabilitiesKHR,
    VkSurfaceFormat2KHR,
    VkSurfaceFormatKHR,
    VkSwapchainCreateInfoKHR,
    VkTilePropertiesQCOM,
    VkValidationCacheCreateInfoEXT,
    VkVertexInputAttributeDescription2EXT,
    VkVertexInputBindingDescription2EXT,
    VkViSurfaceCreateInfoNN,
    VkVideoBeginCodingInfoKHR,
    VkVideoCapabilitiesKHR,
    VkVideoCodingControlInfoKHR,
    VkVideoDecodeInfoKHR,
    VkVideoEncodeInfoKHR,
    VkVideoEncodeQualityLevelPropertiesKHR,
    VkVideoEncodeSessionParametersFeedbackInfoKHR,
    VkVideoEncodeSessionParametersGetInfoKHR,
    VkVideoEndCodingInfoKHR,
    VkVideoFormatPropertiesKHR,
    VkVideoProfileInfoKHR,
    VkVideoSessionCreateInfoKHR,
    VkVideoSessionMemoryRequirementsKHR,
    VkVideoSessionParametersCreateInfoKHR,
    VkVideoSessionParametersUpdateInfoKHR,
    VkViewport,
    VkViewportSwizzleNV,
    VkViewportWScalingNV,
    VkWaylandSurfaceCreateInfoKHR,
    VkWin32SurfaceCreateInfoKHR,
    VkWriteDescriptorSet,
    VkXcbSurfaceCreateInfoKHR,
    VkXlibSurfaceCreateInfoKHR,
)
from .vulkan_callback import (
    vkVoidFunction,
)

vkAcquireDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p)
vkAcquireFullScreenExclusiveModeEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkAcquireImageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkAcquireNextImage2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAcquireNextImageInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkAcquireNextImageKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkAcquirePerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceConfigurationAcquireInfoINTEL), ctypes.POINTER(ctypes.c_void_p))
vkAcquireProfilingLockKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAcquireProfilingLockInfoKHR))
vkAcquireWinrtDisplayNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkAcquireXlibDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
vkAllocateCommandBuffers = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandBufferAllocateInfo), ctypes.POINTER(ctypes.c_void_p))
vkAllocateDescriptorSets = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetAllocateInfo), ctypes.POINTER(ctypes.c_void_p))
vkAllocateMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryAllocateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkBeginCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandBufferBeginInfo))
vkBindAccelerationStructureMemoryNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindAccelerationStructureMemoryInfoNV))
vkBindBufferMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkBindBufferMemory2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindBufferMemoryInfo))
vkBindImageMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkBindImageMemory2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindImageMemoryInfo))
vkBindOpticalFlowSessionImageNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
vkBindVideoSessionMemoryKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindVideoSessionMemoryInfoKHR))
vkBuildAccelerationStructuresKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkBuildMicromapsEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMicromapBuildInfoEXT))
vkCmdBeginConditionalRenderingEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkConditionalRenderingBeginInfoEXT))
vkCmdBeginDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdBeginQuery = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdBeginQueryIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdBeginRenderPass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.c_int)
vkCmdBeginRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.POINTER(VkSubpassBeginInfo))
vkCmdBeginRendering = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo))
vkCmdBeginTransformFeedbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdBeginVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoBeginCodingInfoKHR))
vkCmdBindDescriptorBufferEmbeddedSamplers2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorBufferEmbeddedSamplersInfoEXT))
vkCmdBindDescriptorBufferEmbeddedSamplersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdBindDescriptorBuffersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDescriptorBufferBindingInfoEXT))
vkCmdBindDescriptorSets = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdBindDescriptorSets2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorSetsInfoKHR))
vkCmdBindIndexBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_int)
vkCmdBindIndexBuffer2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_int)
vkCmdBindInvocationMaskHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkCmdBindPipeline = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
vkCmdBindPipelineShaderGroupNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdBindShadersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkCmdBindShadingRateImageNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkCmdBindTransformFeedbackBuffersEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkCmdBindVertexBuffers = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdBindVertexBuffers2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkCmdBlitImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageBlit), ctypes.c_int)
vkCmdBlitImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBlitImageInfo2))
vkCmdBuildAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureInfoNV), ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdBuildAccelerationStructuresIndirectKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint32)))
vkCmdBuildAccelerationStructuresKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
vkCmdBuildMicromapsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMicromapBuildInfoEXT))
vkCmdClearAttachments = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkClearAttachment), ctypes.c_uint32, ctypes.POINTER(VkClearRect))
vkCmdClearColorImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearColorValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdClearDepthStencilImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearDepthStencilValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
vkCmdControlVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoCodingControlInfoKHR))
vkCmdCopyAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCmdCopyAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
vkCmdCopyAccelerationStructureToMemoryKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCmdCopyBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBufferCopy))
vkCmdCopyBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferInfo2))
vkCmdCopyBufferToImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyBufferToImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferToImageInfo2))
vkCmdCopyImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageCopy))
vkCmdCopyImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageInfo2))
vkCmdCopyImageToBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
vkCmdCopyImageToBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToBufferInfo2))
vkCmdCopyMemoryIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdCopyMemoryToAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCmdCopyMemoryToImageIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkImageSubresourceLayers))
vkCmdCopyMemoryToMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToMicromapInfoEXT))
vkCmdCopyMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapInfoEXT))
vkCmdCopyMicromapToMemoryEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
vkCmdCopyQueryPoolResults = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCmdCuLaunchKernelNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCuLaunchInfoNVX))
vkCmdCudaLaunchKernelNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCudaLaunchInfoNV))
vkCmdDebugMarkerBeginEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkCmdDebugMarkerEndEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdDebugMarkerInsertEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerMarkerInfoEXT))
vkCmdDecodeVideoKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoDecodeInfoKHR))
vkCmdDecompressMemoryIndirectCountNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCmdDecompressMemoryNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDecompressMemoryRegionNV))
vkCmdDispatch = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatchBase = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDispatchGraphAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VkDispatchGraphCountInfoAMDX))
vkCmdDispatchGraphIndirectAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VkDispatchGraphCountInfoAMDX))
vkCmdDispatchGraphIndirectCountAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64)
vkCmdDispatchIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdDraw = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawClusterHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawClusterIndirectHUAWEI = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdDrawIndexed = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)
vkCmdDrawIndexedIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndexedIndirectCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirect = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirectByteCountEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawIndirectCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectCountEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectCountNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksIndirectNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMeshTasksNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMultiEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdDrawMultiIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawIndexedInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int32))
vkCmdEncodeVideoKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEncodeInfoKHR))
vkCmdEndConditionalRenderingEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdEndDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdEndQuery = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdEndQueryIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdEndRenderPass = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdEndRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassEndInfo))
vkCmdEndRendering = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdEndTransformFeedbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint64))
vkCmdEndVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEndCodingInfoKHR))
vkCmdExecuteCommands = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkCmdExecuteGeneratedCommandsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdFillBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32)
vkCmdInitializeGraphScratchMemoryAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64)
vkCmdInsertDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkCmdNextSubpass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdNextSubpass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassBeginInfo), ctypes.POINTER(VkSubpassEndInfo))
vkCmdOpticalFlowExecuteNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowExecuteInfoNV))
vkCmdPipelineBarrier = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdPipelineBarrier2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDependencyInfo))
vkCmdPreprocessGeneratedCommandsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsInfoNV))
vkCmdPushConstants = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)
vkCmdPushConstants2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushConstantsInfoKHR))
vkCmdPushDescriptorSet2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetInfoKHR))
vkCmdPushDescriptorSetKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet))
vkCmdPushDescriptorSetWithTemplate2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetWithTemplateInfoKHR))
vkCmdPushDescriptorSetWithTemplateKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkCmdRefreshObjectsKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRefreshObjectListKHR))
vkCmdResetEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdResetEvent2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
vkCmdResetQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdResolveImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageResolve))
vkCmdResolveImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkResolveImageInfo2))
vkCmdSetAlphaToCoverageEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetAlphaToOneEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetAttachmentFeedbackLoopEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetBlendConstants = VKAPI_CALL(None, ctypes.c_void_p, ctypes.ARRAY(ctypes.c_float, 4))
vkCmdSetCheckpointNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p)
vkCmdSetCoarseSampleOrderNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkCoarseSampleOrderCustomNV))
vkCmdSetColorBlendAdvancedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkColorBlendAdvancedEXT))
vkCmdSetColorBlendEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetColorBlendEquationEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkColorBlendEquationEXT))
vkCmdSetColorWriteEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetColorWriteMaskEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetConservativeRasterizationModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetCoverageModulationModeNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetCoverageModulationTableEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageModulationTableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_float))
vkCmdSetCoverageReductionModeNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetCoverageToColorEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCoverageToColorLocationNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetCullMode = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthBias = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)
vkCmdSetDepthBias2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDepthBiasInfoEXT))
vkCmdSetDepthBiasEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthBounds = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)
vkCmdSetDepthBoundsTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthClampEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthClipEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthClipNegativeOneToOneEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthCompareOp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetDepthTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDepthWriteEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDescriptorBufferOffsets2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSetDescriptorBufferOffsetsInfoEXT))
vkCmdSetDescriptorBufferOffsetsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint64))
vkCmdSetDeviceMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDiscardRectangleEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetDiscardRectangleEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetDiscardRectangleModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetEvent2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDependencyInfo))
vkCmdSetExclusiveScissorEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetExclusiveScissorNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetExtraPrimitiveOverestimationSizeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float)
vkCmdSetFragmentShadingRateEnumNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.ARRAY(ctypes.c_int, 2))
vkCmdSetFragmentShadingRateKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExtent2D), ctypes.ARRAY(ctypes.c_int, 2))
vkCmdSetFrontFace = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetLineRasterizationModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetLineStippleEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetLineStippleKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint16)
vkCmdSetLineWidth = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float)
vkCmdSetLogicOpEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetLogicOpEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetPatchControlPointsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetPerformanceMarkerINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceMarkerInfoINTEL))
vkCmdSetPerformanceOverrideINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceOverrideInfoINTEL))
vkCmdSetPerformanceStreamMarkerINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceStreamMarkerInfoINTEL))
vkCmdSetPolygonModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetPrimitiveRestartEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetPrimitiveTopology = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetProvokingVertexModeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetRasterizationSamplesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetRasterizationStreamEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetRasterizerDiscardEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetRayTracingPipelineStackSizeKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetRenderingAttachmentLocationsKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingAttachmentLocationInfoKHR))
vkCmdSetRenderingInputAttachmentIndicesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInputAttachmentIndexInfoKHR))
vkCmdSetRepresentativeFragmentTestEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetSampleLocationsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSampleLocationsInfoEXT))
vkCmdSetSampleLocationsEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetSampleMaskEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkCmdSetScissor = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetScissorWithCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
vkCmdSetShadingRateImageEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetStencilCompareMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetStencilOp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
vkCmdSetStencilReference = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetStencilTestEnable = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetStencilWriteMask = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkCmdSetTessellationDomainOriginEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
vkCmdSetVertexInputEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkVertexInputBindingDescription2EXT), ctypes.c_uint32, ctypes.POINTER(VkVertexInputAttributeDescription2EXT))
vkCmdSetViewport = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSetViewportShadingRatePaletteNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkShadingRatePaletteNV))
vkCmdSetViewportSwizzleNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportSwizzleNV))
vkCmdSetViewportWScalingEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
vkCmdSetViewportWScalingNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportWScalingNV))
vkCmdSetViewportWithCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkViewport))
vkCmdSubpassShadingHUAWEI = VKAPI_CALL(None, ctypes.c_void_p)
vkCmdTraceRaysIndirect2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64)
vkCmdTraceRaysIndirectKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint64)
vkCmdTraceRaysKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdTraceRaysNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
vkCmdUpdateBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p)
vkCmdUpdatePipelineIndirectBufferNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
vkCmdWaitEvents = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
vkCmdWaitEvents2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(VkDependencyInfo))
vkCmdWriteAccelerationStructuresPropertiesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteAccelerationStructuresPropertiesNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteBufferMarker2AMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkCmdWriteBufferMarkerAMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkCmdWriteMicromapsPropertiesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteTimestamp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkCmdWriteTimestamp2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint32)
vkCompileDeferredNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkCopyAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
vkCopyAccelerationStructureToMemoryKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureToMemoryInfoKHR))
vkCopyImageToImageEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToImageInfoEXT))
vkCopyImageToMemoryEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToMemoryInfoEXT))
vkCopyMemoryToAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
vkCopyMemoryToImageEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToImageInfoEXT))
vkCopyMemoryToMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToMicromapInfoEXT))
vkCopyMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapInfoEXT))
vkCopyMicromapToMemoryEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
vkCreateAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateAccelerationStructureNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateAndroidSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAndroidSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateBufferCollectionFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCollectionCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateBufferView = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCommandPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCommandPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateComputePipelines = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCuFunctionNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuFunctionCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCuModuleNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuModuleCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCudaFunctionNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaFunctionCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateCudaModuleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaModuleCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDebugReportCallbackEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugReportCallbackCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDebugUtilsMessengerEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsMessengerCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDeferredOperationKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDescriptorPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDescriptorSetLayout = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDescriptorUpdateTemplate = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorUpdateTemplateCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDevice = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDirectFBSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDirectFBSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDisplayModeKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayModeCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateDisplayPlaneSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplaySurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkEventCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateExecutionGraphPipelinesAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkExecutionGraphPipelineCreateInfoAMDX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateFence = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateFramebuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFramebufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateGraphicsPipelines = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkGraphicsPipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateHeadlessSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkHeadlessSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateIOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateImage = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateImagePipeSurfaceFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImagePipeSurfaceCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateImageView = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateIndirectCommandsLayoutNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIndirectCommandsLayoutCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateInstance = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(VkInstanceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateMacOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMacOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateMetalSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMetalSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMicromapCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateOpticalFlowSessionNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowSessionCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreatePipelineCache = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineCacheCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreatePipelineLayout = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreatePrivateDataSlot = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPrivateDataSlotCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateQueryPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateRayTracingPipelinesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateRayTracingPipelinesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateRenderPass = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateRenderPass2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo2), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSampler = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSamplerYcbcrConversion = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerYcbcrConversionCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateScreenSurfaceQNX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkScreenSurfaceCreateInfoQNX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSemaphore = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSemaphoreSciSyncPoolNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreSciSyncPoolCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateShaderModule = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateShadersEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkShaderCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSharedSwapchainsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateStreamDescriptorSurfaceGGP = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkStreamDescriptorSurfaceCreateInfoGGP), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSwapchainKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateValidationCacheEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkValidationCacheCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateViSurfaceNN = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkViSurfaceCreateInfoNN), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateVideoSessionKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateWaylandSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkWaylandSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateWin32SurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkWin32SurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateXcbSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkXcbSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateXlibSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkXlibSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkDebugMarkerSetObjectNameEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerObjectNameInfoEXT))
vkDebugMarkerSetObjectTagEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerObjectTagInfoEXT))
vkDebugReportMessageEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p)
vkDeferredOperationJoinKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkDestroyAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyBuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyBufferCollectionFUCHSIA = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyBufferView = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCommandPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCuFunctionNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCuModuleNVX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCudaFunctionNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyCudaModuleNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDebugReportCallbackEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDebugUtilsMessengerEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDeferredOperationKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorSetLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDescriptorUpdateTemplate = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyDevice = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyEvent = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyFence = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyFramebuffer = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyImageView = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyIndirectCommandsLayoutNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyInstance = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyMicromapEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyOpticalFlowSessionNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipeline = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipelineCache = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPipelineLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyPrivateDataSlot = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyRenderPass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySampler = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySamplerYcbcrConversion = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySemaphore = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySemaphoreSciSyncPoolNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyShaderEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyShaderModule = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySurfaceKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroySwapchainKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyValidationCacheEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyVideoSessionKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDestroyVideoSessionParametersKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkDeviceWaitIdle = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkDisplayPowerControlEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayPowerInfoEXT))
vkEndCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkEnumerateDeviceExtensionProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkEnumerateDeviceLayerProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateInstanceExtensionProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
vkEnumerateInstanceLayerProperties = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
vkEnumerateInstanceVersion = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32))
vkEnumeratePhysicalDeviceGroups = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceGroupProperties))
vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPerformanceCounterKHR), ctypes.POINTER(VkPerformanceCounterDescriptionKHR))
vkEnumeratePhysicalDevices = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkExportMetalObjectsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExportMetalObjectsInfoEXT))
vkFlushMappedMemoryRanges = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkFreeCommandBuffers = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkFreeDescriptorSets = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkFreeMemory = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
vkGetAccelerationStructureBuildSizesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkAccelerationStructureBuildSizesInfoKHR))
vkGetAccelerationStructureDeviceAddressKHR = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureDeviceAddressInfoKHR))
vkGetAccelerationStructureHandleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p)
vkGetAccelerationStructureMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetAndroidHardwareBufferPropertiesANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAndroidHardwareBufferPropertiesANDROID))
vkGetBufferCollectionPropertiesFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkBufferCollectionPropertiesFUCHSIA))
vkGetBufferDeviceAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkGetBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkMemoryRequirements))
vkGetBufferMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBufferMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetBufferOpaqueCaptureAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkBufferDeviceAddressInfo))
vkGetBufferOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetCalibratedTimestampsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkCalibratedTimestampInfoKHR), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkGetCommandPoolMemoryConsumption = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCommandPoolMemoryConsumption))
vkGetCudaModuleCacheNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetDeferredOperationMaxConcurrencyKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p)
vkGetDeferredOperationResultKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetDescriptorEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorGetInfoEXT), ctypes.c_size_t, ctypes.c_void_p)
vkGetDescriptorSetHostMappingVALVE = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
vkGetDescriptorSetLayoutBindingOffsetEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64))
vkGetDescriptorSetLayoutHostMappingInfoVALVE = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetBindingReferenceVALVE), ctypes.POINTER(VkDescriptorSetLayoutHostMappingInfoVALVE))
vkGetDescriptorSetLayoutSizeEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetDescriptorSetLayoutSupport = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkDescriptorSetLayoutSupport))
vkGetDeviceAccelerationStructureCompatibilityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureVersionInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetDeviceBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceBufferMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
vkGetDeviceFaultInfoEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceFaultCountsEXT), ctypes.POINTER(VkDeviceFaultInfoEXT))
vkGetDeviceGroupPeerMemoryFeatures = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
vkGetDeviceGroupPresentCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceGroupPresentCapabilitiesKHR))
vkGetDeviceGroupSurfacePresentModes2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32))
vkGetDeviceGroupSurfacePresentModesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkGetDeviceImageMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
vkGetDeviceImageSparseMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
vkGetDeviceImageSubresourceLayoutKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageSubresourceInfoKHR), ctypes.POINTER(VkSubresourceLayout2KHR))
vkGetDeviceMemoryCommitment = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetDeviceMemoryOpaqueCaptureAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkDeviceMemoryOpaqueCaptureAddressInfo))
vkGetDeviceMicromapCompatibilityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkMicromapVersionInfoEXT), ctypes.POINTER(ctypes.c_int))
vkGetDeviceProcAddr = VKAPI_CALL(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)
vkGetDeviceQueue = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetDeviceQueue2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceQueueInfo2), ctypes.POINTER(ctypes.c_void_p))
vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExtent2D))
vkGetDisplayModeProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModeProperties2KHR))
vkGetDisplayModePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModePropertiesKHR))
vkGetDisplayPlaneCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplayPlaneInfo2KHR), ctypes.POINTER(VkDisplayPlaneCapabilities2KHR))
vkGetDisplayPlaneCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDisplayPlaneCapabilitiesKHR))
vkGetDisplayPlaneSupportedDisplaysKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkGetDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetDynamicRenderingTilePropertiesQCOM = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo), ctypes.POINTER(VkTilePropertiesQCOM))
vkGetEncodedVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoEncodeSessionParametersGetInfoKHR), ctypes.POINTER(VkVideoEncodeSessionParametersFeedbackInfoKHR), ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetEventStatus = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetExecutionGraphPipelineNodeIndexAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkPipelineShaderStageNodeCreateInfoAMDX), ctypes.POINTER(ctypes.c_uint32))
vkGetExecutionGraphPipelineScratchSizeAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExecutionGraphPipelineScratchSizeAMDX))
vkGetFaultData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkFaultData))
vkGetFenceFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetFenceSciSyncFenceNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetSciSyncInfoNV), ctypes.c_void_p)
vkGetFenceSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetSciSyncInfoNV), ctypes.c_void_p)
vkGetFenceStatus = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkGetFramebufferTilePropertiesQCOM = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkTilePropertiesQCOM))
vkGetGeneratedCommandsMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
vkGetImageDrmFormatModifierPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageDrmFormatModifierPropertiesEXT))
vkGetImageMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkMemoryRequirements))
vkGetImageMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
vkGetImageOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetImageSparseMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements))
vkGetImageSparseMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageSparseMemoryRequirementsInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
vkGetImageSubresourceLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource), ctypes.POINTER(VkSubresourceLayout))
vkGetImageSubresourceLayout2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource2KHR), ctypes.POINTER(VkSubresourceLayout2KHR))
vkGetImageViewAddressNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageViewAddressPropertiesNVX))
vkGetImageViewHandleNVX = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkImageViewHandleInfoNVX))
vkGetImageViewOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageViewCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetInstanceProcAddr = VKAPI_CALL(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)
vkGetLatencyTimingsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkGetLatencyMarkerInfoNV))
vkGetMemoryAndroidHardwareBufferANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetAndroidHardwareBufferInfoANDROID), ctypes.POINTER(ctypes.c_void_p))
vkGetMemoryFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetMemoryFdPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(VkMemoryFdPropertiesKHR))
vkGetMemoryHostPointerPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemoryHostPointerPropertiesEXT))
vkGetMemoryRemoteAddressNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetRemoteAddressInfoNV), ctypes.POINTER(ctypes.c_void_p))
vkGetMemorySciBufNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetSciBufInfoNV), ctypes.POINTER(ctypes.c_void_p))
vkGetMemoryWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkGetMemoryWin32HandleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetMemoryWin32HandlePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemoryWin32HandlePropertiesKHR))
vkGetMemoryZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
vkGetMemoryZirconHandlePropertiesFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryZirconHandlePropertiesFUCHSIA))
vkGetMicromapBuildSizesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkMicromapBuildInfoEXT), ctypes.POINTER(VkMicromapBuildSizesInfoEXT))
vkGetPastPresentationTimingGOOGLE = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPastPresentationTimingGOOGLE))
vkGetPerformanceParameterINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkPerformanceValueINTEL))
vkGetPhysicalDeviceCalibrateableTimeDomainsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetPhysicalDeviceCooperativeMatrixPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCooperativeMatrixPropertiesKHR))
vkGetPhysicalDeviceCooperativeMatrixPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCooperativeMatrixPropertiesNV))
vkGetPhysicalDeviceDirectFBPresentationSupportEXT = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkGetPhysicalDeviceDisplayPlaneProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlaneProperties2KHR))
vkGetPhysicalDeviceDisplayPlanePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlanePropertiesKHR))
vkGetPhysicalDeviceDisplayProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayProperties2KHR))
vkGetPhysicalDeviceDisplayPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPropertiesKHR))
vkGetPhysicalDeviceExternalBufferProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalBufferInfo), ctypes.POINTER(VkExternalBufferProperties))
vkGetPhysicalDeviceExternalFenceProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalFenceInfo), ctypes.POINTER(VkExternalFenceProperties))
vkGetPhysicalDeviceExternalImageFormatPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkExternalImageFormatPropertiesNV))
vkGetPhysicalDeviceExternalMemorySciBufPropertiesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemorySciBufPropertiesNV))
vkGetPhysicalDeviceExternalSemaphoreProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalSemaphoreInfo), ctypes.POINTER(VkExternalSemaphoreProperties))
vkGetPhysicalDeviceFeatures = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures))
vkGetPhysicalDeviceFeatures2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures2))
vkGetPhysicalDeviceFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties))
vkGetPhysicalDeviceFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties2))
vkGetPhysicalDeviceFragmentShadingRatesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceFragmentShadingRateKHR))
vkGetPhysicalDeviceImageFormatProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkImageFormatProperties))
vkGetPhysicalDeviceImageFormatProperties2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceImageFormatInfo2), ctypes.POINTER(VkImageFormatProperties2))
vkGetPhysicalDeviceMemoryProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties))
vkGetPhysicalDeviceMemoryProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties2))
vkGetPhysicalDeviceMultisamplePropertiesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultisamplePropertiesEXT))
vkGetPhysicalDeviceOpticalFlowImageFormatsNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowImageFormatInfoNV), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkOpticalFlowImageFormatPropertiesNV))
vkGetPhysicalDevicePresentRectanglesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkRect2D))
vkGetPhysicalDeviceProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceProperties))
vkGetPhysicalDeviceProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceProperties2))
vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolPerformanceCreateInfoKHR), ctypes.POINTER(ctypes.c_uint32))
vkGetPhysicalDeviceQueueFamilyProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties))
vkGetPhysicalDeviceQueueFamilyProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties2))
vkGetPhysicalDeviceRefreshableObjectTypesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetPhysicalDeviceSciBufAttributesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetPhysicalDeviceSciSyncAttributesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSciSyncAttributesInfoNV), ctypes.c_void_p)
vkGetPhysicalDeviceScreenPresentationSupportQNX = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkGetPhysicalDeviceSparseImageFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties))
vkGetPhysicalDeviceSparseImageFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSparseImageFormatInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties2))
vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkFramebufferMixedSamplesCombinationNV))
vkGetPhysicalDeviceSurfaceCapabilities2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSurfaceCapabilities2EXT))
vkGetPhysicalDeviceSurfaceCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(VkSurfaceCapabilities2KHR))
vkGetPhysicalDeviceSurfaceCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSurfaceCapabilitiesKHR))
vkGetPhysicalDeviceSurfaceFormats2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormat2KHR))
vkGetPhysicalDeviceSurfaceFormatsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormatKHR))
vkGetPhysicalDeviceSurfacePresentModes2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetPhysicalDeviceSurfacePresentModesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
vkGetPhysicalDeviceSurfaceSupportKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
vkGetPhysicalDeviceToolProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPhysicalDeviceToolProperties))
vkGetPhysicalDeviceVideoCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoProfileInfoKHR), ctypes.POINTER(VkVideoCapabilitiesKHR))
vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR), ctypes.POINTER(VkVideoEncodeQualityLevelPropertiesKHR))
vkGetPhysicalDeviceVideoFormatPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoFormatInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkVideoFormatPropertiesKHR))
vkGetPhysicalDeviceWaylandPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
vkGetPhysicalDeviceWin32PresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkGetPhysicalDeviceXcbPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkGetPhysicalDeviceXlibPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
vkGetPipelineCacheData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetPipelineExecutableInternalRepresentationsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableInternalRepresentationKHR))
vkGetPipelineExecutablePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutablePropertiesKHR))
vkGetPipelineExecutableStatisticsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableStatisticKHR))
vkGetPipelineIndirectDeviceAddressNV = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkPipelineIndirectDeviceAddressInfoNV))
vkGetPipelineIndirectMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkMemoryRequirements2))
vkGetPipelinePropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(VkBaseOutStructure))
vkGetPrivateData = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetQueryPoolResults = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32)
vkGetQueueCheckpointData2NV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointData2NV))
vkGetQueueCheckpointDataNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointDataNV))
vkGetRandROutputDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkGetRayTracingCaptureReplayShaderGroupHandlesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetRayTracingShaderGroupHandlesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.c_void_p)
vkGetRayTracingShaderGroupStackSizeKHR = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int)
vkGetRefreshCycleDurationGOOGLE = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkRefreshCycleDurationGOOGLE))
vkGetRenderAreaGranularity = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExtent2D))
vkGetRenderingAreaGranularityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingAreaInfoKHR), ctypes.POINTER(VkExtent2D))
vkGetSamplerOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
vkGetScreenBufferPropertiesQNX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkScreenBufferPropertiesQNX))
vkGetSemaphoreCounterValue = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
vkGetSemaphoreFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
vkGetSemaphoreSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetSciSyncInfoNV), ctypes.c_void_p)
vkGetSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkGetSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
vkGetShaderBinaryDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetShaderInfoAMD = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetShaderModuleCreateInfoIdentifierEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkShaderModuleIdentifierEXT))
vkGetShaderModuleIdentifierEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleIdentifierEXT))
vkGetSwapchainCounterEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64))
vkGetSwapchainGrallocUsage2ANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
vkGetSwapchainGrallocUsageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int))
vkGetSwapchainImagesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_void_p))
vkGetSwapchainStatusKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkGetValidationCacheDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
vkGetVideoSessionMemoryRequirementsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkVideoSessionMemoryRequirementsKHR))
vkGetWinrtDisplayNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkImportFenceFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceFdInfoKHR))
vkImportFenceSciSyncFenceNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceSciSyncInfoNV))
vkImportFenceSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceSciSyncInfoNV))
vkImportFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceWin32HandleInfoKHR))
vkImportSemaphoreFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreFdInfoKHR))
vkImportSemaphoreSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreSciSyncInfoNV))
vkImportSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreWin32HandleInfoKHR))
vkImportSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreZirconHandleInfoFUCHSIA))
vkInitializePerformanceApiINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkInitializePerformanceApiInfoINTEL))
vkInvalidateMappedMemoryRanges = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMappedMemoryRange))
vkLatencySleepNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkLatencySleepInfoNV))
vkMapMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkMapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryMapInfoKHR), ctypes.POINTER(ctypes.c_void_p))
vkMergePipelineCaches = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkMergeValidationCachesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkQueueBeginDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkQueueBindSparse = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindSparseInfo), ctypes.c_void_p)
vkQueueEndDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p)
vkQueueInsertDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsLabelEXT))
vkQueueNotifyOutOfBandNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkOutOfBandQueueTypeInfoNV))
vkQueuePresentKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPresentInfoKHR))
vkQueueSetPerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkQueueSignalReleaseImageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))
vkQueueSubmit = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo), ctypes.c_void_p)
vkQueueSubmit2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo2), ctypes.c_void_p)
vkQueueWaitIdle = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p)
vkRegisterDeviceEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkRegisterDisplayEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkReleaseDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkReleaseFullScreenExclusiveModeEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkReleasePerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkReleaseProfilingLockKHR = VKAPI_CALL(None, ctypes.c_void_p)
vkReleaseSwapchainImagesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkReleaseSwapchainImagesInfoEXT))
vkResetCommandBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
vkResetCommandPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkResetDescriptorPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkResetEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkResetFences = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
vkResetQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32)
vkSetBufferCollectionBufferConstraintsFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkBufferConstraintsInfoFUCHSIA))
vkSetBufferCollectionImageConstraintsFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageConstraintsInfoFUCHSIA))
vkSetDebugUtilsObjectNameEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT))
vkSetDebugUtilsObjectTagEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsObjectTagInfoEXT))
vkSetDeviceMemoryPriorityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)
vkSetEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
vkSetHdrMetadataEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(VkHdrMetadataEXT))
vkSetLatencyMarkerNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkSetLatencyMarkerInfoNV))
vkSetLatencySleepModeNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkLatencySleepModeInfoNV))
vkSetLocalDimmingAMD = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkSetPrivateData = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint64)
vkSignalSemaphore = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreSignalInfo))
vkSubmitDebugUtilsMessageEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT))
vkTransitionImageLayoutEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkHostImageLayoutTransitionInfoEXT))
vkTrimCommandPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
vkUninitializePerformanceApiINTEL = VKAPI_CALL(None, ctypes.c_void_p)
vkUnmapMemory = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p)
vkUnmapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryUnmapInfoKHR))
vkUpdateDescriptorSetWithTemplate = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
vkUpdateDescriptorSets = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet), ctypes.c_uint32, ctypes.POINTER(VkCopyDescriptorSet))
vkUpdateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersUpdateInfoKHR))
vkWaitForFences = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_uint64)
vkWaitForPresentKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64)
vkWaitSemaphores = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreWaitInfo), ctypes.c_uint64)
vkWriteAccelerationStructuresPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)
vkWriteMicromapsPropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)

vkBindBufferMemory2KHR = vkBindBufferMemory2
vkBindImageMemory2KHR = vkBindImageMemory2
vkCmdBeginRenderPass2KHR = vkCmdBeginRenderPass2
vkCmdBeginRenderingKHR = vkCmdBeginRendering
vkCmdBindVertexBuffers2EXT = vkCmdBindVertexBuffers2
vkCmdBlitImage2KHR = vkCmdBlitImage2
vkCmdCopyBuffer2KHR = vkCmdCopyBuffer2
vkCmdCopyBufferToImage2KHR = vkCmdCopyBufferToImage2
vkCmdCopyImage2KHR = vkCmdCopyImage2
vkCmdCopyImageToBuffer2KHR = vkCmdCopyImageToBuffer2
vkCmdDispatchBaseKHR = vkCmdDispatchBase
vkCmdDrawIndexedIndirectCountAMD = vkCmdDrawIndexedIndirectCount
vkCmdDrawIndexedIndirectCountKHR = vkCmdDrawIndexedIndirectCount
vkCmdDrawIndirectCountAMD = vkCmdDrawIndirectCount
vkCmdDrawIndirectCountKHR = vkCmdDrawIndirectCount
vkCmdEndRenderPass2KHR = vkCmdEndRenderPass2
vkCmdEndRenderingKHR = vkCmdEndRendering
vkCmdNextSubpass2KHR = vkCmdNextSubpass2
vkCmdPipelineBarrier2KHR = vkCmdPipelineBarrier2
vkCmdResetEvent2KHR = vkCmdResetEvent2
vkCmdResolveImage2KHR = vkCmdResolveImage2
vkCmdSetCullModeEXT = vkCmdSetCullMode
vkCmdSetDepthBiasEnableEXT = vkCmdSetDepthBiasEnable
vkCmdSetDepthBoundsTestEnableEXT = vkCmdSetDepthBoundsTestEnable
vkCmdSetDepthCompareOpEXT = vkCmdSetDepthCompareOp
vkCmdSetDepthTestEnableEXT = vkCmdSetDepthTestEnable
vkCmdSetDepthWriteEnableEXT = vkCmdSetDepthWriteEnable
vkCmdSetDeviceMaskKHR = vkCmdSetDeviceMask
vkCmdSetEvent2KHR = vkCmdSetEvent2
vkCmdSetFrontFaceEXT = vkCmdSetFrontFace
vkCmdSetLineStippleEXT = vkCmdSetLineStippleKHR
vkCmdSetPrimitiveRestartEnableEXT = vkCmdSetPrimitiveRestartEnable
vkCmdSetPrimitiveTopologyEXT = vkCmdSetPrimitiveTopology
vkCmdSetRasterizerDiscardEnableEXT = vkCmdSetRasterizerDiscardEnable
vkCmdSetScissorWithCountEXT = vkCmdSetScissorWithCount
vkCmdSetStencilOpEXT = vkCmdSetStencilOp
vkCmdSetStencilTestEnableEXT = vkCmdSetStencilTestEnable
vkCmdSetViewportWithCountEXT = vkCmdSetViewportWithCount
vkCmdWaitEvents2KHR = vkCmdWaitEvents2
vkCmdWriteTimestamp2KHR = vkCmdWriteTimestamp2
vkCreateDescriptorUpdateTemplateKHR = vkCreateDescriptorUpdateTemplate
vkCreatePrivateDataSlotEXT = vkCreatePrivateDataSlot
vkCreateRenderPass2KHR = vkCreateRenderPass2
vkCreateSamplerYcbcrConversionKHR = vkCreateSamplerYcbcrConversion
vkDestroyDescriptorUpdateTemplateKHR = vkDestroyDescriptorUpdateTemplate
vkDestroyPrivateDataSlotEXT = vkDestroyPrivateDataSlot
vkDestroySamplerYcbcrConversionKHR = vkDestroySamplerYcbcrConversion
vkEnumeratePhysicalDeviceGroupsKHR = vkEnumeratePhysicalDeviceGroups
vkGetBufferDeviceAddressEXT = vkGetBufferDeviceAddress
vkGetBufferDeviceAddressKHR = vkGetBufferDeviceAddress
vkGetBufferMemoryRequirements2KHR = vkGetBufferMemoryRequirements2
vkGetBufferOpaqueCaptureAddressKHR = vkGetBufferOpaqueCaptureAddress
vkGetCalibratedTimestampsEXT = vkGetCalibratedTimestampsKHR
vkGetDescriptorSetLayoutSupportKHR = vkGetDescriptorSetLayoutSupport
vkGetDeviceBufferMemoryRequirementsKHR = vkGetDeviceBufferMemoryRequirements
vkGetDeviceGroupPeerMemoryFeaturesKHR = vkGetDeviceGroupPeerMemoryFeatures
vkGetDeviceImageMemoryRequirementsKHR = vkGetDeviceImageMemoryRequirements
vkGetDeviceImageSparseMemoryRequirementsKHR = vkGetDeviceImageSparseMemoryRequirements
vkGetDeviceMemoryOpaqueCaptureAddressKHR = vkGetDeviceMemoryOpaqueCaptureAddress
vkGetImageMemoryRequirements2KHR = vkGetImageMemoryRequirements2
vkGetImageSparseMemoryRequirements2KHR = vkGetImageSparseMemoryRequirements2
vkGetImageSubresourceLayout2EXT = vkGetImageSubresourceLayout2KHR
vkGetPhysicalDeviceCalibrateableTimeDomainsEXT = vkGetPhysicalDeviceCalibrateableTimeDomainsKHR
vkGetPhysicalDeviceExternalBufferPropertiesKHR = vkGetPhysicalDeviceExternalBufferProperties
vkGetPhysicalDeviceExternalFencePropertiesKHR = vkGetPhysicalDeviceExternalFenceProperties
vkGetPhysicalDeviceExternalSemaphorePropertiesKHR = vkGetPhysicalDeviceExternalSemaphoreProperties
vkGetPhysicalDeviceFeatures2KHR = vkGetPhysicalDeviceFeatures2
vkGetPhysicalDeviceFormatProperties2KHR = vkGetPhysicalDeviceFormatProperties2
vkGetPhysicalDeviceImageFormatProperties2KHR = vkGetPhysicalDeviceImageFormatProperties2
vkGetPhysicalDeviceMemoryProperties2KHR = vkGetPhysicalDeviceMemoryProperties2
vkGetPhysicalDeviceProperties2KHR = vkGetPhysicalDeviceProperties2
vkGetPhysicalDeviceQueueFamilyProperties2KHR = vkGetPhysicalDeviceQueueFamilyProperties2
vkGetPhysicalDeviceSparseImageFormatProperties2KHR = vkGetPhysicalDeviceSparseImageFormatProperties2
vkGetPhysicalDeviceToolPropertiesEXT = vkGetPhysicalDeviceToolProperties
vkGetPrivateDataEXT = vkGetPrivateData
vkGetRayTracingShaderGroupHandlesNV = vkGetRayTracingShaderGroupHandlesKHR
vkGetSemaphoreCounterValueKHR = vkGetSemaphoreCounterValue
vkQueueSubmit2KHR = vkQueueSubmit2
vkResetQueryPoolEXT = vkResetQueryPool
vkSetPrivateDataEXT = vkSetPrivateData
vkSignalSemaphoreKHR = vkSignalSemaphore
vkTrimCommandPoolKHR = vkTrimCommandPool
vkUpdateDescriptorSetWithTemplateKHR = vkUpdateDescriptorSetWithTemplate
vkWaitSemaphoresKHR = vkWaitSemaphores

__all__ = [
    'vkAcquireDrmDisplayEXT',
    'vkAcquireFullScreenExclusiveModeEXT',
    'vkAcquireImageANDROID',
    'vkAcquireNextImage2KHR',
    'vkAcquireNextImageKHR',
    'vkAcquirePerformanceConfigurationINTEL',
    'vkAcquireProfilingLockKHR',
    'vkAcquireWinrtDisplayNV',
    'vkAcquireXlibDisplayEXT',
    'vkAllocateCommandBuffers',
    'vkAllocateDescriptorSets',
    'vkAllocateMemory',
    'vkBeginCommandBuffer',
    'vkBindAccelerationStructureMemoryNV',
    'vkBindBufferMemory',
    'vkBindBufferMemory2',
    'vkBindBufferMemory2KHR',
    'vkBindImageMemory',
    'vkBindImageMemory2',
    'vkBindImageMemory2KHR',
    'vkBindOpticalFlowSessionImageNV',
    'vkBindVideoSessionMemoryKHR',
    'vkBuildAccelerationStructuresKHR',
    'vkBuildMicromapsEXT',
    'vkCmdBeginConditionalRenderingEXT',
    'vkCmdBeginDebugUtilsLabelEXT',
    'vkCmdBeginQuery',
    'vkCmdBeginQueryIndexedEXT',
    'vkCmdBeginRenderPass',
    'vkCmdBeginRenderPass2',
    'vkCmdBeginRenderPass2KHR',
    'vkCmdBeginRendering',
    'vkCmdBeginRenderingKHR',
    'vkCmdBeginTransformFeedbackEXT',
    'vkCmdBeginVideoCodingKHR',
    'vkCmdBindDescriptorBufferEmbeddedSamplers2EXT',
    'vkCmdBindDescriptorBufferEmbeddedSamplersEXT',
    'vkCmdBindDescriptorBuffersEXT',
    'vkCmdBindDescriptorSets',
    'vkCmdBindDescriptorSets2KHR',
    'vkCmdBindIndexBuffer',
    'vkCmdBindIndexBuffer2KHR',
    'vkCmdBindInvocationMaskHUAWEI',
    'vkCmdBindPipeline',
    'vkCmdBindPipelineShaderGroupNV',
    'vkCmdBindShadersEXT',
    'vkCmdBindShadingRateImageNV',
    'vkCmdBindTransformFeedbackBuffersEXT',
    'vkCmdBindVertexBuffers',
    'vkCmdBindVertexBuffers2',
    'vkCmdBindVertexBuffers2EXT',
    'vkCmdBlitImage',
    'vkCmdBlitImage2',
    'vkCmdBlitImage2KHR',
    'vkCmdBuildAccelerationStructureNV',
    'vkCmdBuildAccelerationStructuresIndirectKHR',
    'vkCmdBuildAccelerationStructuresKHR',
    'vkCmdBuildMicromapsEXT',
    'vkCmdClearAttachments',
    'vkCmdClearColorImage',
    'vkCmdClearDepthStencilImage',
    'vkCmdControlVideoCodingKHR',
    'vkCmdCopyAccelerationStructureKHR',
    'vkCmdCopyAccelerationStructureNV',
    'vkCmdCopyAccelerationStructureToMemoryKHR',
    'vkCmdCopyBuffer',
    'vkCmdCopyBuffer2',
    'vkCmdCopyBuffer2KHR',
    'vkCmdCopyBufferToImage',
    'vkCmdCopyBufferToImage2',
    'vkCmdCopyBufferToImage2KHR',
    'vkCmdCopyImage',
    'vkCmdCopyImage2',
    'vkCmdCopyImage2KHR',
    'vkCmdCopyImageToBuffer',
    'vkCmdCopyImageToBuffer2',
    'vkCmdCopyImageToBuffer2KHR',
    'vkCmdCopyMemoryIndirectNV',
    'vkCmdCopyMemoryToAccelerationStructureKHR',
    'vkCmdCopyMemoryToImageIndirectNV',
    'vkCmdCopyMemoryToMicromapEXT',
    'vkCmdCopyMicromapEXT',
    'vkCmdCopyMicromapToMemoryEXT',
    'vkCmdCopyQueryPoolResults',
    'vkCmdCuLaunchKernelNVX',
    'vkCmdCudaLaunchKernelNV',
    'vkCmdDebugMarkerBeginEXT',
    'vkCmdDebugMarkerEndEXT',
    'vkCmdDebugMarkerInsertEXT',
    'vkCmdDecodeVideoKHR',
    'vkCmdDecompressMemoryIndirectCountNV',
    'vkCmdDecompressMemoryNV',
    'vkCmdDispatch',
    'vkCmdDispatchBase',
    'vkCmdDispatchBaseKHR',
    'vkCmdDispatchGraphAMDX',
    'vkCmdDispatchGraphIndirectAMDX',
    'vkCmdDispatchGraphIndirectCountAMDX',
    'vkCmdDispatchIndirect',
    'vkCmdDraw',
    'vkCmdDrawClusterHUAWEI',
    'vkCmdDrawClusterIndirectHUAWEI',
    'vkCmdDrawIndexed',
    'vkCmdDrawIndexedIndirect',
    'vkCmdDrawIndexedIndirectCount',
    'vkCmdDrawIndexedIndirectCountAMD',
    'vkCmdDrawIndexedIndirectCountKHR',
    'vkCmdDrawIndirect',
    'vkCmdDrawIndirectByteCountEXT',
    'vkCmdDrawIndirectCount',
    'vkCmdDrawIndirectCountAMD',
    'vkCmdDrawIndirectCountKHR',
    'vkCmdDrawMeshTasksEXT',
    'vkCmdDrawMeshTasksIndirectCountEXT',
    'vkCmdDrawMeshTasksIndirectCountNV',
    'vkCmdDrawMeshTasksIndirectEXT',
    'vkCmdDrawMeshTasksIndirectNV',
    'vkCmdDrawMeshTasksNV',
    'vkCmdDrawMultiEXT',
    'vkCmdDrawMultiIndexedEXT',
    'vkCmdEncodeVideoKHR',
    'vkCmdEndConditionalRenderingEXT',
    'vkCmdEndDebugUtilsLabelEXT',
    'vkCmdEndQuery',
    'vkCmdEndQueryIndexedEXT',
    'vkCmdEndRenderPass',
    'vkCmdEndRenderPass2',
    'vkCmdEndRenderPass2KHR',
    'vkCmdEndRendering',
    'vkCmdEndRenderingKHR',
    'vkCmdEndTransformFeedbackEXT',
    'vkCmdEndVideoCodingKHR',
    'vkCmdExecuteCommands',
    'vkCmdExecuteGeneratedCommandsNV',
    'vkCmdFillBuffer',
    'vkCmdInitializeGraphScratchMemoryAMDX',
    'vkCmdInsertDebugUtilsLabelEXT',
    'vkCmdNextSubpass',
    'vkCmdNextSubpass2',
    'vkCmdNextSubpass2KHR',
    'vkCmdOpticalFlowExecuteNV',
    'vkCmdPipelineBarrier',
    'vkCmdPipelineBarrier2',
    'vkCmdPipelineBarrier2KHR',
    'vkCmdPreprocessGeneratedCommandsNV',
    'vkCmdPushConstants',
    'vkCmdPushConstants2KHR',
    'vkCmdPushDescriptorSet2KHR',
    'vkCmdPushDescriptorSetKHR',
    'vkCmdPushDescriptorSetWithTemplate2KHR',
    'vkCmdPushDescriptorSetWithTemplateKHR',
    'vkCmdRefreshObjectsKHR',
    'vkCmdResetEvent',
    'vkCmdResetEvent2',
    'vkCmdResetEvent2KHR',
    'vkCmdResetQueryPool',
    'vkCmdResolveImage',
    'vkCmdResolveImage2',
    'vkCmdResolveImage2KHR',
    'vkCmdSetAlphaToCoverageEnableEXT',
    'vkCmdSetAlphaToOneEnableEXT',
    'vkCmdSetAttachmentFeedbackLoopEnableEXT',
    'vkCmdSetBlendConstants',
    'vkCmdSetCheckpointNV',
    'vkCmdSetCoarseSampleOrderNV',
    'vkCmdSetColorBlendAdvancedEXT',
    'vkCmdSetColorBlendEnableEXT',
    'vkCmdSetColorBlendEquationEXT',
    'vkCmdSetColorWriteEnableEXT',
    'vkCmdSetColorWriteMaskEXT',
    'vkCmdSetConservativeRasterizationModeEXT',
    'vkCmdSetCoverageModulationModeNV',
    'vkCmdSetCoverageModulationTableEnableNV',
    'vkCmdSetCoverageModulationTableNV',
    'vkCmdSetCoverageReductionModeNV',
    'vkCmdSetCoverageToColorEnableNV',
    'vkCmdSetCoverageToColorLocationNV',
    'vkCmdSetCullMode',
    'vkCmdSetCullModeEXT',
    'vkCmdSetDepthBias',
    'vkCmdSetDepthBias2EXT',
    'vkCmdSetDepthBiasEnable',
    'vkCmdSetDepthBiasEnableEXT',
    'vkCmdSetDepthBounds',
    'vkCmdSetDepthBoundsTestEnable',
    'vkCmdSetDepthBoundsTestEnableEXT',
    'vkCmdSetDepthClampEnableEXT',
    'vkCmdSetDepthClipEnableEXT',
    'vkCmdSetDepthClipNegativeOneToOneEXT',
    'vkCmdSetDepthCompareOp',
    'vkCmdSetDepthCompareOpEXT',
    'vkCmdSetDepthTestEnable',
    'vkCmdSetDepthTestEnableEXT',
    'vkCmdSetDepthWriteEnable',
    'vkCmdSetDepthWriteEnableEXT',
    'vkCmdSetDescriptorBufferOffsets2EXT',
    'vkCmdSetDescriptorBufferOffsetsEXT',
    'vkCmdSetDeviceMask',
    'vkCmdSetDeviceMaskKHR',
    'vkCmdSetDiscardRectangleEXT',
    'vkCmdSetDiscardRectangleEnableEXT',
    'vkCmdSetDiscardRectangleModeEXT',
    'vkCmdSetEvent',
    'vkCmdSetEvent2',
    'vkCmdSetEvent2KHR',
    'vkCmdSetExclusiveScissorEnableNV',
    'vkCmdSetExclusiveScissorNV',
    'vkCmdSetExtraPrimitiveOverestimationSizeEXT',
    'vkCmdSetFragmentShadingRateEnumNV',
    'vkCmdSetFragmentShadingRateKHR',
    'vkCmdSetFrontFace',
    'vkCmdSetFrontFaceEXT',
    'vkCmdSetLineRasterizationModeEXT',
    'vkCmdSetLineStippleEXT',
    'vkCmdSetLineStippleEnableEXT',
    'vkCmdSetLineStippleKHR',
    'vkCmdSetLineWidth',
    'vkCmdSetLogicOpEXT',
    'vkCmdSetLogicOpEnableEXT',
    'vkCmdSetPatchControlPointsEXT',
    'vkCmdSetPerformanceMarkerINTEL',
    'vkCmdSetPerformanceOverrideINTEL',
    'vkCmdSetPerformanceStreamMarkerINTEL',
    'vkCmdSetPolygonModeEXT',
    'vkCmdSetPrimitiveRestartEnable',
    'vkCmdSetPrimitiveRestartEnableEXT',
    'vkCmdSetPrimitiveTopology',
    'vkCmdSetPrimitiveTopologyEXT',
    'vkCmdSetProvokingVertexModeEXT',
    'vkCmdSetRasterizationSamplesEXT',
    'vkCmdSetRasterizationStreamEXT',
    'vkCmdSetRasterizerDiscardEnable',
    'vkCmdSetRasterizerDiscardEnableEXT',
    'vkCmdSetRayTracingPipelineStackSizeKHR',
    'vkCmdSetRenderingAttachmentLocationsKHR',
    'vkCmdSetRenderingInputAttachmentIndicesKHR',
    'vkCmdSetRepresentativeFragmentTestEnableNV',
    'vkCmdSetSampleLocationsEXT',
    'vkCmdSetSampleLocationsEnableEXT',
    'vkCmdSetSampleMaskEXT',
    'vkCmdSetScissor',
    'vkCmdSetScissorWithCount',
    'vkCmdSetScissorWithCountEXT',
    'vkCmdSetShadingRateImageEnableNV',
    'vkCmdSetStencilCompareMask',
    'vkCmdSetStencilOp',
    'vkCmdSetStencilOpEXT',
    'vkCmdSetStencilReference',
    'vkCmdSetStencilTestEnable',
    'vkCmdSetStencilTestEnableEXT',
    'vkCmdSetStencilWriteMask',
    'vkCmdSetTessellationDomainOriginEXT',
    'vkCmdSetVertexInputEXT',
    'vkCmdSetViewport',
    'vkCmdSetViewportShadingRatePaletteNV',
    'vkCmdSetViewportSwizzleNV',
    'vkCmdSetViewportWScalingEnableNV',
    'vkCmdSetViewportWScalingNV',
    'vkCmdSetViewportWithCount',
    'vkCmdSetViewportWithCountEXT',
    'vkCmdSubpassShadingHUAWEI',
    'vkCmdTraceRaysIndirect2KHR',
    'vkCmdTraceRaysIndirectKHR',
    'vkCmdTraceRaysKHR',
    'vkCmdTraceRaysNV',
    'vkCmdUpdateBuffer',
    'vkCmdUpdatePipelineIndirectBufferNV',
    'vkCmdWaitEvents',
    'vkCmdWaitEvents2',
    'vkCmdWaitEvents2KHR',
    'vkCmdWriteAccelerationStructuresPropertiesKHR',
    'vkCmdWriteAccelerationStructuresPropertiesNV',
    'vkCmdWriteBufferMarker2AMD',
    'vkCmdWriteBufferMarkerAMD',
    'vkCmdWriteMicromapsPropertiesEXT',
    'vkCmdWriteTimestamp',
    'vkCmdWriteTimestamp2',
    'vkCmdWriteTimestamp2KHR',
    'vkCompileDeferredNV',
    'vkCopyAccelerationStructureKHR',
    'vkCopyAccelerationStructureToMemoryKHR',
    'vkCopyImageToImageEXT',
    'vkCopyImageToMemoryEXT',
    'vkCopyMemoryToAccelerationStructureKHR',
    'vkCopyMemoryToImageEXT',
    'vkCopyMemoryToMicromapEXT',
    'vkCopyMicromapEXT',
    'vkCopyMicromapToMemoryEXT',
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
    'vkCreateDescriptorUpdateTemplateKHR',
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
    'vkCreatePrivateDataSlotEXT',
    'vkCreateQueryPool',
    'vkCreateRayTracingPipelinesKHR',
    'vkCreateRayTracingPipelinesNV',
    'vkCreateRenderPass',
    'vkCreateRenderPass2',
    'vkCreateRenderPass2KHR',
    'vkCreateSampler',
    'vkCreateSamplerYcbcrConversion',
    'vkCreateSamplerYcbcrConversionKHR',
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
    'vkDebugMarkerSetObjectNameEXT',
    'vkDebugMarkerSetObjectTagEXT',
    'vkDebugReportMessageEXT',
    'vkDeferredOperationJoinKHR',
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
    'vkDestroyDescriptorUpdateTemplateKHR',
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
    'vkDestroyPrivateDataSlotEXT',
    'vkDestroyQueryPool',
    'vkDestroyRenderPass',
    'vkDestroySampler',
    'vkDestroySamplerYcbcrConversion',
    'vkDestroySamplerYcbcrConversionKHR',
    'vkDestroySemaphore',
    'vkDestroySemaphoreSciSyncPoolNV',
    'vkDestroyShaderEXT',
    'vkDestroyShaderModule',
    'vkDestroySurfaceKHR',
    'vkDestroySwapchainKHR',
    'vkDestroyValidationCacheEXT',
    'vkDestroyVideoSessionKHR',
    'vkDestroyVideoSessionParametersKHR',
    'vkDeviceWaitIdle',
    'vkDisplayPowerControlEXT',
    'vkEndCommandBuffer',
    'vkEnumerateDeviceExtensionProperties',
    'vkEnumerateDeviceLayerProperties',
    'vkEnumerateInstanceExtensionProperties',
    'vkEnumerateInstanceLayerProperties',
    'vkEnumerateInstanceVersion',
    'vkEnumeratePhysicalDeviceGroups',
    'vkEnumeratePhysicalDeviceGroupsKHR',
    'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR',
    'vkEnumeratePhysicalDevices',
    'vkExportMetalObjectsEXT',
    'vkFlushMappedMemoryRanges',
    'vkFreeCommandBuffers',
    'vkFreeDescriptorSets',
    'vkFreeMemory',
    'vkGetAccelerationStructureBuildSizesKHR',
    'vkGetAccelerationStructureDeviceAddressKHR',
    'vkGetAccelerationStructureHandleNV',
    'vkGetAccelerationStructureMemoryRequirementsNV',
    'vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT',
    'vkGetAndroidHardwareBufferPropertiesANDROID',
    'vkGetBufferCollectionPropertiesFUCHSIA',
    'vkGetBufferDeviceAddress',
    'vkGetBufferDeviceAddressEXT',
    'vkGetBufferDeviceAddressKHR',
    'vkGetBufferMemoryRequirements',
    'vkGetBufferMemoryRequirements2',
    'vkGetBufferMemoryRequirements2KHR',
    'vkGetBufferOpaqueCaptureAddress',
    'vkGetBufferOpaqueCaptureAddressKHR',
    'vkGetBufferOpaqueCaptureDescriptorDataEXT',
    'vkGetCalibratedTimestampsEXT',
    'vkGetCalibratedTimestampsKHR',
    'vkGetCommandPoolMemoryConsumption',
    'vkGetCudaModuleCacheNV',
    'vkGetDeferredOperationMaxConcurrencyKHR',
    'vkGetDeferredOperationResultKHR',
    'vkGetDescriptorEXT',
    'vkGetDescriptorSetHostMappingVALVE',
    'vkGetDescriptorSetLayoutBindingOffsetEXT',
    'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    'vkGetDescriptorSetLayoutSizeEXT',
    'vkGetDescriptorSetLayoutSupport',
    'vkGetDescriptorSetLayoutSupportKHR',
    'vkGetDeviceAccelerationStructureCompatibilityKHR',
    'vkGetDeviceBufferMemoryRequirements',
    'vkGetDeviceBufferMemoryRequirementsKHR',
    'vkGetDeviceFaultInfoEXT',
    'vkGetDeviceGroupPeerMemoryFeatures',
    'vkGetDeviceGroupPeerMemoryFeaturesKHR',
    'vkGetDeviceGroupPresentCapabilitiesKHR',
    'vkGetDeviceGroupSurfacePresentModes2EXT',
    'vkGetDeviceGroupSurfacePresentModesKHR',
    'vkGetDeviceImageMemoryRequirements',
    'vkGetDeviceImageMemoryRequirementsKHR',
    'vkGetDeviceImageSparseMemoryRequirements',
    'vkGetDeviceImageSparseMemoryRequirementsKHR',
    'vkGetDeviceImageSubresourceLayoutKHR',
    'vkGetDeviceMemoryCommitment',
    'vkGetDeviceMemoryOpaqueCaptureAddress',
    'vkGetDeviceMemoryOpaqueCaptureAddressKHR',
    'vkGetDeviceMicromapCompatibilityEXT',
    'vkGetDeviceProcAddr',
    'vkGetDeviceQueue',
    'vkGetDeviceQueue2',
    'vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI',
    'vkGetDisplayModeProperties2KHR',
    'vkGetDisplayModePropertiesKHR',
    'vkGetDisplayPlaneCapabilities2KHR',
    'vkGetDisplayPlaneCapabilitiesKHR',
    'vkGetDisplayPlaneSupportedDisplaysKHR',
    'vkGetDrmDisplayEXT',
    'vkGetDynamicRenderingTilePropertiesQCOM',
    'vkGetEncodedVideoSessionParametersKHR',
    'vkGetEventStatus',
    'vkGetExecutionGraphPipelineNodeIndexAMDX',
    'vkGetExecutionGraphPipelineScratchSizeAMDX',
    'vkGetFaultData',
    'vkGetFenceFdKHR',
    'vkGetFenceSciSyncFenceNV',
    'vkGetFenceSciSyncObjNV',
    'vkGetFenceStatus',
    'vkGetFenceWin32HandleKHR',
    'vkGetFramebufferTilePropertiesQCOM',
    'vkGetGeneratedCommandsMemoryRequirementsNV',
    'vkGetImageDrmFormatModifierPropertiesEXT',
    'vkGetImageMemoryRequirements',
    'vkGetImageMemoryRequirements2',
    'vkGetImageMemoryRequirements2KHR',
    'vkGetImageOpaqueCaptureDescriptorDataEXT',
    'vkGetImageSparseMemoryRequirements',
    'vkGetImageSparseMemoryRequirements2',
    'vkGetImageSparseMemoryRequirements2KHR',
    'vkGetImageSubresourceLayout',
    'vkGetImageSubresourceLayout2EXT',
    'vkGetImageSubresourceLayout2KHR',
    'vkGetImageViewAddressNVX',
    'vkGetImageViewHandleNVX',
    'vkGetImageViewOpaqueCaptureDescriptorDataEXT',
    'vkGetInstanceProcAddr',
    'vkGetLatencyTimingsNV',
    'vkGetMemoryAndroidHardwareBufferANDROID',
    'vkGetMemoryFdKHR',
    'vkGetMemoryFdPropertiesKHR',
    'vkGetMemoryHostPointerPropertiesEXT',
    'vkGetMemoryRemoteAddressNV',
    'vkGetMemorySciBufNV',
    'vkGetMemoryWin32HandleKHR',
    'vkGetMemoryWin32HandleNV',
    'vkGetMemoryWin32HandlePropertiesKHR',
    'vkGetMemoryZirconHandleFUCHSIA',
    'vkGetMemoryZirconHandlePropertiesFUCHSIA',
    'vkGetMicromapBuildSizesEXT',
    'vkGetPastPresentationTimingGOOGLE',
    'vkGetPerformanceParameterINTEL',
    'vkGetPhysicalDeviceCalibrateableTimeDomainsEXT',
    'vkGetPhysicalDeviceCalibrateableTimeDomainsKHR',
    'vkGetPhysicalDeviceCooperativeMatrixPropertiesKHR',
    'vkGetPhysicalDeviceCooperativeMatrixPropertiesNV',
    'vkGetPhysicalDeviceDirectFBPresentationSupportEXT',
    'vkGetPhysicalDeviceDisplayPlaneProperties2KHR',
    'vkGetPhysicalDeviceDisplayPlanePropertiesKHR',
    'vkGetPhysicalDeviceDisplayProperties2KHR',
    'vkGetPhysicalDeviceDisplayPropertiesKHR',
    'vkGetPhysicalDeviceExternalBufferProperties',
    'vkGetPhysicalDeviceExternalBufferPropertiesKHR',
    'vkGetPhysicalDeviceExternalFenceProperties',
    'vkGetPhysicalDeviceExternalFencePropertiesKHR',
    'vkGetPhysicalDeviceExternalImageFormatPropertiesNV',
    'vkGetPhysicalDeviceExternalMemorySciBufPropertiesNV',
    'vkGetPhysicalDeviceExternalSemaphoreProperties',
    'vkGetPhysicalDeviceExternalSemaphorePropertiesKHR',
    'vkGetPhysicalDeviceFeatures',
    'vkGetPhysicalDeviceFeatures2',
    'vkGetPhysicalDeviceFeatures2KHR',
    'vkGetPhysicalDeviceFormatProperties',
    'vkGetPhysicalDeviceFormatProperties2',
    'vkGetPhysicalDeviceFormatProperties2KHR',
    'vkGetPhysicalDeviceFragmentShadingRatesKHR',
    'vkGetPhysicalDeviceImageFormatProperties',
    'vkGetPhysicalDeviceImageFormatProperties2',
    'vkGetPhysicalDeviceImageFormatProperties2KHR',
    'vkGetPhysicalDeviceMemoryProperties',
    'vkGetPhysicalDeviceMemoryProperties2',
    'vkGetPhysicalDeviceMemoryProperties2KHR',
    'vkGetPhysicalDeviceMultisamplePropertiesEXT',
    'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
    'vkGetPhysicalDevicePresentRectanglesKHR',
    'vkGetPhysicalDeviceProperties',
    'vkGetPhysicalDeviceProperties2',
    'vkGetPhysicalDeviceProperties2KHR',
    'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR',
    'vkGetPhysicalDeviceQueueFamilyProperties',
    'vkGetPhysicalDeviceQueueFamilyProperties2',
    'vkGetPhysicalDeviceQueueFamilyProperties2KHR',
    'vkGetPhysicalDeviceRefreshableObjectTypesKHR',
    'vkGetPhysicalDeviceSciBufAttributesNV',
    'vkGetPhysicalDeviceSciSyncAttributesNV',
    'vkGetPhysicalDeviceScreenPresentationSupportQNX',
    'vkGetPhysicalDeviceSparseImageFormatProperties',
    'vkGetPhysicalDeviceSparseImageFormatProperties2',
    'vkGetPhysicalDeviceSparseImageFormatProperties2KHR',
    'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV',
    'vkGetPhysicalDeviceSurfaceCapabilities2EXT',
    'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
    'vkGetPhysicalDeviceSurfaceCapabilitiesKHR',
    'vkGetPhysicalDeviceSurfaceFormats2KHR',
    'vkGetPhysicalDeviceSurfaceFormatsKHR',
    'vkGetPhysicalDeviceSurfacePresentModes2EXT',
    'vkGetPhysicalDeviceSurfacePresentModesKHR',
    'vkGetPhysicalDeviceSurfaceSupportKHR',
    'vkGetPhysicalDeviceToolProperties',
    'vkGetPhysicalDeviceToolPropertiesEXT',
    'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
    'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
    'vkGetPhysicalDeviceWaylandPresentationSupportKHR',
    'vkGetPhysicalDeviceWin32PresentationSupportKHR',
    'vkGetPhysicalDeviceXcbPresentationSupportKHR',
    'vkGetPhysicalDeviceXlibPresentationSupportKHR',
    'vkGetPipelineCacheData',
    'vkGetPipelineExecutableInternalRepresentationsKHR',
    'vkGetPipelineExecutablePropertiesKHR',
    'vkGetPipelineExecutableStatisticsKHR',
    'vkGetPipelineIndirectDeviceAddressNV',
    'vkGetPipelineIndirectMemoryRequirementsNV',
    'vkGetPipelinePropertiesEXT',
    'vkGetPrivateData',
    'vkGetPrivateDataEXT',
    'vkGetQueryPoolResults',
    'vkGetQueueCheckpointData2NV',
    'vkGetQueueCheckpointDataNV',
    'vkGetRandROutputDisplayEXT',
    'vkGetRayTracingCaptureReplayShaderGroupHandlesKHR',
    'vkGetRayTracingShaderGroupHandlesKHR',
    'vkGetRayTracingShaderGroupHandlesNV',
    'vkGetRayTracingShaderGroupStackSizeKHR',
    'vkGetRefreshCycleDurationGOOGLE',
    'vkGetRenderAreaGranularity',
    'vkGetRenderingAreaGranularityKHR',
    'vkGetSamplerOpaqueCaptureDescriptorDataEXT',
    'vkGetScreenBufferPropertiesQNX',
    'vkGetSemaphoreCounterValue',
    'vkGetSemaphoreCounterValueKHR',
    'vkGetSemaphoreFdKHR',
    'vkGetSemaphoreSciSyncObjNV',
    'vkGetSemaphoreWin32HandleKHR',
    'vkGetSemaphoreZirconHandleFUCHSIA',
    'vkGetShaderBinaryDataEXT',
    'vkGetShaderInfoAMD',
    'vkGetShaderModuleCreateInfoIdentifierEXT',
    'vkGetShaderModuleIdentifierEXT',
    'vkGetSwapchainCounterEXT',
    'vkGetSwapchainGrallocUsage2ANDROID',
    'vkGetSwapchainGrallocUsageANDROID',
    'vkGetSwapchainImagesKHR',
    'vkGetSwapchainStatusKHR',
    'vkGetValidationCacheDataEXT',
    'vkGetVideoSessionMemoryRequirementsKHR',
    'vkGetWinrtDisplayNV',
    'vkImportFenceFdKHR',
    'vkImportFenceSciSyncFenceNV',
    'vkImportFenceSciSyncObjNV',
    'vkImportFenceWin32HandleKHR',
    'vkImportSemaphoreFdKHR',
    'vkImportSemaphoreSciSyncObjNV',
    'vkImportSemaphoreWin32HandleKHR',
    'vkImportSemaphoreZirconHandleFUCHSIA',
    'vkInitializePerformanceApiINTEL',
    'vkInvalidateMappedMemoryRanges',
    'vkLatencySleepNV',
    'vkMapMemory',
    'vkMapMemory2KHR',
    'vkMergePipelineCaches',
    'vkMergeValidationCachesEXT',
    'vkQueueBeginDebugUtilsLabelEXT',
    'vkQueueBindSparse',
    'vkQueueEndDebugUtilsLabelEXT',
    'vkQueueInsertDebugUtilsLabelEXT',
    'vkQueueNotifyOutOfBandNV',
    'vkQueuePresentKHR',
    'vkQueueSetPerformanceConfigurationINTEL',
    'vkQueueSignalReleaseImageANDROID',
    'vkQueueSubmit',
    'vkQueueSubmit2',
    'vkQueueSubmit2KHR',
    'vkQueueWaitIdle',
    'vkRegisterDeviceEventEXT',
    'vkRegisterDisplayEventEXT',
    'vkReleaseDisplayEXT',
    'vkReleaseFullScreenExclusiveModeEXT',
    'vkReleasePerformanceConfigurationINTEL',
    'vkReleaseProfilingLockKHR',
    'vkReleaseSwapchainImagesEXT',
    'vkResetCommandBuffer',
    'vkResetCommandPool',
    'vkResetDescriptorPool',
    'vkResetEvent',
    'vkResetFences',
    'vkResetQueryPool',
    'vkResetQueryPoolEXT',
    'vkSetBufferCollectionBufferConstraintsFUCHSIA',
    'vkSetBufferCollectionImageConstraintsFUCHSIA',
    'vkSetDebugUtilsObjectNameEXT',
    'vkSetDebugUtilsObjectTagEXT',
    'vkSetDeviceMemoryPriorityEXT',
    'vkSetEvent',
    'vkSetHdrMetadataEXT',
    'vkSetLatencyMarkerNV',
    'vkSetLatencySleepModeNV',
    'vkSetLocalDimmingAMD',
    'vkSetPrivateData',
    'vkSetPrivateDataEXT',
    'vkSignalSemaphore',
    'vkSignalSemaphoreKHR',
    'vkSubmitDebugUtilsMessageEXT',
    'vkTransitionImageLayoutEXT',
    'vkTrimCommandPool',
    'vkTrimCommandPoolKHR',
    'vkUninitializePerformanceApiINTEL',
    'vkUnmapMemory',
    'vkUnmapMemory2KHR',
    'vkUpdateDescriptorSetWithTemplate',
    'vkUpdateDescriptorSetWithTemplateKHR',
    'vkUpdateDescriptorSets',
    'vkUpdateVideoSessionParametersKHR',
    'vkWaitForFences',
    'vkWaitForPresentKHR',
    'vkWaitSemaphores',
    'vkWaitSemaphoresKHR',
    'vkWriteAccelerationStructuresPropertiesKHR',
    'vkWriteMicromapsPropertiesEXT',
]
