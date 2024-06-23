import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDisplayModeParametersKHR',
        'VkDisplayPlaneCapabilitiesKHR',
        'VkDisplayPropertiesKHR',
        'VkDisplaySurfaceCreateInfoKHR',
        'VkFragmentShadingRateAttachmentInfoKHR',
        'VkImageViewSampleWeightCreateInfoQCOM',
        'VkMultisamplePropertiesEXT',
        'VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM',
        'VkPhysicalDeviceFragmentDensityMapPropertiesEXT',
        'VkPhysicalDeviceFragmentShadingRateKHR',
        'VkPhysicalDeviceFragmentShadingRatePropertiesKHR',
        'VkPhysicalDeviceImageProcessing2PropertiesQCOM',
        'VkPhysicalDeviceImageProcessingPropertiesQCOM',
        'VkPhysicalDeviceRenderPassStripedPropertiesARM',
        'VkPhysicalDeviceSampleLocationsPropertiesEXT',
        'VkPhysicalDeviceShadingRateImagePropertiesNV',
        'VkPipelineFragmentShadingRateStateCreateInfoKHR',
        'VkRect2D',
        'VkRectLayerKHR',
        'VkRenderingFragmentShadingRateAttachmentInfoKHR',
        'VkSampleLocationsInfoEXT',
        'VkSamplerBlockMatchWindowCreateInfoQCOM',
        'VkSurfaceCapabilities2EXT',
        'VkSurfaceCapabilitiesKHR',
        'VkSurfacePresentScalingCapabilitiesEXT',
        'VkSwapchainCreateInfoKHR',
        'VkTilePropertiesQCOM',
        'VkVideoCapabilitiesKHR',
        'VkVideoEncodeCapabilitiesKHR',
        'VkVideoEncodeH265CapabilitiesKHR',
        'VkVideoPictureResourceInfoKHR',
        'VkVideoSessionCreateInfoKHR',
    },
    'input_of': {
        'vkCmdSetFragmentShadingRateKHR',
    },
    'output_of': {
        'vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI',
        'vkGetRenderAreaGranularity',
        'vkGetRenderingAreaGranularityKHR',
    },
    'member_map': {
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
    }
}
