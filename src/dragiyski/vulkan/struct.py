from ._struct import (
    StdVideoAV1ChromaSamplePosition,
    StdVideoAV1ColorPrimaries,
    StdVideoAV1FrameRestorationType,
    StdVideoAV1FrameType,
    StdVideoAV1InterpolationFilter,
    StdVideoAV1Level,
    StdVideoAV1MatrixCoefficients,
    StdVideoAV1Profile,
    StdVideoAV1ReferenceName,
    StdVideoAV1TransferCharacteristics,
    StdVideoAV1TxMode,
    StdVideoDecodeH264FieldOrderCount,
    StdVideoH264AspectRatioIdc,
    StdVideoH264CabacInitIdc,
    StdVideoH264ChromaFormatIdc,
    StdVideoH264DisableDeblockingFilterIdc,
    StdVideoH264LevelIdc,
    StdVideoH264MemMgmtControlOp,
    StdVideoH264ModificationOfPicNumsIdc,
    StdVideoH264NonVclNaluType,
    StdVideoH264PictureType,
    StdVideoH264PocType,
    StdVideoH264ProfileIdc,
    StdVideoH264SliceType,
    StdVideoH264WeightedBipredIdc,
    StdVideoH265AspectRatioIdc,
    StdVideoH265ChromaFormatIdc,
    StdVideoH265LevelIdc,
    StdVideoH265PictureType,
    StdVideoH265ProfileIdc,
    StdVideoH265SliceType,
    VkAccelerationStructureBuildTypeKHR,
    VkAccelerationStructureCompatibilityKHR,
    VkAccelerationStructureCreateFlagsKHR,
    VkAccelerationStructureMemoryRequirementsTypeNV,
    VkAccelerationStructureMotionInfoFlagsNV,
    VkAccelerationStructureMotionInstanceFlagsNV,
    VkAccelerationStructureMotionInstanceTypeNV,
    VkAccelerationStructureTypeKHR,
    VkAccessFlags,
    VkAccessFlags2,
    VkAcquireProfilingLockFlagsKHR,
    VkAndroidSurfaceCreateFlagsKHR,
    VkAttachmentDescriptionFlags,
    VkAttachmentLoadOp,
    VkAttachmentStoreOp,
    VkBlendFactor,
    VkBlendOp,
    VkBlendOverlapEXT,
    VkBlockMatchWindowCompareModeQCOM,
    VkBorderColor,
    VkBufferCreateFlags,
    VkBufferUsageFlags,
    VkBufferUsageFlags2KHR,
    VkBufferViewCreateFlags,
    VkBuildAccelerationStructureFlagsKHR,
    VkBuildAccelerationStructureModeKHR,
    VkBuildMicromapFlagsEXT,
    VkBuildMicromapModeEXT,
    VkChromaLocation,
    VkCoarseSampleOrderTypeNV,
    VkColorComponentFlags,
    VkColorSpaceKHR,
    VkCommandBufferLevel,
    VkCommandBufferResetFlags,
    VkCommandBufferUsageFlags,
    VkCommandPoolCreateFlags,
    VkCommandPoolResetFlags,
    VkCommandPoolTrimFlags,
    VkCompareOp,
    VkComponentSwizzle,
    VkComponentTypeKHR,
    VkCompositeAlphaFlagsKHR,
    VkConditionalRenderingFlagsEXT,
    VkConservativeRasterizationModeEXT,
    VkCopyAccelerationStructureModeKHR,
    VkCopyMicromapModeEXT,
    VkCoverageModulationModeNV,
    VkCoverageReductionModeNV,
    VkCubicFilterWeightsQCOM,
    VkCullModeFlags,
    VkDebugReportFlagsEXT,
    VkDebugReportObjectTypeEXT,
    VkDebugUtilsMessageSeverityFlagsEXT,
    VkDebugUtilsMessageTypeFlagsEXT,
    VkDebugUtilsMessengerCallbackDataFlagsEXT,
    VkDebugUtilsMessengerCreateFlagsEXT,
    VkDependencyFlags,
    VkDepthBiasRepresentationEXT,
    VkDescriptorBindingFlags,
    VkDescriptorPoolCreateFlags,
    VkDescriptorPoolResetFlags,
    VkDescriptorSetLayoutCreateFlags,
    VkDescriptorType,
    VkDescriptorUpdateTemplateCreateFlags,
    VkDescriptorUpdateTemplateType,
    VkDeviceAddressBindingFlagsEXT,
    VkDeviceAddressBindingTypeEXT,
    VkDeviceCreateFlags,
    VkDeviceDiagnosticsConfigFlagsNV,
    VkDeviceEventTypeEXT,
    VkDeviceFaultAddressTypeEXT,
    VkDeviceFaultVendorBinaryHeaderVersionEXT,
    VkDeviceGroupPresentModeFlagsKHR,
    VkDeviceMemoryReportEventTypeEXT,
    VkDeviceMemoryReportFlagsEXT,
    VkDeviceQueueCreateFlags,
    VkDirectDriverLoadingFlagsLUNARG,
    VkDirectDriverLoadingModeLUNARG,
    VkDirectFBSurfaceCreateFlagsEXT,
    VkDiscardRectangleModeEXT,
    VkDisplacementMicromapFormatNV,
    VkDisplayEventTypeEXT,
    VkDisplayModeCreateFlagsKHR,
    VkDisplayPlaneAlphaFlagsKHR,
    VkDisplayPowerStateEXT,
    VkDisplaySurfaceCreateFlagsKHR,
    VkDriverId,
    VkDynamicState,
    VkEventCreateFlags,
    VkExportMetalObjectTypeFlagsEXT,
    VkExternalFenceFeatureFlags,
    VkExternalFenceHandleTypeFlags,
    VkExternalMemoryFeatureFlags,
    VkExternalMemoryFeatureFlagsNV,
    VkExternalMemoryHandleTypeFlags,
    VkExternalMemoryHandleTypeFlagsNV,
    VkExternalSemaphoreFeatureFlags,
    VkExternalSemaphoreHandleTypeFlags,
    VkFaultLevel,
    VkFaultQueryBehavior,
    VkFaultType,
    VkFenceCreateFlags,
    VkFenceImportFlags,
    VkFilter,
    VkFormat,
    VkFormatFeatureFlags,
    VkFormatFeatureFlags2,
    VkFragmentShadingRateCombinerOpKHR,
    VkFragmentShadingRateNV,
    VkFragmentShadingRateTypeNV,
    VkFrameBoundaryFlagsEXT,
    VkFramebufferCreateFlags,
    VkFrontFace,
    VkFullScreenExclusiveEXT,
    VkGeometryFlagsKHR,
    VkGeometryInstanceFlagsKHR,
    VkGeometryTypeKHR,
    VkGraphicsPipelineLibraryFlagsEXT,
    VkHeadlessSurfaceCreateFlagsEXT,
    VkHostImageCopyFlagsEXT,
    VkIOSSurfaceCreateFlagsMVK,
    VkImageAspectFlags,
    VkImageCompressionFixedRateFlagsEXT,
    VkImageCompressionFlagsEXT,
    VkImageConstraintsInfoFlagsFUCHSIA,
    VkImageCreateFlags,
    VkImageFormatConstraintsFlagBitsFUCHSIA,
    VkImageFormatConstraintsFlagsFUCHSIA,
    VkImageLayout,
    VkImagePipeSurfaceCreateFlagsFUCHSIA,
    VkImageTiling,
    VkImageType,
    VkImageUsageFlags,
    VkImageViewCreateFlags,
    VkImageViewType,
    VkIndexType,
    VkIndirectCommandsLayoutUsageFlagsNV,
    VkIndirectCommandsTokenTypeNV,
    VkIndirectStateFlagsNV,
    VkInstanceCreateFlags,
    VkInternalAllocationType,
    VkLatencyMarkerNV,
    VkLayerSettingTypeEXT,
    VkLayeredDriverUnderlyingApiMSFT,
    VkLineRasterizationModeKHR,
    VkLogicOp,
    VkMacOSSurfaceCreateFlagsMVK,
    VkMemoryAllocateFlags,
    VkMemoryDecompressionMethodFlagsNV,
    VkMemoryHeapFlags,
    VkMemoryMapFlags,
    VkMemoryOverallocationBehaviorAMD,
    VkMemoryPropertyFlags,
    VkMemoryUnmapFlagsKHR,
    VkMetalSurfaceCreateFlagsEXT,
    VkMicromapCreateFlagsEXT,
    VkMicromapTypeEXT,
    VkObjectType,
    VkOpacityMicromapFormatEXT,
    VkOpacityMicromapSpecialIndexEXT,
    VkOpticalFlowExecuteFlagsNV,
    VkOpticalFlowGridSizeFlagsNV,
    VkOpticalFlowPerformanceLevelNV,
    VkOpticalFlowSessionBindingPointNV,
    VkOpticalFlowSessionCreateFlagsNV,
    VkOpticalFlowUsageFlagsNV,
    VkOutOfBandQueueTypeNV,
    VkPeerMemoryFeatureFlags,
    VkPerformanceConfigurationTypeINTEL,
    VkPerformanceCounterDescriptionFlagsKHR,
    VkPerformanceCounterScopeKHR,
    VkPerformanceCounterStorageKHR,
    VkPerformanceCounterUnitKHR,
    VkPerformanceOverrideTypeINTEL,
    VkPerformanceParameterTypeINTEL,
    VkPerformanceValueTypeINTEL,
    VkPhysicalDeviceSchedulingControlsFlagsARM,
    VkPhysicalDeviceType,
    VkPipelineBindPoint,
    VkPipelineCacheCreateFlags,
    VkPipelineCacheHeaderVersion,
    VkPipelineCacheValidationVersion,
    VkPipelineColorBlendStateCreateFlags,
    VkPipelineCompilerControlFlagsAMD,
    VkPipelineCoverageModulationStateCreateFlagsNV,
    VkPipelineCoverageReductionStateCreateFlagsNV,
    VkPipelineCoverageToColorStateCreateFlagsNV,
    VkPipelineCreateFlags,
    VkPipelineCreateFlags2KHR,
    VkPipelineCreationFeedbackFlags,
    VkPipelineDepthStencilStateCreateFlags,
    VkPipelineDiscardRectangleStateCreateFlagsEXT,
    VkPipelineDynamicStateCreateFlags,
    VkPipelineExecutableStatisticFormatKHR,
    VkPipelineInputAssemblyStateCreateFlags,
    VkPipelineLayoutCreateFlags,
    VkPipelineMatchControl,
    VkPipelineMultisampleStateCreateFlags,
    VkPipelineRasterizationConservativeStateCreateFlagsEXT,
    VkPipelineRasterizationDepthClipStateCreateFlagsEXT,
    VkPipelineRasterizationStateCreateFlags,
    VkPipelineRasterizationStateStreamCreateFlagsEXT,
    VkPipelineRobustnessBufferBehaviorEXT,
    VkPipelineRobustnessImageBehaviorEXT,
    VkPipelineShaderStageCreateFlags,
    VkPipelineStageFlags,
    VkPipelineStageFlags2,
    VkPipelineTessellationStateCreateFlags,
    VkPipelineVertexInputStateCreateFlags,
    VkPipelineViewportStateCreateFlags,
    VkPipelineViewportSwizzleStateCreateFlagsNV,
    VkPointClippingBehavior,
    VkPolygonMode,
    VkPresentGravityFlagsEXT,
    VkPresentModeKHR,
    VkPresentScalingFlagsEXT,
    VkPrimitiveTopology,
    VkPrivateDataSlotCreateFlagBits,
    VkPrivateDataSlotCreateFlags,
    VkProvokingVertexModeEXT,
    VkQueryControlFlags,
    VkQueryPipelineStatisticFlags,
    VkQueryPoolCreateFlags,
    VkQueryPoolSamplingModeINTEL,
    VkQueryResultFlags,
    VkQueryResultStatusKHR,
    VkQueryType,
    VkQueueFlags,
    VkQueueGlobalPriorityKHR,
    VkRasterizationOrderAMD,
    VkRayTracingInvocationReorderModeNV,
    VkRayTracingShaderGroupTypeKHR,
    VkRefreshObjectFlagsKHR,
    VkRenderPassCreateFlags,
    VkRenderingFlags,
    VkResolveModeFlags,
    VkResult,
    VkSampleCountFlags,
    VkSamplerAddressMode,
    VkSamplerCreateFlags,
    VkSamplerMipmapMode,
    VkSamplerReductionMode,
    VkSamplerYcbcrModelConversion,
    VkSamplerYcbcrRange,
    VkSciSyncClientTypeNV,
    VkSciSyncPrimitiveTypeNV,
    VkScopeKHR,
    VkScreenSurfaceCreateFlagsQNX,
    VkSemaphoreCreateFlagBits,
    VkSemaphoreCreateFlags,
    VkSemaphoreImportFlags,
    VkSemaphoreType,
    VkSemaphoreWaitFlags,
    VkShaderCodeTypeEXT,
    VkShaderCorePropertiesFlagsAMD,
    VkShaderCreateFlagsEXT,
    VkShaderFloatControlsIndependence,
    VkShaderGroupShaderKHR,
    VkShaderInfoTypeAMD,
    VkShaderModuleCreateFlagBits,
    VkShaderModuleCreateFlags,
    VkShaderStageFlags,
    VkShadingRatePaletteEntryNV,
    VkSharingMode,
    VkSparseImageFormatFlags,
    VkSparseMemoryBindFlags,
    VkStencilFaceFlags,
    VkStencilOp,
    VkStreamDescriptorSurfaceCreateFlagsGGP,
    VkStructureType,
    VkSubgroupFeatureFlags,
    VkSubmitFlags,
    VkSubpassContents,
    VkSubpassDescriptionFlags,
    VkSubpassMergeStatusEXT,
    VkSurfaceCounterFlagsEXT,
    VkSurfaceTransformFlagsKHR,
    VkSwapchainCreateFlagsKHR,
    VkSwapchainImageUsageFlagsANDROID,
    VkSystemAllocationScope,
    VkTessellationDomainOrigin,
    VkTimeDomainKHR,
    VkToolPurposeFlags,
    VkValidationCacheCreateFlagsEXT,
    VkValidationCacheHeaderVersionEXT,
    VkValidationCheckEXT,
    VkValidationFeatureDisableEXT,
    VkValidationFeatureEnableEXT,
    VkVendorId,
    VkVertexInputRate,
    VkViSurfaceCreateFlagsNN,
    VkVideoBeginCodingFlagsKHR,
    VkVideoCapabilityFlagsKHR,
    VkVideoChromaSubsamplingFlagsKHR,
    VkVideoCodecOperationFlagsKHR,
    VkVideoCodingControlFlagsKHR,
    VkVideoComponentBitDepthFlagsKHR,
    VkVideoDecodeCapabilityFlagsKHR,
    VkVideoDecodeFlagsKHR,
    VkVideoDecodeH264PictureLayoutFlagsKHR,
    VkVideoDecodeUsageFlagsKHR,
    VkVideoEncodeCapabilityFlagsKHR,
    VkVideoEncodeContentFlagsKHR,
    VkVideoEncodeFeedbackFlagsKHR,
    VkVideoEncodeFlagsKHR,
    VkVideoEncodeH264CapabilityFlagsKHR,
    VkVideoEncodeH264RateControlFlagsKHR,
    VkVideoEncodeH264StdFlagsKHR,
    VkVideoEncodeH265CapabilityFlagsKHR,
    VkVideoEncodeH265CtbSizeFlagsKHR,
    VkVideoEncodeH265RateControlFlagsKHR,
    VkVideoEncodeH265StdFlagsKHR,
    VkVideoEncodeH265TransformBlockSizeFlagsKHR,
    VkVideoEncodeRateControlFlagsKHR,
    VkVideoEncodeRateControlModeFlagsKHR,
    VkVideoEncodeTuningModeKHR,
    VkVideoEncodeUsageFlagsKHR,
    VkVideoEndCodingFlagsKHR,
    VkVideoSessionCreateFlagsKHR,
    VkVideoSessionParametersCreateFlagsKHR,
    VkViewportCoordinateSwizzleNV,
    VkWaylandSurfaceCreateFlagsKHR,
    VkWin32SurfaceCreateFlagsKHR,
    VkXcbSurfaceCreateFlagsKHR,
    VkXlibSurfaceCreateFlagsKHR,
)

