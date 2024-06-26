import ctypes

class VkPhysicalDeviceVulkan13Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustImageAccess', ctypes.c_uint32),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
        ('pipelineCreationCacheControl', ctypes.c_uint32),
        ('privateData', ctypes.c_uint32),
        ('shaderDemoteToHelperInvocation', ctypes.c_uint32),
        ('shaderTerminateInvocation', ctypes.c_uint32),
        ('subgroupSizeControl', ctypes.c_uint32),
        ('computeFullSubgroups', ctypes.c_uint32),
        ('synchronization2', ctypes.c_uint32),
        ('textureCompressionASTC_HDR', ctypes.c_uint32),
        ('shaderZeroInitializeWorkgroupMemory', ctypes.c_uint32),
        ('dynamicRendering', ctypes.c_uint32),
        ('shaderIntegerDotProduct', ctypes.c_uint32),
        ('maintenance4', ctypes.c_uint32),
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
        'robustImageAccess': 'robust_image_access',
        'inlineUniformBlock': 'inline_uniform_block',
        'descriptorBindingInlineUniformBlockUpdateAfterBind': 'descriptor_binding_inline_uniform_block_update_after_bind',
        'pipelineCreationCacheControl': 'pipeline_creation_cache_control',
        'privateData': 'private_data',
        'shaderDemoteToHelperInvocation': 'shader_demote_to_helper_invocation',
        'shaderTerminateInvocation': 'shader_terminate_invocation',
        'subgroupSizeControl': 'subgroup_size_control',
        'computeFullSubgroups': 'compute_full_subgroups',
        'synchronization2': 'synchronization2',
        'textureCompressionASTC_HDR': 'texture_compression_astc_hdr',
        'shaderZeroInitializeWorkgroupMemory': 'shader_zero_initialize_workgroup_memory',
        'dynamicRendering': 'dynamic_rendering',
        'shaderIntegerDotProduct': 'shader_integer_dot_product',
        'maintenance4': 'maintenance4',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_FEATURES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_FEATURES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceVulkan13Features._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'robustImageAccess': ctypes.c_uint32,
    'inlineUniformBlock': ctypes.c_uint32,
    'descriptorBindingInlineUniformBlockUpdateAfterBind': ctypes.c_uint32,
    'pipelineCreationCacheControl': ctypes.c_uint32,
    'privateData': ctypes.c_uint32,
    'shaderDemoteToHelperInvocation': ctypes.c_uint32,
    'shaderTerminateInvocation': ctypes.c_uint32,
    'subgroupSizeControl': ctypes.c_uint32,
    'computeFullSubgroups': ctypes.c_uint32,
    'synchronization2': ctypes.c_uint32,
    'textureCompressionASTC_HDR': ctypes.c_uint32,
    'shaderZeroInitializeWorkgroupMemory': ctypes.c_uint32,
    'dynamicRendering': ctypes.c_uint32,
    'shaderIntegerDotProduct': ctypes.c_uint32,
    'maintenance4': ctypes.c_uint32,
}
