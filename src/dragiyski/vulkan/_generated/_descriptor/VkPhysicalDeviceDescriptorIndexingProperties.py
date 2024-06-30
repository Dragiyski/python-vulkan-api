from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDescriptorIndexingProperties'
_member_list_ = ['sType', 'pNext', 'maxUpdateAfterBindDescriptorsInAllPools', 'shaderUniformBufferArrayNonUniformIndexingNative', 'shaderSampledImageArrayNonUniformIndexingNative', 'shaderStorageBufferArrayNonUniformIndexingNative', 'shaderStorageImageArrayNonUniformIndexingNative', 'shaderInputAttachmentArrayNonUniformIndexingNative', 'robustBufferAccessUpdateAfterBind', 'quadDivergentImplicitLod', 'maxPerStageDescriptorUpdateAfterBindSamplers', 'maxPerStageDescriptorUpdateAfterBindUniformBuffers', 'maxPerStageDescriptorUpdateAfterBindStorageBuffers', 'maxPerStageDescriptorUpdateAfterBindSampledImages', 'maxPerStageDescriptorUpdateAfterBindStorageImages', 'maxPerStageDescriptorUpdateAfterBindInputAttachments', 'maxPerStageUpdateAfterBindResources', 'maxDescriptorSetUpdateAfterBindSamplers', 'maxDescriptorSetUpdateAfterBindUniformBuffers', 'maxDescriptorSetUpdateAfterBindUniformBuffersDynamic', 'maxDescriptorSetUpdateAfterBindStorageBuffers', 'maxDescriptorSetUpdateAfterBindStorageBuffersDynamic', 'maxDescriptorSetUpdateAfterBindSampledImages', 'maxDescriptorSetUpdateAfterBindStorageImages', 'maxDescriptorSetUpdateAfterBindInputAttachments']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
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
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
