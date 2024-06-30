from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan12Features'
_member_list_ = ['sType', 'pNext', 'samplerMirrorClampToEdge', 'drawIndirectCount', 'storageBuffer8BitAccess', 'uniformAndStorageBuffer8BitAccess', 'storagePushConstant8', 'shaderBufferInt64Atomics', 'shaderSharedInt64Atomics', 'shaderFloat16', 'shaderInt8', 'descriptorIndexing', 'shaderInputAttachmentArrayDynamicIndexing', 'shaderUniformTexelBufferArrayDynamicIndexing', 'shaderStorageTexelBufferArrayDynamicIndexing', 'shaderUniformBufferArrayNonUniformIndexing', 'shaderSampledImageArrayNonUniformIndexing', 'shaderStorageBufferArrayNonUniformIndexing', 'shaderStorageImageArrayNonUniformIndexing', 'shaderInputAttachmentArrayNonUniformIndexing', 'shaderUniformTexelBufferArrayNonUniformIndexing', 'shaderStorageTexelBufferArrayNonUniformIndexing', 'descriptorBindingUniformBufferUpdateAfterBind', 'descriptorBindingSampledImageUpdateAfterBind', 'descriptorBindingStorageImageUpdateAfterBind', 'descriptorBindingStorageBufferUpdateAfterBind', 'descriptorBindingUniformTexelBufferUpdateAfterBind', 'descriptorBindingStorageTexelBufferUpdateAfterBind', 'descriptorBindingUpdateUnusedWhilePending', 'descriptorBindingPartiallyBound', 'descriptorBindingVariableDescriptorCount', 'runtimeDescriptorArray', 'samplerFilterMinmax', 'scalarBlockLayout', 'imagelessFramebuffer', 'uniformBufferStandardLayout', 'shaderSubgroupExtendedTypes', 'separateDepthStencilLayouts', 'hostQueryReset', 'timelineSemaphore', 'bufferDeviceAddress', 'bufferDeviceAddressCaptureReplay', 'bufferDeviceAddressMultiDevice', 'vulkanMemoryModel', 'vulkanMemoryModelDeviceScope', 'vulkanMemoryModelAvailabilityVisibilityChains', 'shaderOutputViewportIndex', 'shaderOutputLayer', 'subgroupBroadcastDynamicId']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_FEATURES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'samplerMirrorClampToEdge': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'drawIndirectCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storageBuffer8BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uniformAndStorageBuffer8BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storagePushConstant8': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderBufferInt64Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSharedInt64Atomics': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderFloat16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderInt8': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorIndexing': {
        'type': CIntType('c_uint32'),
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
    'samplerFilterMinmax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'scalarBlockLayout': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imagelessFramebuffer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uniformBufferStandardLayout': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSubgroupExtendedTypes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'separateDepthStencilLayouts': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'hostQueryReset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'timelineSemaphore': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferDeviceAddress': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferDeviceAddressCaptureReplay': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferDeviceAddressMultiDevice': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vulkanMemoryModel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vulkanMemoryModelDeviceScope': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vulkanMemoryModelAvailabilityVisibilityChains': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderOutputViewportIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderOutputLayer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subgroupBroadcastDynamicId': {
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
