import ctypes

class VkExtent2D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
    ]

    _init_ = []
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
    _python_name_ = {
        'width': 'width',
        'height': 'height',
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

VkExtent2D._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
}
