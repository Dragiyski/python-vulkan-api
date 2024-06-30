from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan12Properties'
_member_list_ = ['sType', 'pNext', 'driverID', 'driverName', 'driverInfo', 'conformanceVersion', 'denormBehaviorIndependence', 'roundingModeIndependence', 'shaderSignedZeroInfNanPreserveFloat16', 'shaderSignedZeroInfNanPreserveFloat32', 'shaderSignedZeroInfNanPreserveFloat64', 'shaderDenormPreserveFloat16', 'shaderDenormPreserveFloat32', 'shaderDenormPreserveFloat64', 'shaderDenormFlushToZeroFloat16', 'shaderDenormFlushToZeroFloat32', 'shaderDenormFlushToZeroFloat64', 'shaderRoundingModeRTEFloat16', 'shaderRoundingModeRTEFloat32', 'shaderRoundingModeRTEFloat64', 'shaderRoundingModeRTZFloat16', 'shaderRoundingModeRTZFloat32', 'shaderRoundingModeRTZFloat64', 'maxUpdateAfterBindDescriptorsInAllPools', 'shaderUniformBufferArrayNonUniformIndexingNative', 'shaderSampledImageArrayNonUniformIndexingNative', 'shaderStorageBufferArrayNonUniformIndexingNative', 'shaderStorageImageArrayNonUniformIndexingNative', 'shaderInputAttachmentArrayNonUniformIndexingNative', 'robustBufferAccessUpdateAfterBind', 'quadDivergentImplicitLod', 'maxPerStageDescriptorUpdateAfterBindSamplers', 'maxPerStageDescriptorUpdateAfterBindUniformBuffers', 'maxPerStageDescriptorUpdateAfterBindStorageBuffers', 'maxPerStageDescriptorUpdateAfterBindSampledImages', 'maxPerStageDescriptorUpdateAfterBindStorageImages', 'maxPerStageDescriptorUpdateAfterBindInputAttachments', 'maxPerStageUpdateAfterBindResources', 'maxDescriptorSetUpdateAfterBindSamplers', 'maxDescriptorSetUpdateAfterBindUniformBuffers', 'maxDescriptorSetUpdateAfterBindUniformBuffersDynamic', 'maxDescriptorSetUpdateAfterBindStorageBuffers', 'maxDescriptorSetUpdateAfterBindStorageBuffersDynamic', 'maxDescriptorSetUpdateAfterBindSampledImages', 'maxDescriptorSetUpdateAfterBindStorageImages', 'maxDescriptorSetUpdateAfterBindInputAttachments', 'supportedDepthResolveModes', 'supportedStencilResolveModes', 'independentResolveNone', 'independentResolve', 'filterMinmaxSingleComponentFormats', 'filterMinmaxImageComponentMapping', 'maxTimelineSemaphoreValueDifference', 'framebufferIntegerColorSampleCounts']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'driverID': {
        'type': CIntType('c_int'),
        'type_name': 'VkDriverId',
        'enum': 'VkDriverId',
        'is_string': False,
    },
    'driverName': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'driverInfo': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'conformanceVersion': {
        'type': CComplexType('VkConformanceVersion'),
        'type_name': 'VkConformanceVersion',
        'structure': 'VkConformanceVersion',
        'is_string': False,
    },
    'denormBehaviorIndependence': {
        'type': CIntType('c_int'),
        'type_name': 'VkShaderFloatControlsIndependence',
        'enum': 'VkShaderFloatControlsIndependence',
        'is_string': False,
    },
    'roundingModeIndependence': {
        'type': CIntType('c_int'),
        'type_name': 'VkShaderFloatControlsIndependence',
        'enum': 'VkShaderFloatControlsIndependence',
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSignedZeroInfNanPreserveFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormPreserveFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDenormFlushToZeroFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTEFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderRoundingModeRTZFloat64': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxUpdateAfterBindDescriptorsInAllPools': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderUniformBufferArrayNonUniformIndexingNative': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSampledImageArrayNonUniformIndexingNative': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageBufferArrayNonUniformIndexingNative': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageImageArrayNonUniformIndexingNative': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderInputAttachmentArrayNonUniformIndexingNative': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'robustBufferAccessUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'quadDivergentImplicitLod': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindUniformBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindStorageBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindSampledImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindStorageImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindInputAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageUpdateAfterBindResources': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindUniformBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindUniformBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindStorageBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindStorageBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindSampledImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindStorageImages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindInputAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'supportedDepthResolveModes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlags',
        'enum': 'VkResolveModeFlags',
        'is_string': False,
    },
    'supportedStencilResolveModes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlags',
        'enum': 'VkResolveModeFlags',
        'is_string': False,
    },
    'independentResolveNone': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'independentResolve': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'filterMinmaxSingleComponentFormats': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'filterMinmaxImageComponentMapping': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTimelineSemaphoreValueDifference': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'framebufferIntegerColorSampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkConformanceVersion',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
