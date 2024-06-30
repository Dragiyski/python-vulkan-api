from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExtent2D'
_member_list_ = ['width', 'height']
_member_info_ = {
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
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
}
_input_of_ = {
    'vkCmdSetFragmentShadingRateKHR',
}
_output_of_ = {
    'vkGetDeviceSubpassShadingMaxWorkgroupSizeHUAWEI',
    'vkGetRenderAreaGranularity',
    'vkGetRenderingAreaGranularityKHR',
}
