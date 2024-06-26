import ctypes

class VkWriteDescriptorSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkWriteDescriptorSetAccelerationStructureKHR',
        'VkWriteDescriptorSetAccelerationStructureNV',
        'VkWriteDescriptorSetInlineUniformBlock',
    }
    _includes_ = {
        'VkDescriptorBufferInfo',
        'VkDescriptorImageInfo',
    }
    _included_in_ = {
        'VkPushDescriptorSetInfoKHR',
    }
    _input_of_ = {
        'vkCmdPushDescriptorSetKHR',
        'vkUpdateDescriptorSets',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'dstSet': 'dst_set',
        'dstBinding': 'dst_binding',
        'dstArrayElement': 'dst_array_element',
        'descriptorCount': 'descriptor_count',
        'descriptorType': 'descriptor_type',
        'pImageInfo': 'image_info',
        'pBufferInfo': 'buffer_info',
        'pTexelBufferView': 'texel_buffer_view',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'descriptorType': 'VkDescriptorType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDescriptorBufferInfo import VkDescriptorBufferInfo
from .VkDescriptorImageInfo import VkDescriptorImageInfo

VkWriteDescriptorSet._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('dstSet', ctypes.c_void_p),
    ('dstBinding', ctypes.c_uint32),
    ('dstArrayElement', ctypes.c_uint32),
    ('descriptorCount', ctypes.c_uint32),
    ('descriptorType', ctypes.c_int),
    ('pImageInfo', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pBufferInfo', ctypes.POINTER(VkDescriptorBufferInfo)),
    ('pTexelBufferView', ctypes.POINTER(ctypes.c_void_p)),
]

VkWriteDescriptorSet._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dstSet': ctypes.c_void_p,
    'dstBinding': ctypes.c_uint32,
    'dstArrayElement': ctypes.c_uint32,
    'descriptorCount': ctypes.c_uint32,
    'descriptorType': ctypes.c_int,
    'pImageInfo': ctypes.POINTER(VkDescriptorImageInfo),
    'pBufferInfo': ctypes.POINTER(VkDescriptorBufferInfo),
    'pTexelBufferView': ctypes.POINTER(ctypes.c_void_p),
}
