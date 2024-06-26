import ctypes

class VkPhysicalDeviceDescriptorIndexingFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderInputAttachmentArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderUniformTexelBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderStorageTexelBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderUniformBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderSampledImageArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageImageArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderInputAttachmentArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderUniformTexelBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageTexelBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('descriptorBindingUniformBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingSampledImageUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageImageUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingUniformTexelBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageTexelBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingUpdateUnusedWhilePending', ctypes.c_uint32),
        ('descriptorBindingPartiallyBound', ctypes.c_uint32),
        ('descriptorBindingVariableDescriptorCount', ctypes.c_uint32),
        ('runtimeDescriptorArray', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shaderInputAttachmentArrayDynamicIndexing': 'shader_input_attachment_array_dynamic_indexing',
        'shaderUniformTexelBufferArrayDynamicIndexing': 'shader_uniform_texel_buffer_array_dynamic_indexing',
        'shaderStorageTexelBufferArrayDynamicIndexing': 'shader_storage_texel_buffer_array_dynamic_indexing',
        'shaderUniformBufferArrayNonUniformIndexing': 'shader_uniform_buffer_array_non_uniform_indexing',
        'shaderSampledImageArrayNonUniformIndexing': 'shader_sampled_image_array_non_uniform_indexing',
        'shaderStorageBufferArrayNonUniformIndexing': 'shader_storage_buffer_array_non_uniform_indexing',
        'shaderStorageImageArrayNonUniformIndexing': 'shader_storage_image_array_non_uniform_indexing',
        'shaderInputAttachmentArrayNonUniformIndexing': 'shader_input_attachment_array_non_uniform_indexing',
        'shaderUniformTexelBufferArrayNonUniformIndexing': 'shader_uniform_texel_buffer_array_non_uniform_indexing',
        'shaderStorageTexelBufferArrayNonUniformIndexing': 'shader_storage_texel_buffer_array_non_uniform_indexing',
        'descriptorBindingUniformBufferUpdateAfterBind': 'descriptor_binding_uniform_buffer_update_after_bind',
        'descriptorBindingSampledImageUpdateAfterBind': 'descriptor_binding_sampled_image_update_after_bind',
        'descriptorBindingStorageImageUpdateAfterBind': 'descriptor_binding_storage_image_update_after_bind',
        'descriptorBindingStorageBufferUpdateAfterBind': 'descriptor_binding_storage_buffer_update_after_bind',
        'descriptorBindingUniformTexelBufferUpdateAfterBind': 'descriptor_binding_uniform_texel_buffer_update_after_bind',
        'descriptorBindingStorageTexelBufferUpdateAfterBind': 'descriptor_binding_storage_texel_buffer_update_after_bind',
        'descriptorBindingUpdateUnusedWhilePending': 'descriptor_binding_update_unused_while_pending',
        'descriptorBindingPartiallyBound': 'descriptor_binding_partially_bound',
        'descriptorBindingVariableDescriptorCount': 'descriptor_binding_variable_descriptor_count',
        'runtimeDescriptorArray': 'runtime_descriptor_array',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDescriptorIndexingFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderInputAttachmentArrayDynamicIndexing': ctypes.c_uint32,
    'shaderUniformTexelBufferArrayDynamicIndexing': ctypes.c_uint32,
    'shaderStorageTexelBufferArrayDynamicIndexing': ctypes.c_uint32,
    'shaderUniformBufferArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderSampledImageArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderStorageBufferArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderStorageImageArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderInputAttachmentArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderUniformTexelBufferArrayNonUniformIndexing': ctypes.c_uint32,
    'shaderStorageTexelBufferArrayNonUniformIndexing': ctypes.c_uint32,
    'descriptorBindingUniformBufferUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingSampledImageUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingStorageImageUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingStorageBufferUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingUniformTexelBufferUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingStorageTexelBufferUpdateAfterBind': ctypes.c_uint32,
    'descriptorBindingUpdateUnusedWhilePending': ctypes.c_uint32,
    'descriptorBindingPartiallyBound': ctypes.c_uint32,
    'descriptorBindingVariableDescriptorCount': ctypes.c_uint32,
    'runtimeDescriptorArray': ctypes.c_uint32,
}
