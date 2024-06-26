import ctypes

class VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('advancedBlendMaxColorAttachments', ctypes.c_uint32),
        ('advancedBlendIndependentBlend', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedSrcColor', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedDstColor', ctypes.c_uint32),
        ('advancedBlendCorrelatedOverlap', ctypes.c_uint32),
        ('advancedBlendAllOperations', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'advancedBlendMaxColorAttachments': 'advanced_blend_max_color_attachments',
        'advancedBlendIndependentBlend': 'advanced_blend_independent_blend',
        'advancedBlendNonPremultipliedSrcColor': 'advanced_blend_non_premultiplied_src_color',
        'advancedBlendNonPremultipliedDstColor': 'advanced_blend_non_premultiplied_dst_color',
        'advancedBlendCorrelatedOverlap': 'advanced_blend_correlated_overlap',
        'advancedBlendAllOperations': 'advanced_blend_all_operations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_blend_operation_advanced',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'advancedBlendMaxColorAttachments': ctypes.c_uint32,
    'advancedBlendIndependentBlend': ctypes.c_uint32,
    'advancedBlendNonPremultipliedSrcColor': ctypes.c_uint32,
    'advancedBlendNonPremultipliedDstColor': ctypes.c_uint32,
    'advancedBlendCorrelatedOverlap': ctypes.c_uint32,
    'advancedBlendAllOperations': ctypes.c_uint32,
}
