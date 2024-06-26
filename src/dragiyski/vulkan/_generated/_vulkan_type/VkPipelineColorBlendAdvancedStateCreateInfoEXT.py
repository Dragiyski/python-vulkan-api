import ctypes

class VkPipelineColorBlendAdvancedStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineColorBlendStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcPremultiplied': 'src_premultiplied',
        'dstPremultiplied': 'dst_premultiplied',
        'blendOverlap': 'blend_overlap',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_blend_operation_advanced',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'blendOverlap': 'VkBlendOverlapEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineColorBlendAdvancedStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcPremultiplied': ctypes.c_uint32,
    'dstPremultiplied': ctypes.c_uint32,
    'blendOverlap': ctypes.c_int,
}
