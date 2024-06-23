import ctypes
from .vulkan_base import VKAPI_PTR, VKAPI_CALL
from ._vulkan_type.VkAccelerationStructureBuildGeometryInfoKHR import CType as VkAccelerationStructureBuildGeometryInfoKHR
from ._vulkan_type.VkAccelerationStructureBuildRangeInfoKHR import CType as VkAccelerationStructureBuildRangeInfoKHR
from ._vulkan_type.VkAccelerationStructureBuildSizesInfoKHR import CType as VkAccelerationStructureBuildSizesInfoKHR
from ._vulkan_type.VkAccelerationStructureCaptureDescriptorDataInfoEXT import CType as VkAccelerationStructureCaptureDescriptorDataInfoEXT
from ._vulkan_type.VkAccelerationStructureCreateInfoKHR import CType as VkAccelerationStructureCreateInfoKHR
from ._vulkan_type.VkAccelerationStructureCreateInfoNV import CType as VkAccelerationStructureCreateInfoNV
from ._vulkan_type.VkAccelerationStructureDeviceAddressInfoKHR import CType as VkAccelerationStructureDeviceAddressInfoKHR
from ._vulkan_type.VkAccelerationStructureInfoNV import CType as VkAccelerationStructureInfoNV
from ._vulkan_type.VkAccelerationStructureMemoryRequirementsInfoNV import CType as VkAccelerationStructureMemoryRequirementsInfoNV
from ._vulkan_type.VkAccelerationStructureVersionInfoKHR import CType as VkAccelerationStructureVersionInfoKHR
from ._vulkan_type.VkAcquireNextImageInfoKHR import CType as VkAcquireNextImageInfoKHR
from ._vulkan_type.VkAcquireProfilingLockInfoKHR import CType as VkAcquireProfilingLockInfoKHR
from ._vulkan_type.VkAllocationCallbacks import CType as VkAllocationCallbacks
from ._vulkan_type.VkAndroidHardwareBufferPropertiesANDROID import CType as VkAndroidHardwareBufferPropertiesANDROID
from ._vulkan_type.VkAndroidSurfaceCreateInfoKHR import CType as VkAndroidSurfaceCreateInfoKHR
from ._vulkan_type.VkBaseOutStructure import CType as VkBaseOutStructure
from ._vulkan_type.VkBindAccelerationStructureMemoryInfoNV import CType as VkBindAccelerationStructureMemoryInfoNV
from ._vulkan_type.VkBindBufferMemoryInfo import CType as VkBindBufferMemoryInfo
from ._vulkan_type.VkBindDescriptorBufferEmbeddedSamplersInfoEXT import CType as VkBindDescriptorBufferEmbeddedSamplersInfoEXT
from ._vulkan_type.VkBindDescriptorSetsInfoKHR import CType as VkBindDescriptorSetsInfoKHR
from ._vulkan_type.VkBindImageMemoryInfo import CType as VkBindImageMemoryInfo
from ._vulkan_type.VkBindSparseInfo import CType as VkBindSparseInfo
from ._vulkan_type.VkBindVideoSessionMemoryInfoKHR import CType as VkBindVideoSessionMemoryInfoKHR
from ._vulkan_type.VkBlitImageInfo2 import CType as VkBlitImageInfo2
from ._vulkan_type.VkBufferCaptureDescriptorDataInfoEXT import CType as VkBufferCaptureDescriptorDataInfoEXT
from ._vulkan_type.VkBufferCollectionCreateInfoFUCHSIA import CType as VkBufferCollectionCreateInfoFUCHSIA
from ._vulkan_type.VkBufferCollectionPropertiesFUCHSIA import CType as VkBufferCollectionPropertiesFUCHSIA
from ._vulkan_type.VkBufferConstraintsInfoFUCHSIA import CType as VkBufferConstraintsInfoFUCHSIA
from ._vulkan_type.VkBufferCopy import CType as VkBufferCopy
from ._vulkan_type.VkBufferCreateInfo import CType as VkBufferCreateInfo
from ._vulkan_type.VkBufferDeviceAddressInfo import CType as VkBufferDeviceAddressInfo
from ._vulkan_type.VkBufferImageCopy import CType as VkBufferImageCopy
from ._vulkan_type.VkBufferMemoryBarrier import CType as VkBufferMemoryBarrier
from ._vulkan_type.VkBufferMemoryRequirementsInfo2 import CType as VkBufferMemoryRequirementsInfo2
from ._vulkan_type.VkBufferViewCreateInfo import CType as VkBufferViewCreateInfo
from ._vulkan_type.VkCalibratedTimestampInfoKHR import CType as VkCalibratedTimestampInfoKHR
from ._vulkan_type.VkCheckpointData2NV import CType as VkCheckpointData2NV
from ._vulkan_type.VkCheckpointDataNV import CType as VkCheckpointDataNV
from ._vulkan_type.VkClearAttachment import CType as VkClearAttachment
from ._vulkan_type.VkClearColorValue import CType as VkClearColorValue
from ._vulkan_type.VkClearDepthStencilValue import CType as VkClearDepthStencilValue
from ._vulkan_type.VkClearRect import CType as VkClearRect
from ._vulkan_type.VkCoarseSampleOrderCustomNV import CType as VkCoarseSampleOrderCustomNV
from ._vulkan_type.VkColorBlendAdvancedEXT import CType as VkColorBlendAdvancedEXT
from ._vulkan_type.VkColorBlendEquationEXT import CType as VkColorBlendEquationEXT
from ._vulkan_type.VkCommandBufferAllocateInfo import CType as VkCommandBufferAllocateInfo
from ._vulkan_type.VkCommandBufferBeginInfo import CType as VkCommandBufferBeginInfo
from ._vulkan_type.VkCommandPoolCreateInfo import CType as VkCommandPoolCreateInfo
from ._vulkan_type.VkCommandPoolMemoryConsumption import CType as VkCommandPoolMemoryConsumption
from ._vulkan_type.VkComputePipelineCreateInfo import CType as VkComputePipelineCreateInfo
from ._vulkan_type.VkConditionalRenderingBeginInfoEXT import CType as VkConditionalRenderingBeginInfoEXT
from ._vulkan_type.VkCooperativeMatrixPropertiesKHR import CType as VkCooperativeMatrixPropertiesKHR
from ._vulkan_type.VkCooperativeMatrixPropertiesNV import CType as VkCooperativeMatrixPropertiesNV
from ._vulkan_type.VkCopyAccelerationStructureInfoKHR import CType as VkCopyAccelerationStructureInfoKHR
from ._vulkan_type.VkCopyAccelerationStructureToMemoryInfoKHR import CType as VkCopyAccelerationStructureToMemoryInfoKHR
from ._vulkan_type.VkCopyBufferInfo2 import CType as VkCopyBufferInfo2
from ._vulkan_type.VkCopyBufferToImageInfo2 import CType as VkCopyBufferToImageInfo2
from ._vulkan_type.VkCopyDescriptorSet import CType as VkCopyDescriptorSet
from ._vulkan_type.VkCopyImageInfo2 import CType as VkCopyImageInfo2
from ._vulkan_type.VkCopyImageToBufferInfo2 import CType as VkCopyImageToBufferInfo2
from ._vulkan_type.VkCopyImageToImageInfoEXT import CType as VkCopyImageToImageInfoEXT
from ._vulkan_type.VkCopyImageToMemoryInfoEXT import CType as VkCopyImageToMemoryInfoEXT
from ._vulkan_type.VkCopyMemoryToAccelerationStructureInfoKHR import CType as VkCopyMemoryToAccelerationStructureInfoKHR
from ._vulkan_type.VkCopyMemoryToImageInfoEXT import CType as VkCopyMemoryToImageInfoEXT
from ._vulkan_type.VkCopyMemoryToMicromapInfoEXT import CType as VkCopyMemoryToMicromapInfoEXT
from ._vulkan_type.VkCopyMicromapInfoEXT import CType as VkCopyMicromapInfoEXT
from ._vulkan_type.VkCopyMicromapToMemoryInfoEXT import CType as VkCopyMicromapToMemoryInfoEXT
from ._vulkan_type.VkCuFunctionCreateInfoNVX import CType as VkCuFunctionCreateInfoNVX
from ._vulkan_type.VkCuLaunchInfoNVX import CType as VkCuLaunchInfoNVX
from ._vulkan_type.VkCuModuleCreateInfoNVX import CType as VkCuModuleCreateInfoNVX
from ._vulkan_type.VkCudaFunctionCreateInfoNV import CType as VkCudaFunctionCreateInfoNV
from ._vulkan_type.VkCudaLaunchInfoNV import CType as VkCudaLaunchInfoNV
from ._vulkan_type.VkCudaModuleCreateInfoNV import CType as VkCudaModuleCreateInfoNV
from ._vulkan_type.VkDebugMarkerMarkerInfoEXT import CType as VkDebugMarkerMarkerInfoEXT
from ._vulkan_type.VkDebugMarkerObjectNameInfoEXT import CType as VkDebugMarkerObjectNameInfoEXT
from ._vulkan_type.VkDebugMarkerObjectTagInfoEXT import CType as VkDebugMarkerObjectTagInfoEXT
from ._vulkan_type.VkDebugReportCallbackCreateInfoEXT import CType as VkDebugReportCallbackCreateInfoEXT
from ._vulkan_type.VkDebugUtilsLabelEXT import CType as VkDebugUtilsLabelEXT
from ._vulkan_type.VkDebugUtilsMessengerCallbackDataEXT import CType as VkDebugUtilsMessengerCallbackDataEXT
from ._vulkan_type.VkDebugUtilsMessengerCreateInfoEXT import CType as VkDebugUtilsMessengerCreateInfoEXT
from ._vulkan_type.VkDebugUtilsObjectNameInfoEXT import CType as VkDebugUtilsObjectNameInfoEXT
from ._vulkan_type.VkDebugUtilsObjectTagInfoEXT import CType as VkDebugUtilsObjectTagInfoEXT
from ._vulkan_type.VkDecompressMemoryRegionNV import CType as VkDecompressMemoryRegionNV
from ._vulkan_type.VkDependencyInfo import CType as VkDependencyInfo
from ._vulkan_type.VkDepthBiasInfoEXT import CType as VkDepthBiasInfoEXT
from ._vulkan_type.VkDescriptorBufferBindingInfoEXT import CType as VkDescriptorBufferBindingInfoEXT
from ._vulkan_type.VkDescriptorGetInfoEXT import CType as VkDescriptorGetInfoEXT
from ._vulkan_type.VkDescriptorPoolCreateInfo import CType as VkDescriptorPoolCreateInfo
from ._vulkan_type.VkDescriptorSetAllocateInfo import CType as VkDescriptorSetAllocateInfo
from ._vulkan_type.VkDescriptorSetBindingReferenceVALVE import CType as VkDescriptorSetBindingReferenceVALVE
from ._vulkan_type.VkDescriptorSetLayoutCreateInfo import CType as VkDescriptorSetLayoutCreateInfo
from ._vulkan_type.VkDescriptorSetLayoutHostMappingInfoVALVE import CType as VkDescriptorSetLayoutHostMappingInfoVALVE
from ._vulkan_type.VkDescriptorSetLayoutSupport import CType as VkDescriptorSetLayoutSupport
from ._vulkan_type.VkDescriptorUpdateTemplateCreateInfo import CType as VkDescriptorUpdateTemplateCreateInfo
from ._vulkan_type.VkDeviceBufferMemoryRequirements import CType as VkDeviceBufferMemoryRequirements
from ._vulkan_type.VkDeviceCreateInfo import CType as VkDeviceCreateInfo
from ._vulkan_type.VkDeviceEventInfoEXT import CType as VkDeviceEventInfoEXT
from ._vulkan_type.VkDeviceFaultCountsEXT import CType as VkDeviceFaultCountsEXT
from ._vulkan_type.VkDeviceFaultInfoEXT import CType as VkDeviceFaultInfoEXT
from ._vulkan_type.VkDeviceGroupPresentCapabilitiesKHR import CType as VkDeviceGroupPresentCapabilitiesKHR
from ._vulkan_type.VkDeviceImageMemoryRequirements import CType as VkDeviceImageMemoryRequirements
from ._vulkan_type.VkDeviceImageSubresourceInfoKHR import CType as VkDeviceImageSubresourceInfoKHR
from ._vulkan_type.VkDeviceMemoryOpaqueCaptureAddressInfo import CType as VkDeviceMemoryOpaqueCaptureAddressInfo
from ._vulkan_type.VkDeviceQueueInfo2 import CType as VkDeviceQueueInfo2
from ._vulkan_type.VkDirectFBSurfaceCreateInfoEXT import CType as VkDirectFBSurfaceCreateInfoEXT
from ._vulkan_type.VkDispatchGraphCountInfoAMDX import CType as VkDispatchGraphCountInfoAMDX
from ._vulkan_type.VkDisplayEventInfoEXT import CType as VkDisplayEventInfoEXT
from ._vulkan_type.VkDisplayModeCreateInfoKHR import CType as VkDisplayModeCreateInfoKHR
from ._vulkan_type.VkDisplayModeProperties2KHR import CType as VkDisplayModeProperties2KHR
from ._vulkan_type.VkDisplayModePropertiesKHR import CType as VkDisplayModePropertiesKHR
from ._vulkan_type.VkDisplayPlaneCapabilities2KHR import CType as VkDisplayPlaneCapabilities2KHR
from ._vulkan_type.VkDisplayPlaneCapabilitiesKHR import CType as VkDisplayPlaneCapabilitiesKHR
from ._vulkan_type.VkDisplayPlaneInfo2KHR import CType as VkDisplayPlaneInfo2KHR
from ._vulkan_type.VkDisplayPlaneProperties2KHR import CType as VkDisplayPlaneProperties2KHR
from ._vulkan_type.VkDisplayPlanePropertiesKHR import CType as VkDisplayPlanePropertiesKHR
from ._vulkan_type.VkDisplayPowerInfoEXT import CType as VkDisplayPowerInfoEXT
from ._vulkan_type.VkDisplayProperties2KHR import CType as VkDisplayProperties2KHR
from ._vulkan_type.VkDisplayPropertiesKHR import CType as VkDisplayPropertiesKHR
from ._vulkan_type.VkDisplaySurfaceCreateInfoKHR import CType as VkDisplaySurfaceCreateInfoKHR
from ._vulkan_type.VkEventCreateInfo import CType as VkEventCreateInfo
from ._vulkan_type.VkExecutionGraphPipelineCreateInfoAMDX import CType as VkExecutionGraphPipelineCreateInfoAMDX
from ._vulkan_type.VkExecutionGraphPipelineScratchSizeAMDX import CType as VkExecutionGraphPipelineScratchSizeAMDX
from ._vulkan_type.VkExportMetalObjectsInfoEXT import CType as VkExportMetalObjectsInfoEXT
from ._vulkan_type.VkExtensionProperties import CType as VkExtensionProperties
from ._vulkan_type.VkExtent2D import CType as VkExtent2D
from ._vulkan_type.VkExternalBufferProperties import CType as VkExternalBufferProperties
from ._vulkan_type.VkExternalFenceProperties import CType as VkExternalFenceProperties
from ._vulkan_type.VkExternalImageFormatPropertiesNV import CType as VkExternalImageFormatPropertiesNV
from ._vulkan_type.VkExternalSemaphoreProperties import CType as VkExternalSemaphoreProperties
from ._vulkan_type.VkFaultData import CType as VkFaultData
from ._vulkan_type.VkFenceCreateInfo import CType as VkFenceCreateInfo
from ._vulkan_type.VkFenceGetFdInfoKHR import CType as VkFenceGetFdInfoKHR
from ._vulkan_type.VkFenceGetSciSyncInfoNV import CType as VkFenceGetSciSyncInfoNV
from ._vulkan_type.VkFenceGetWin32HandleInfoKHR import CType as VkFenceGetWin32HandleInfoKHR
from ._vulkan_type.VkFormatProperties import CType as VkFormatProperties
from ._vulkan_type.VkFormatProperties2 import CType as VkFormatProperties2
from ._vulkan_type.VkFramebufferCreateInfo import CType as VkFramebufferCreateInfo
from ._vulkan_type.VkFramebufferMixedSamplesCombinationNV import CType as VkFramebufferMixedSamplesCombinationNV
from ._vulkan_type.VkGeneratedCommandsInfoNV import CType as VkGeneratedCommandsInfoNV
from ._vulkan_type.VkGeneratedCommandsMemoryRequirementsInfoNV import CType as VkGeneratedCommandsMemoryRequirementsInfoNV
from ._vulkan_type.VkGetLatencyMarkerInfoNV import CType as VkGetLatencyMarkerInfoNV
from ._vulkan_type.VkGraphicsPipelineCreateInfo import CType as VkGraphicsPipelineCreateInfo
from ._vulkan_type.VkHdrMetadataEXT import CType as VkHdrMetadataEXT
from ._vulkan_type.VkHeadlessSurfaceCreateInfoEXT import CType as VkHeadlessSurfaceCreateInfoEXT
from ._vulkan_type.VkHostImageLayoutTransitionInfoEXT import CType as VkHostImageLayoutTransitionInfoEXT
from ._vulkan_type.VkIOSSurfaceCreateInfoMVK import CType as VkIOSSurfaceCreateInfoMVK
from ._vulkan_type.VkImageBlit import CType as VkImageBlit
from ._vulkan_type.VkImageCaptureDescriptorDataInfoEXT import CType as VkImageCaptureDescriptorDataInfoEXT
from ._vulkan_type.VkImageConstraintsInfoFUCHSIA import CType as VkImageConstraintsInfoFUCHSIA
from ._vulkan_type.VkImageCopy import CType as VkImageCopy
from ._vulkan_type.VkImageCreateInfo import CType as VkImageCreateInfo
from ._vulkan_type.VkImageDrmFormatModifierPropertiesEXT import CType as VkImageDrmFormatModifierPropertiesEXT
from ._vulkan_type.VkImageFormatProperties import CType as VkImageFormatProperties
from ._vulkan_type.VkImageFormatProperties2 import CType as VkImageFormatProperties2
from ._vulkan_type.VkImageMemoryBarrier import CType as VkImageMemoryBarrier
from ._vulkan_type.VkImageMemoryRequirementsInfo2 import CType as VkImageMemoryRequirementsInfo2
from ._vulkan_type.VkImagePipeSurfaceCreateInfoFUCHSIA import CType as VkImagePipeSurfaceCreateInfoFUCHSIA
from ._vulkan_type.VkImageResolve import CType as VkImageResolve
from ._vulkan_type.VkImageSparseMemoryRequirementsInfo2 import CType as VkImageSparseMemoryRequirementsInfo2
from ._vulkan_type.VkImageSubresource import CType as VkImageSubresource
from ._vulkan_type.VkImageSubresource2KHR import CType as VkImageSubresource2KHR
from ._vulkan_type.VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from ._vulkan_type.VkImageSubresourceRange import CType as VkImageSubresourceRange
from ._vulkan_type.VkImageViewAddressPropertiesNVX import CType as VkImageViewAddressPropertiesNVX
from ._vulkan_type.VkImageViewCaptureDescriptorDataInfoEXT import CType as VkImageViewCaptureDescriptorDataInfoEXT
from ._vulkan_type.VkImageViewCreateInfo import CType as VkImageViewCreateInfo
from ._vulkan_type.VkImageViewHandleInfoNVX import CType as VkImageViewHandleInfoNVX
from ._vulkan_type.VkImportFenceFdInfoKHR import CType as VkImportFenceFdInfoKHR
from ._vulkan_type.VkImportFenceSciSyncInfoNV import CType as VkImportFenceSciSyncInfoNV
from ._vulkan_type.VkImportFenceWin32HandleInfoKHR import CType as VkImportFenceWin32HandleInfoKHR
from ._vulkan_type.VkImportSemaphoreFdInfoKHR import CType as VkImportSemaphoreFdInfoKHR
from ._vulkan_type.VkImportSemaphoreSciSyncInfoNV import CType as VkImportSemaphoreSciSyncInfoNV
from ._vulkan_type.VkImportSemaphoreWin32HandleInfoKHR import CType as VkImportSemaphoreWin32HandleInfoKHR
from ._vulkan_type.VkImportSemaphoreZirconHandleInfoFUCHSIA import CType as VkImportSemaphoreZirconHandleInfoFUCHSIA
from ._vulkan_type.VkIndirectCommandsLayoutCreateInfoNV import CType as VkIndirectCommandsLayoutCreateInfoNV
from ._vulkan_type.VkInitializePerformanceApiInfoINTEL import CType as VkInitializePerformanceApiInfoINTEL
from ._vulkan_type.VkInstanceCreateInfo import CType as VkInstanceCreateInfo
from ._vulkan_type.VkLatencySleepInfoNV import CType as VkLatencySleepInfoNV
from ._vulkan_type.VkLatencySleepModeInfoNV import CType as VkLatencySleepModeInfoNV
from ._vulkan_type.VkLayerProperties import CType as VkLayerProperties
from ._vulkan_type.VkMacOSSurfaceCreateInfoMVK import CType as VkMacOSSurfaceCreateInfoMVK
from ._vulkan_type.VkMappedMemoryRange import CType as VkMappedMemoryRange
from ._vulkan_type.VkMemoryAllocateInfo import CType as VkMemoryAllocateInfo
from ._vulkan_type.VkMemoryBarrier import CType as VkMemoryBarrier
from ._vulkan_type.VkMemoryFdPropertiesKHR import CType as VkMemoryFdPropertiesKHR
from ._vulkan_type.VkMemoryGetAndroidHardwareBufferInfoANDROID import CType as VkMemoryGetAndroidHardwareBufferInfoANDROID
from ._vulkan_type.VkMemoryGetFdInfoKHR import CType as VkMemoryGetFdInfoKHR
from ._vulkan_type.VkMemoryGetRemoteAddressInfoNV import CType as VkMemoryGetRemoteAddressInfoNV
from ._vulkan_type.VkMemoryGetSciBufInfoNV import CType as VkMemoryGetSciBufInfoNV
from ._vulkan_type.VkMemoryGetWin32HandleInfoKHR import CType as VkMemoryGetWin32HandleInfoKHR
from ._vulkan_type.VkMemoryGetZirconHandleInfoFUCHSIA import CType as VkMemoryGetZirconHandleInfoFUCHSIA
from ._vulkan_type.VkMemoryHostPointerPropertiesEXT import CType as VkMemoryHostPointerPropertiesEXT
from ._vulkan_type.VkMemoryMapInfoKHR import CType as VkMemoryMapInfoKHR
from ._vulkan_type.VkMemoryRequirements import CType as VkMemoryRequirements
from ._vulkan_type.VkMemoryRequirements2 import CType as VkMemoryRequirements2
from ._vulkan_type.VkMemorySciBufPropertiesNV import CType as VkMemorySciBufPropertiesNV
from ._vulkan_type.VkMemoryUnmapInfoKHR import CType as VkMemoryUnmapInfoKHR
from ._vulkan_type.VkMemoryWin32HandlePropertiesKHR import CType as VkMemoryWin32HandlePropertiesKHR
from ._vulkan_type.VkMemoryZirconHandlePropertiesFUCHSIA import CType as VkMemoryZirconHandlePropertiesFUCHSIA
from ._vulkan_type.VkMetalSurfaceCreateInfoEXT import CType as VkMetalSurfaceCreateInfoEXT
from ._vulkan_type.VkMicromapBuildInfoEXT import CType as VkMicromapBuildInfoEXT
from ._vulkan_type.VkMicromapBuildSizesInfoEXT import CType as VkMicromapBuildSizesInfoEXT
from ._vulkan_type.VkMicromapCreateInfoEXT import CType as VkMicromapCreateInfoEXT
from ._vulkan_type.VkMicromapVersionInfoEXT import CType as VkMicromapVersionInfoEXT
from ._vulkan_type.VkMultiDrawIndexedInfoEXT import CType as VkMultiDrawIndexedInfoEXT
from ._vulkan_type.VkMultiDrawInfoEXT import CType as VkMultiDrawInfoEXT
from ._vulkan_type.VkMultisamplePropertiesEXT import CType as VkMultisamplePropertiesEXT
from ._vulkan_type.VkOpticalFlowExecuteInfoNV import CType as VkOpticalFlowExecuteInfoNV
from ._vulkan_type.VkOpticalFlowImageFormatInfoNV import CType as VkOpticalFlowImageFormatInfoNV
from ._vulkan_type.VkOpticalFlowImageFormatPropertiesNV import CType as VkOpticalFlowImageFormatPropertiesNV
from ._vulkan_type.VkOpticalFlowSessionCreateInfoNV import CType as VkOpticalFlowSessionCreateInfoNV
from ._vulkan_type.VkOutOfBandQueueTypeInfoNV import CType as VkOutOfBandQueueTypeInfoNV
from ._vulkan_type.VkPastPresentationTimingGOOGLE import CType as VkPastPresentationTimingGOOGLE
from ._vulkan_type.VkPerformanceConfigurationAcquireInfoINTEL import CType as VkPerformanceConfigurationAcquireInfoINTEL
from ._vulkan_type.VkPerformanceCounterDescriptionKHR import CType as VkPerformanceCounterDescriptionKHR
from ._vulkan_type.VkPerformanceCounterKHR import CType as VkPerformanceCounterKHR
from ._vulkan_type.VkPerformanceMarkerInfoINTEL import CType as VkPerformanceMarkerInfoINTEL
from ._vulkan_type.VkPerformanceOverrideInfoINTEL import CType as VkPerformanceOverrideInfoINTEL
from ._vulkan_type.VkPerformanceStreamMarkerInfoINTEL import CType as VkPerformanceStreamMarkerInfoINTEL
from ._vulkan_type.VkPerformanceValueINTEL import CType as VkPerformanceValueINTEL
from ._vulkan_type.VkPhysicalDeviceExternalBufferInfo import CType as VkPhysicalDeviceExternalBufferInfo
from ._vulkan_type.VkPhysicalDeviceExternalFenceInfo import CType as VkPhysicalDeviceExternalFenceInfo
from ._vulkan_type.VkPhysicalDeviceExternalSemaphoreInfo import CType as VkPhysicalDeviceExternalSemaphoreInfo
from ._vulkan_type.VkPhysicalDeviceFeatures import CType as VkPhysicalDeviceFeatures
from ._vulkan_type.VkPhysicalDeviceFeatures2 import CType as VkPhysicalDeviceFeatures2
from ._vulkan_type.VkPhysicalDeviceFragmentShadingRateKHR import CType as VkPhysicalDeviceFragmentShadingRateKHR
from ._vulkan_type.VkPhysicalDeviceGroupProperties import CType as VkPhysicalDeviceGroupProperties
from ._vulkan_type.VkPhysicalDeviceImageFormatInfo2 import CType as VkPhysicalDeviceImageFormatInfo2
from ._vulkan_type.VkPhysicalDeviceMemoryProperties import CType as VkPhysicalDeviceMemoryProperties
from ._vulkan_type.VkPhysicalDeviceMemoryProperties2 import CType as VkPhysicalDeviceMemoryProperties2
from ._vulkan_type.VkPhysicalDeviceProperties import CType as VkPhysicalDeviceProperties
from ._vulkan_type.VkPhysicalDeviceProperties2 import CType as VkPhysicalDeviceProperties2
from ._vulkan_type.VkPhysicalDeviceSparseImageFormatInfo2 import CType as VkPhysicalDeviceSparseImageFormatInfo2
from ._vulkan_type.VkPhysicalDeviceSurfaceInfo2KHR import CType as VkPhysicalDeviceSurfaceInfo2KHR
from ._vulkan_type.VkPhysicalDeviceToolProperties import CType as VkPhysicalDeviceToolProperties
from ._vulkan_type.VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR import CType as VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR
from ._vulkan_type.VkPhysicalDeviceVideoFormatInfoKHR import CType as VkPhysicalDeviceVideoFormatInfoKHR
from ._vulkan_type.VkPipelineCacheCreateInfo import CType as VkPipelineCacheCreateInfo
from ._vulkan_type.VkPipelineExecutableInfoKHR import CType as VkPipelineExecutableInfoKHR
from ._vulkan_type.VkPipelineExecutableInternalRepresentationKHR import CType as VkPipelineExecutableInternalRepresentationKHR
from ._vulkan_type.VkPipelineExecutablePropertiesKHR import CType as VkPipelineExecutablePropertiesKHR
from ._vulkan_type.VkPipelineExecutableStatisticKHR import CType as VkPipelineExecutableStatisticKHR
from ._vulkan_type.VkPipelineIndirectDeviceAddressInfoNV import CType as VkPipelineIndirectDeviceAddressInfoNV
from ._vulkan_type.VkPipelineInfoKHR import CType as VkPipelineInfoKHR
from ._vulkan_type.VkPipelineLayoutCreateInfo import CType as VkPipelineLayoutCreateInfo
from ._vulkan_type.VkPipelineShaderStageNodeCreateInfoAMDX import CType as VkPipelineShaderStageNodeCreateInfoAMDX
from ._vulkan_type.VkPresentInfoKHR import CType as VkPresentInfoKHR
from ._vulkan_type.VkPrivateDataSlotCreateInfo import CType as VkPrivateDataSlotCreateInfo
from ._vulkan_type.VkPushConstantsInfoKHR import CType as VkPushConstantsInfoKHR
from ._vulkan_type.VkPushDescriptorSetInfoKHR import CType as VkPushDescriptorSetInfoKHR
from ._vulkan_type.VkPushDescriptorSetWithTemplateInfoKHR import CType as VkPushDescriptorSetWithTemplateInfoKHR
from ._vulkan_type.VkQueryPoolCreateInfo import CType as VkQueryPoolCreateInfo
from ._vulkan_type.VkQueryPoolPerformanceCreateInfoKHR import CType as VkQueryPoolPerformanceCreateInfoKHR
from ._vulkan_type.VkQueueFamilyProperties import CType as VkQueueFamilyProperties
from ._vulkan_type.VkQueueFamilyProperties2 import CType as VkQueueFamilyProperties2
from ._vulkan_type.VkRayTracingPipelineCreateInfoKHR import CType as VkRayTracingPipelineCreateInfoKHR
from ._vulkan_type.VkRayTracingPipelineCreateInfoNV import CType as VkRayTracingPipelineCreateInfoNV
from ._vulkan_type.VkRect2D import CType as VkRect2D
from ._vulkan_type.VkRefreshCycleDurationGOOGLE import CType as VkRefreshCycleDurationGOOGLE
from ._vulkan_type.VkRefreshObjectListKHR import CType as VkRefreshObjectListKHR
from ._vulkan_type.VkReleaseSwapchainImagesInfoEXT import CType as VkReleaseSwapchainImagesInfoEXT
from ._vulkan_type.VkRenderPassBeginInfo import CType as VkRenderPassBeginInfo
from ._vulkan_type.VkRenderPassCreateInfo import CType as VkRenderPassCreateInfo
from ._vulkan_type.VkRenderPassCreateInfo2 import CType as VkRenderPassCreateInfo2
from ._vulkan_type.VkRenderingAreaInfoKHR import CType as VkRenderingAreaInfoKHR
from ._vulkan_type.VkRenderingAttachmentLocationInfoKHR import CType as VkRenderingAttachmentLocationInfoKHR
from ._vulkan_type.VkRenderingInfo import CType as VkRenderingInfo
from ._vulkan_type.VkRenderingInputAttachmentIndexInfoKHR import CType as VkRenderingInputAttachmentIndexInfoKHR
from ._vulkan_type.VkResolveImageInfo2 import CType as VkResolveImageInfo2
from ._vulkan_type.VkSampleLocationsInfoEXT import CType as VkSampleLocationsInfoEXT
from ._vulkan_type.VkSamplerCaptureDescriptorDataInfoEXT import CType as VkSamplerCaptureDescriptorDataInfoEXT
from ._vulkan_type.VkSamplerCreateInfo import CType as VkSamplerCreateInfo
from ._vulkan_type.VkSamplerYcbcrConversionCreateInfo import CType as VkSamplerYcbcrConversionCreateInfo
from ._vulkan_type.VkSciSyncAttributesInfoNV import CType as VkSciSyncAttributesInfoNV
from ._vulkan_type.VkScreenBufferPropertiesQNX import CType as VkScreenBufferPropertiesQNX
from ._vulkan_type.VkScreenSurfaceCreateInfoQNX import CType as VkScreenSurfaceCreateInfoQNX
from ._vulkan_type.VkSemaphoreCreateInfo import CType as VkSemaphoreCreateInfo
from ._vulkan_type.VkSemaphoreGetFdInfoKHR import CType as VkSemaphoreGetFdInfoKHR
from ._vulkan_type.VkSemaphoreGetSciSyncInfoNV import CType as VkSemaphoreGetSciSyncInfoNV
from ._vulkan_type.VkSemaphoreGetWin32HandleInfoKHR import CType as VkSemaphoreGetWin32HandleInfoKHR
from ._vulkan_type.VkSemaphoreGetZirconHandleInfoFUCHSIA import CType as VkSemaphoreGetZirconHandleInfoFUCHSIA
from ._vulkan_type.VkSemaphoreSciSyncPoolCreateInfoNV import CType as VkSemaphoreSciSyncPoolCreateInfoNV
from ._vulkan_type.VkSemaphoreSignalInfo import CType as VkSemaphoreSignalInfo
from ._vulkan_type.VkSemaphoreWaitInfo import CType as VkSemaphoreWaitInfo
from ._vulkan_type.VkSetDescriptorBufferOffsetsInfoEXT import CType as VkSetDescriptorBufferOffsetsInfoEXT
from ._vulkan_type.VkSetLatencyMarkerInfoNV import CType as VkSetLatencyMarkerInfoNV
from ._vulkan_type.VkShaderCreateInfoEXT import CType as VkShaderCreateInfoEXT
from ._vulkan_type.VkShaderModuleCreateInfo import CType as VkShaderModuleCreateInfo
from ._vulkan_type.VkShaderModuleIdentifierEXT import CType as VkShaderModuleIdentifierEXT
from ._vulkan_type.VkShadingRatePaletteNV import CType as VkShadingRatePaletteNV
from ._vulkan_type.VkSparseImageFormatProperties import CType as VkSparseImageFormatProperties
from ._vulkan_type.VkSparseImageFormatProperties2 import CType as VkSparseImageFormatProperties2
from ._vulkan_type.VkSparseImageMemoryRequirements import CType as VkSparseImageMemoryRequirements
from ._vulkan_type.VkSparseImageMemoryRequirements2 import CType as VkSparseImageMemoryRequirements2
from ._vulkan_type.VkStreamDescriptorSurfaceCreateInfoGGP import CType as VkStreamDescriptorSurfaceCreateInfoGGP
from ._vulkan_type.VkStridedDeviceAddressRegionKHR import CType as VkStridedDeviceAddressRegionKHR
from ._vulkan_type.VkSubmitInfo import CType as VkSubmitInfo
from ._vulkan_type.VkSubmitInfo2 import CType as VkSubmitInfo2
from ._vulkan_type.VkSubpassBeginInfo import CType as VkSubpassBeginInfo
from ._vulkan_type.VkSubpassEndInfo import CType as VkSubpassEndInfo
from ._vulkan_type.VkSubresourceLayout import CType as VkSubresourceLayout
from ._vulkan_type.VkSubresourceLayout2KHR import CType as VkSubresourceLayout2KHR
from ._vulkan_type.VkSurfaceCapabilities2EXT import CType as VkSurfaceCapabilities2EXT
from ._vulkan_type.VkSurfaceCapabilities2KHR import CType as VkSurfaceCapabilities2KHR
from ._vulkan_type.VkSurfaceCapabilitiesKHR import CType as VkSurfaceCapabilitiesKHR
from ._vulkan_type.VkSurfaceFormat2KHR import CType as VkSurfaceFormat2KHR
from ._vulkan_type.VkSurfaceFormatKHR import CType as VkSurfaceFormatKHR
from ._vulkan_type.VkSwapchainCreateInfoKHR import CType as VkSwapchainCreateInfoKHR
from ._vulkan_type.VkTilePropertiesQCOM import CType as VkTilePropertiesQCOM
from ._vulkan_type.VkValidationCacheCreateInfoEXT import CType as VkValidationCacheCreateInfoEXT
from ._vulkan_type.VkVertexInputAttributeDescription2EXT import CType as VkVertexInputAttributeDescription2EXT
from ._vulkan_type.VkVertexInputBindingDescription2EXT import CType as VkVertexInputBindingDescription2EXT
from ._vulkan_type.VkViSurfaceCreateInfoNN import CType as VkViSurfaceCreateInfoNN
from ._vulkan_type.VkVideoBeginCodingInfoKHR import CType as VkVideoBeginCodingInfoKHR
from ._vulkan_type.VkVideoCapabilitiesKHR import CType as VkVideoCapabilitiesKHR
from ._vulkan_type.VkVideoCodingControlInfoKHR import CType as VkVideoCodingControlInfoKHR
from ._vulkan_type.VkVideoDecodeInfoKHR import CType as VkVideoDecodeInfoKHR
from ._vulkan_type.VkVideoEncodeInfoKHR import CType as VkVideoEncodeInfoKHR
from ._vulkan_type.VkVideoEncodeQualityLevelPropertiesKHR import CType as VkVideoEncodeQualityLevelPropertiesKHR
from ._vulkan_type.VkVideoEncodeSessionParametersFeedbackInfoKHR import CType as VkVideoEncodeSessionParametersFeedbackInfoKHR
from ._vulkan_type.VkVideoEncodeSessionParametersGetInfoKHR import CType as VkVideoEncodeSessionParametersGetInfoKHR
from ._vulkan_type.VkVideoEndCodingInfoKHR import CType as VkVideoEndCodingInfoKHR
from ._vulkan_type.VkVideoFormatPropertiesKHR import CType as VkVideoFormatPropertiesKHR
from ._vulkan_type.VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR
from ._vulkan_type.VkVideoSessionCreateInfoKHR import CType as VkVideoSessionCreateInfoKHR
from ._vulkan_type.VkVideoSessionMemoryRequirementsKHR import CType as VkVideoSessionMemoryRequirementsKHR
from ._vulkan_type.VkVideoSessionParametersCreateInfoKHR import CType as VkVideoSessionParametersCreateInfoKHR
from ._vulkan_type.VkVideoSessionParametersUpdateInfoKHR import CType as VkVideoSessionParametersUpdateInfoKHR
from ._vulkan_type.VkViewport import CType as VkViewport
from ._vulkan_type.VkViewportSwizzleNV import CType as VkViewportSwizzleNV
from ._vulkan_type.VkViewportWScalingNV import CType as VkViewportWScalingNV
from ._vulkan_type.VkWaylandSurfaceCreateInfoKHR import CType as VkWaylandSurfaceCreateInfoKHR
from ._vulkan_type.VkWin32SurfaceCreateInfoKHR import CType as VkWin32SurfaceCreateInfoKHR
from ._vulkan_type.VkWriteDescriptorSet import CType as VkWriteDescriptorSet
from ._vulkan_type.VkXcbSurfaceCreateInfoKHR import CType as VkXcbSurfaceCreateInfoKHR
from ._vulkan_type.VkXlibSurfaceCreateInfoKHR import CType as VkXlibSurfaceCreateInfoKHR
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
vkCreateSharedSwapchainsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateStreamDescriptorSurfaceGGP = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkStreamDescriptorSurfaceCreateInfoGGP), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
vkCreateSwapchainKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
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
vkGetDeviceProcAddr = VKAPI_CALL(vkVoidFunction, ctypes.c_void_p, ctypes.c_char_p)
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
vkGetInstanceProcAddr = VKAPI_CALL(vkVoidFunction, ctypes.c_void_p, ctypes.c_char_p)
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
