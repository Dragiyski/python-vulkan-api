import ctypes

class VkPhysicalDeviceProperties2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPhysicalDeviceAccelerationStructurePropertiesKHR',
        'VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT',
        'VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI',
        'VkPhysicalDeviceConservativeRasterizationPropertiesEXT',
        'VkPhysicalDeviceCooperativeMatrixPropertiesKHR',
        'VkPhysicalDeviceCooperativeMatrixPropertiesNV',
        'VkPhysicalDeviceCopyMemoryIndirectPropertiesNV',
        'VkPhysicalDeviceCudaKernelLaunchPropertiesNV',
        'VkPhysicalDeviceCustomBorderColorPropertiesEXT',
        'VkPhysicalDeviceDepthStencilResolveProperties',
        'VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT',
        'VkPhysicalDeviceDescriptorBufferPropertiesEXT',
        'VkPhysicalDeviceDescriptorIndexingProperties',
        'VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV',
        'VkPhysicalDeviceDiscardRectanglePropertiesEXT',
        'VkPhysicalDeviceDisplacementMicromapPropertiesNV',
        'VkPhysicalDeviceDriverProperties',
        'VkPhysicalDeviceDrmPropertiesEXT',
        'VkPhysicalDeviceExtendedDynamicState3PropertiesEXT',
        'VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV',
        'VkPhysicalDeviceExternalFormatResolvePropertiesANDROID',
        'VkPhysicalDeviceExternalMemoryHostPropertiesEXT',
        'VkPhysicalDeviceFloatControlsProperties',
        'VkPhysicalDeviceFragmentDensityMap2PropertiesEXT',
        'VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM',
        'VkPhysicalDeviceFragmentDensityMapPropertiesEXT',
        'VkPhysicalDeviceFragmentShaderBarycentricPropertiesKHR',
        'VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV',
        'VkPhysicalDeviceFragmentShadingRatePropertiesKHR',
        'VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT',
        'VkPhysicalDeviceHostImageCopyPropertiesEXT',
        'VkPhysicalDeviceIDProperties',
        'VkPhysicalDeviceImageAlignmentControlPropertiesMESA',
        'VkPhysicalDeviceImageProcessing2PropertiesQCOM',
        'VkPhysicalDeviceImageProcessingPropertiesQCOM',
        'VkPhysicalDeviceInlineUniformBlockProperties',
        'VkPhysicalDeviceLayeredDriverPropertiesMSFT',
        'VkPhysicalDeviceLegacyVertexAttributesPropertiesEXT',
        'VkPhysicalDeviceLineRasterizationPropertiesKHR',
        'VkPhysicalDeviceMaintenance3Properties',
        'VkPhysicalDeviceMaintenance4Properties',
        'VkPhysicalDeviceMaintenance5PropertiesKHR',
        'VkPhysicalDeviceMaintenance6PropertiesKHR',
        'VkPhysicalDeviceMapMemoryPlacedPropertiesEXT',
        'VkPhysicalDeviceMemoryDecompressionPropertiesNV',
        'VkPhysicalDeviceMeshShaderPropertiesEXT',
        'VkPhysicalDeviceMeshShaderPropertiesNV',
        'VkPhysicalDeviceMultiDrawPropertiesEXT',
        'VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX',
        'VkPhysicalDeviceMultiviewProperties',
        'VkPhysicalDeviceNestedCommandBufferPropertiesEXT',
        'VkPhysicalDeviceOpacityMicromapPropertiesEXT',
        'VkPhysicalDeviceOpticalFlowPropertiesNV',
        'VkPhysicalDevicePCIBusInfoPropertiesEXT',
        'VkPhysicalDevicePerformanceQueryPropertiesKHR',
        'VkPhysicalDevicePipelineRobustnessPropertiesEXT',
        'VkPhysicalDevicePointClippingProperties',
        'VkPhysicalDevicePortabilitySubsetPropertiesKHR',
        'VkPhysicalDeviceProtectedMemoryProperties',
        'VkPhysicalDeviceProvokingVertexPropertiesEXT',
        'VkPhysicalDevicePushDescriptorPropertiesKHR',
        'VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV',
        'VkPhysicalDeviceRayTracingPipelinePropertiesKHR',
        'VkPhysicalDeviceRayTracingPropertiesNV',
        'VkPhysicalDeviceRenderPassStripedPropertiesARM',
        'VkPhysicalDeviceRobustness2PropertiesEXT',
        'VkPhysicalDeviceSampleLocationsPropertiesEXT',
        'VkPhysicalDeviceSamplerFilterMinmaxProperties',
        'VkPhysicalDeviceSchedulingControlsPropertiesARM',
        'VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM',
        'VkPhysicalDeviceShaderCoreProperties2AMD',
        'VkPhysicalDeviceShaderCorePropertiesAMD',
        'VkPhysicalDeviceShaderCorePropertiesARM',
        'VkPhysicalDeviceShaderEnqueuePropertiesAMDX',
        'VkPhysicalDeviceShaderIntegerDotProductProperties',
        'VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT',
        'VkPhysicalDeviceShaderObjectPropertiesEXT',
        'VkPhysicalDeviceShaderSMBuiltinsPropertiesNV',
        'VkPhysicalDeviceShaderTileImagePropertiesEXT',
        'VkPhysicalDeviceShadingRateImagePropertiesNV',
        'VkPhysicalDeviceSubgroupProperties',
        'VkPhysicalDeviceSubgroupSizeControlProperties',
        'VkPhysicalDeviceSubpassShadingPropertiesHUAWEI',
        'VkPhysicalDeviceTexelBufferAlignmentProperties',
        'VkPhysicalDeviceTimelineSemaphoreProperties',
        'VkPhysicalDeviceTransformFeedbackPropertiesEXT',
        'VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT',
        'VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR',
        'VkPhysicalDeviceVulkan11Properties',
        'VkPhysicalDeviceVulkan12Properties',
        'VkPhysicalDeviceVulkan13Properties',
    }
    _includes_ = {
        'VkPhysicalDeviceProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceProperties2',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'properties': 'properties',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPhysicalDeviceProperties import VkPhysicalDeviceProperties

VkPhysicalDeviceProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkPhysicalDeviceProperties),
]

VkPhysicalDeviceProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'properties': VkPhysicalDeviceProperties,
}
