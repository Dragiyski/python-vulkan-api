import ctypes

class VkCopyDescriptorSet(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSet', ctypes.c_void_p),
        ('srcBinding', ctypes.c_uint32),
        ('srcArrayElement', ctypes.c_uint32),
        ('dstSet', ctypes.c_void_p),
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkUpdateDescriptorSets',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcSet': 'src_set',
        'srcBinding': 'src_binding',
        'srcArrayElement': 'src_array_element',
        'dstSet': 'dst_set',
        'dstBinding': 'dst_binding',
        'dstArrayElement': 'dst_array_element',
        'descriptorCount': 'descriptor_count',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET
        for function in self._init_:
            function(self, *args, **kwargs)

VkCopyDescriptorSet._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSet': ctypes.c_void_p,
    'srcBinding': ctypes.c_uint32,
    'srcArrayElement': ctypes.c_uint32,
    'dstSet': ctypes.c_void_p,
    'dstBinding': ctypes.c_uint32,
    'dstArrayElement': ctypes.c_uint32,
    'descriptorCount': ctypes.c_uint32,
}
