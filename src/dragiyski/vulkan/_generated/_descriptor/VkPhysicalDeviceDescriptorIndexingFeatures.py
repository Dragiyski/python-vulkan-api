from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDescriptorIndexingFeatures'
_member_list_ = ['sType', 'pNext', 'shaderInputAttachmentArrayDynamicIndexing', 'shaderUniformTexelBufferArrayDynamicIndexing', 'shaderStorageTexelBufferArrayDynamicIndexing', 'shaderUniformBufferArrayNonUniformIndexing', 'shaderSampledImageArrayNonUniformIndexing', 'shaderStorageBufferArrayNonUniformIndexing', 'shaderStorageImageArrayNonUniformIndexing', 'shaderInputAttachmentArrayNonUniformIndexing', 'shaderUniformTexelBufferArrayNonUniformIndexing', 'shaderStorageTexelBufferArrayNonUniformIndexing', 'descriptorBindingUniformBufferUpdateAfterBind', 'descriptorBindingSampledImageUpdateAfterBind', 'descriptorBindingStorageImageUpdateAfterBind', 'descriptorBindingStorageBufferUpdateAfterBind', 'descriptorBindingUniformTexelBufferUpdateAfterBind', 'descriptorBindingStorageTexelBufferUpdateAfterBind', 'descriptorBindingUpdateUnusedWhilePending', 'descriptorBindingPartiallyBound', 'descriptorBindingVariableDescriptorCount', 'runtimeDescriptorArray']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderInputAttachmentArrayDynamicIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderUniformTexelBufferArrayDynamicIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageTexelBufferArrayDynamicIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderUniformBufferArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSampledImageArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageBufferArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageImageArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderInputAttachmentArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderUniformTexelBufferArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderStorageTexelBufferArrayNonUniformIndexing': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingUniformBufferUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingSampledImageUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingStorageImageUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingStorageBufferUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingUniformTexelBufferUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingStorageTexelBufferUpdateAfterBind': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingUpdateUnusedWhilePending': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingPartiallyBound': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorBindingVariableDescriptorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'runtimeDescriptorArray': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