VkAabbPositionsNV = VkAabbPositionsKHR
VkAccelerationStructureInstanceNV = VkAccelerationStructureInstanceKHR
VkAttachmentDescription2KHR = VkAttachmentDescription2
VkAttachmentDescriptionStencilLayoutKHR = VkAttachmentDescriptionStencilLayout
VkAttachmentReference2KHR = VkAttachmentReference2
VkAttachmentReferenceStencilLayoutKHR = VkAttachmentReferenceStencilLayout
VkAttachmentSampleCountInfoNV = VkAttachmentSampleCountInfoAMD
VkBindBufferMemoryDeviceGroupInfoKHR = VkBindBufferMemoryDeviceGroupInfo
VkBindBufferMemoryInfoKHR = VkBindBufferMemoryInfo
VkBindImageMemoryDeviceGroupInfoKHR = VkBindImageMemoryDeviceGroupInfo
VkBindImageMemoryInfoKHR = VkBindImageMemoryInfo
VkBindImagePlaneMemoryInfoKHR = VkBindImagePlaneMemoryInfo
VkBlitImageInfo2KHR = VkBlitImageInfo2
VkBufferCopy2KHR = VkBufferCopy2
VkBufferDeviceAddressInfoEXT = VkBufferDeviceAddressInfo
VkBufferDeviceAddressInfoKHR = VkBufferDeviceAddressInfo
VkBufferImageCopy2KHR = VkBufferImageCopy2
VkBufferMemoryBarrier2KHR = VkBufferMemoryBarrier2
VkBufferMemoryRequirementsInfo2KHR = VkBufferMemoryRequirementsInfo2
VkBufferOpaqueCaptureAddressCreateInfoKHR = VkBufferOpaqueCaptureAddressCreateInfo
VkCalibratedTimestampInfoEXT = VkCalibratedTimestampInfoKHR
VkCommandBufferInheritanceRenderingInfoKHR = VkCommandBufferInheritanceRenderingInfo
VkCommandBufferSubmitInfoKHR = VkCommandBufferSubmitInfo
VkConformanceVersionKHR = VkConformanceVersion
VkCopyBufferInfo2KHR = VkCopyBufferInfo2
VkCopyBufferToImageInfo2KHR = VkCopyBufferToImageInfo2
VkCopyImageInfo2KHR = VkCopyImageInfo2
VkCopyImageToBufferInfo2KHR = VkCopyImageToBufferInfo2
VkDependencyInfoKHR = VkDependencyInfo
VkDescriptorPoolInlineUniformBlockCreateInfoEXT = VkDescriptorPoolInlineUniformBlockCreateInfo
VkDescriptorSetLayoutBindingFlagsCreateInfoEXT = VkDescriptorSetLayoutBindingFlagsCreateInfo
VkDescriptorSetLayoutSupportKHR = VkDescriptorSetLayoutSupport
VkDescriptorSetVariableDescriptorCountAllocateInfoEXT = VkDescriptorSetVariableDescriptorCountAllocateInfo
VkDescriptorSetVariableDescriptorCountLayoutSupportEXT = VkDescriptorSetVariableDescriptorCountLayoutSupport
VkDescriptorUpdateTemplateCreateInfoKHR = VkDescriptorUpdateTemplateCreateInfo
VkDescriptorUpdateTemplateEntryKHR = VkDescriptorUpdateTemplateEntry
VkDeviceBufferMemoryRequirementsKHR = VkDeviceBufferMemoryRequirements
VkDeviceGroupBindSparseInfoKHR = VkDeviceGroupBindSparseInfo
VkDeviceGroupCommandBufferBeginInfoKHR = VkDeviceGroupCommandBufferBeginInfo
VkDeviceGroupDeviceCreateInfoKHR = VkDeviceGroupDeviceCreateInfo
VkDeviceGroupRenderPassBeginInfoKHR = VkDeviceGroupRenderPassBeginInfo
VkDeviceGroupSubmitInfoKHR = VkDeviceGroupSubmitInfo
VkDeviceImageMemoryRequirementsKHR = VkDeviceImageMemoryRequirements
VkDeviceMemoryOpaqueCaptureAddressInfoKHR = VkDeviceMemoryOpaqueCaptureAddressInfo
VkDevicePrivateDataCreateInfoEXT = VkDevicePrivateDataCreateInfo
VkDeviceQueueGlobalPriorityCreateInfoEXT = VkDeviceQueueGlobalPriorityCreateInfoKHR
VkExportFenceCreateInfoKHR = VkExportFenceCreateInfo
VkExportMemoryAllocateInfoKHR = VkExportMemoryAllocateInfo
VkExportSemaphoreCreateInfoKHR = VkExportSemaphoreCreateInfo
VkExternalBufferPropertiesKHR = VkExternalBufferProperties
VkExternalFencePropertiesKHR = VkExternalFenceProperties
VkExternalImageFormatPropertiesKHR = VkExternalImageFormatProperties
VkExternalMemoryBufferCreateInfoKHR = VkExternalMemoryBufferCreateInfo
VkExternalMemoryImageCreateInfoKHR = VkExternalMemoryImageCreateInfo
VkExternalMemoryPropertiesKHR = VkExternalMemoryProperties
VkExternalSemaphorePropertiesKHR = VkExternalSemaphoreProperties
VkFormatProperties2KHR = VkFormatProperties2
VkFormatProperties3KHR = VkFormatProperties3
VkFramebufferAttachmentImageInfoKHR = VkFramebufferAttachmentImageInfo
VkFramebufferAttachmentsCreateInfoKHR = VkFramebufferAttachmentsCreateInfo
VkImageBlit2KHR = VkImageBlit2
VkImageCopy2KHR = VkImageCopy2
VkImageFormatListCreateInfoKHR = VkImageFormatListCreateInfo
VkImageFormatProperties2KHR = VkImageFormatProperties2
VkImageMemoryBarrier2KHR = VkImageMemoryBarrier2
VkImageMemoryRequirementsInfo2KHR = VkImageMemoryRequirementsInfo2
VkImagePlaneMemoryRequirementsInfoKHR = VkImagePlaneMemoryRequirementsInfo
VkImageResolve2KHR = VkImageResolve2
VkImageSparseMemoryRequirementsInfo2KHR = VkImageSparseMemoryRequirementsInfo2
VkImageStencilUsageCreateInfoEXT = VkImageStencilUsageCreateInfo
VkImageSubresource2EXT = VkImageSubresource2KHR
VkImageViewUsageCreateInfoKHR = VkImageViewUsageCreateInfo
VkInputAttachmentAspectReferenceKHR = VkInputAttachmentAspectReference
VkMemoryAllocateFlagsInfoKHR = VkMemoryAllocateFlagsInfo
VkMemoryBarrier2KHR = VkMemoryBarrier2
VkMemoryDedicatedAllocateInfoKHR = VkMemoryDedicatedAllocateInfo
VkMemoryDedicatedRequirementsKHR = VkMemoryDedicatedRequirements
VkMemoryOpaqueCaptureAddressAllocateInfoKHR = VkMemoryOpaqueCaptureAddressAllocateInfo
VkMemoryRequirements2KHR = VkMemoryRequirements2
VkMutableDescriptorTypeCreateInfoVALVE = VkMutableDescriptorTypeCreateInfoEXT
VkMutableDescriptorTypeListVALVE = VkMutableDescriptorTypeListEXT
VkPhysicalDevice16BitStorageFeaturesKHR = VkPhysicalDevice16BitStorageFeatures
VkPhysicalDevice8BitStorageFeaturesKHR = VkPhysicalDevice8BitStorageFeatures
VkPhysicalDeviceBufferAddressFeaturesEXT = VkPhysicalDeviceBufferDeviceAddressFeaturesEXT
VkPhysicalDeviceBufferDeviceAddressFeaturesKHR = VkPhysicalDeviceBufferDeviceAddressFeatures
VkPhysicalDeviceDepthStencilResolvePropertiesKHR = VkPhysicalDeviceDepthStencilResolveProperties
VkPhysicalDeviceDescriptorIndexingFeaturesEXT = VkPhysicalDeviceDescriptorIndexingFeatures
VkPhysicalDeviceDescriptorIndexingPropertiesEXT = VkPhysicalDeviceDescriptorIndexingProperties
VkPhysicalDeviceDriverPropertiesKHR = VkPhysicalDeviceDriverProperties
VkPhysicalDeviceDynamicRenderingFeaturesKHR = VkPhysicalDeviceDynamicRenderingFeatures
VkPhysicalDeviceExternalBufferInfoKHR = VkPhysicalDeviceExternalBufferInfo
VkPhysicalDeviceExternalFenceInfoKHR = VkPhysicalDeviceExternalFenceInfo
VkPhysicalDeviceExternalImageFormatInfoKHR = VkPhysicalDeviceExternalImageFormatInfo
VkPhysicalDeviceExternalSciBufFeaturesNV = VkPhysicalDeviceExternalMemorySciBufFeaturesNV
VkPhysicalDeviceExternalSemaphoreInfoKHR = VkPhysicalDeviceExternalSemaphoreInfo
VkPhysicalDeviceFeatures2KHR = VkPhysicalDeviceFeatures2
VkPhysicalDeviceFloat16Int8FeaturesKHR = VkPhysicalDeviceShaderFloat16Int8Features
VkPhysicalDeviceFloatControlsPropertiesKHR = VkPhysicalDeviceFloatControlsProperties
VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV = VkPhysicalDeviceFragmentShaderBarycentricFeaturesKHR
VkPhysicalDeviceGlobalPriorityQueryFeaturesEXT = VkPhysicalDeviceGlobalPriorityQueryFeaturesKHR
VkPhysicalDeviceGroupPropertiesKHR = VkPhysicalDeviceGroupProperties
VkPhysicalDeviceHostQueryResetFeaturesEXT = VkPhysicalDeviceHostQueryResetFeatures
VkPhysicalDeviceIDPropertiesKHR = VkPhysicalDeviceIDProperties
VkPhysicalDeviceImageFormatInfo2KHR = VkPhysicalDeviceImageFormatInfo2
VkPhysicalDeviceImageRobustnessFeaturesEXT = VkPhysicalDeviceImageRobustnessFeatures
VkPhysicalDeviceImagelessFramebufferFeaturesKHR = VkPhysicalDeviceImagelessFramebufferFeatures
VkPhysicalDeviceIndexTypeUint8FeaturesEXT = VkPhysicalDeviceIndexTypeUint8FeaturesKHR
VkPhysicalDeviceInlineUniformBlockFeaturesEXT = VkPhysicalDeviceInlineUniformBlockFeatures
VkPhysicalDeviceInlineUniformBlockPropertiesEXT = VkPhysicalDeviceInlineUniformBlockProperties
VkPhysicalDeviceLineRasterizationFeaturesEXT = VkPhysicalDeviceLineRasterizationFeaturesKHR
VkPhysicalDeviceLineRasterizationPropertiesEXT = VkPhysicalDeviceLineRasterizationPropertiesKHR
VkPhysicalDeviceMaintenance3PropertiesKHR = VkPhysicalDeviceMaintenance3Properties
VkPhysicalDeviceMaintenance4FeaturesKHR = VkPhysicalDeviceMaintenance4Features
VkPhysicalDeviceMaintenance4PropertiesKHR = VkPhysicalDeviceMaintenance4Properties
VkPhysicalDeviceMemoryProperties2KHR = VkPhysicalDeviceMemoryProperties2
VkPhysicalDeviceMultiviewFeaturesKHR = VkPhysicalDeviceMultiviewFeatures
VkPhysicalDeviceMultiviewPropertiesKHR = VkPhysicalDeviceMultiviewProperties
VkPhysicalDeviceMutableDescriptorTypeFeaturesVALVE = VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT
VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT = VkPhysicalDevicePipelineCreationCacheControlFeatures
VkPhysicalDevicePointClippingPropertiesKHR = VkPhysicalDevicePointClippingProperties
VkPhysicalDevicePrivateDataFeaturesEXT = VkPhysicalDevicePrivateDataFeatures
VkPhysicalDeviceProperties2KHR = VkPhysicalDeviceProperties2
VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesARM = VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT
VkPhysicalDeviceSamplerFilterMinmaxPropertiesEXT = VkPhysicalDeviceSamplerFilterMinmaxProperties
VkPhysicalDeviceSamplerYcbcrConversionFeaturesKHR = VkPhysicalDeviceSamplerYcbcrConversionFeatures
VkPhysicalDeviceScalarBlockLayoutFeaturesEXT = VkPhysicalDeviceScalarBlockLayoutFeatures
VkPhysicalDeviceSeparateDepthStencilLayoutsFeaturesKHR = VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures
VkPhysicalDeviceShaderAtomicInt64FeaturesKHR = VkPhysicalDeviceShaderAtomicInt64Features
VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT = VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures
VkPhysicalDeviceShaderDrawParameterFeatures = VkPhysicalDeviceShaderDrawParametersFeatures
VkPhysicalDeviceShaderFloat16Int8FeaturesKHR = VkPhysicalDeviceShaderFloat16Int8Features
VkPhysicalDeviceShaderIntegerDotProductFeaturesKHR = VkPhysicalDeviceShaderIntegerDotProductFeatures
VkPhysicalDeviceShaderIntegerDotProductPropertiesKHR = VkPhysicalDeviceShaderIntegerDotProductProperties
VkPhysicalDeviceShaderSubgroupExtendedTypesFeaturesKHR = VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures
VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR = VkPhysicalDeviceShaderTerminateInvocationFeatures
VkPhysicalDeviceSparseImageFormatInfo2KHR = VkPhysicalDeviceSparseImageFormatInfo2
VkPhysicalDeviceSubgroupSizeControlFeaturesEXT = VkPhysicalDeviceSubgroupSizeControlFeatures
VkPhysicalDeviceSubgroupSizeControlPropertiesEXT = VkPhysicalDeviceSubgroupSizeControlProperties
VkPhysicalDeviceSynchronization2FeaturesKHR = VkPhysicalDeviceSynchronization2Features
VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT = VkPhysicalDeviceTexelBufferAlignmentProperties
VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT = VkPhysicalDeviceTextureCompressionASTCHDRFeatures
VkPhysicalDeviceTimelineSemaphoreFeaturesKHR = VkPhysicalDeviceTimelineSemaphoreFeatures
VkPhysicalDeviceTimelineSemaphorePropertiesKHR = VkPhysicalDeviceTimelineSemaphoreProperties
VkPhysicalDeviceToolPropertiesEXT = VkPhysicalDeviceToolProperties
VkPhysicalDeviceUniformBufferStandardLayoutFeaturesKHR = VkPhysicalDeviceUniformBufferStandardLayoutFeatures
VkPhysicalDeviceVariablePointerFeatures = VkPhysicalDeviceVariablePointersFeatures
VkPhysicalDeviceVariablePointerFeaturesKHR = VkPhysicalDeviceVariablePointersFeatures
VkPhysicalDeviceVariablePointersFeaturesKHR = VkPhysicalDeviceVariablePointersFeatures
VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT = VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR
VkPhysicalDeviceVulkanMemoryModelFeaturesKHR = VkPhysicalDeviceVulkanMemoryModelFeatures
VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeaturesKHR = VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeatures
VkPipelineCreationFeedbackCreateInfoEXT = VkPipelineCreationFeedbackCreateInfo
VkPipelineCreationFeedbackEXT = VkPipelineCreationFeedback
VkPipelineInfoEXT = VkPipelineInfoKHR
VkPipelineRasterizationLineStateCreateInfoEXT = VkPipelineRasterizationLineStateCreateInfoKHR
VkPipelineRenderingCreateInfoKHR = VkPipelineRenderingCreateInfo
VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT = VkPipelineShaderStageRequiredSubgroupSizeCreateInfo
VkPipelineTessellationDomainOriginStateCreateInfoKHR = VkPipelineTessellationDomainOriginStateCreateInfo
VkPipelineVertexInputDivisorStateCreateInfoEXT = VkPipelineVertexInputDivisorStateCreateInfoKHR
VkPrivateDataSlotCreateInfoEXT = VkPrivateDataSlotCreateInfo
VkQueryPoolCreateInfoINTEL = VkQueryPoolPerformanceQueryCreateInfoINTEL
VkQueueFamilyGlobalPriorityPropertiesEXT = VkQueueFamilyGlobalPriorityPropertiesKHR
VkQueueFamilyProperties2KHR = VkQueueFamilyProperties2
VkRenderPassAttachmentBeginInfoKHR = VkRenderPassAttachmentBeginInfo
VkRenderPassCreateInfo2KHR = VkRenderPassCreateInfo2
VkRenderPassInputAttachmentAspectCreateInfoKHR = VkRenderPassInputAttachmentAspectCreateInfo
VkRenderPassMultiviewCreateInfoKHR = VkRenderPassMultiviewCreateInfo
VkRenderingAttachmentInfoKHR = VkRenderingAttachmentInfo
VkRenderingInfoKHR = VkRenderingInfo
VkResolveImageInfo2KHR = VkResolveImageInfo2
VkSamplerReductionModeCreateInfoEXT = VkSamplerReductionModeCreateInfo
VkSamplerYcbcrConversionCreateInfoKHR = VkSamplerYcbcrConversionCreateInfo
VkSamplerYcbcrConversionImageFormatPropertiesKHR = VkSamplerYcbcrConversionImageFormatProperties
VkSamplerYcbcrConversionInfoKHR = VkSamplerYcbcrConversionInfo
VkSemaphoreSignalInfoKHR = VkSemaphoreSignalInfo
VkSemaphoreSubmitInfoKHR = VkSemaphoreSubmitInfo
VkSemaphoreTypeCreateInfoKHR = VkSemaphoreTypeCreateInfo
VkSemaphoreWaitInfoKHR = VkSemaphoreWaitInfo
VkShaderRequiredSubgroupSizeCreateInfoEXT = VkPipelineShaderStageRequiredSubgroupSizeCreateInfo
VkSparseImageFormatProperties2KHR = VkSparseImageFormatProperties2
VkSparseImageMemoryRequirements2KHR = VkSparseImageMemoryRequirements2
VkSubmitInfo2KHR = VkSubmitInfo2
VkSubpassBeginInfoKHR = VkSubpassBeginInfo
VkSubpassDependency2KHR = VkSubpassDependency2
VkSubpassDescription2KHR = VkSubpassDescription2
VkSubpassDescriptionDepthStencilResolveKHR = VkSubpassDescriptionDepthStencilResolve
VkSubpassEndInfoKHR = VkSubpassEndInfo
VkSubresourceLayout2EXT = VkSubresourceLayout2KHR
VkTimelineSemaphoreSubmitInfoKHR = VkTimelineSemaphoreSubmitInfo
VkTransformMatrixNV = VkTransformMatrixKHR
VkVertexInputBindingDivisorDescriptionEXT = VkVertexInputBindingDivisorDescriptionKHR
VkWriteDescriptorSetInlineUniformBlockEXT = VkWriteDescriptorSetInlineUniformBlock
