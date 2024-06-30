from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'size', 'usage', 'sharingMode', 'queueFamilyIndexCount', 'pQueueFamilyIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferCreateFlags',
        'enum': 'VkBufferCreateFlags',
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferUsageFlags',
        'enum': 'VkBufferUsageFlags',
        'is_string': False,
    },
    'sharingMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkSharingMode',
        'enum': 'VkSharingMode',
        'is_string': False,
    },
    'queueFamilyIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueueFamilyIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['queueFamilyIndexCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBufferCollectionBufferCreateInfoFUCHSIA',
    'VkBufferDeviceAddressCreateInfoEXT',
    'VkBufferOpaqueCaptureAddressCreateInfo',
    'VkBufferUsageFlags2CreateInfoKHR',
    'VkDedicatedAllocationBufferCreateInfoNV',
    'VkExternalMemoryBufferCreateInfo',
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    'VkVideoProfileListInfoKHR',
}
_includes_ = set()
_included_in_ = {
    'VkBufferConstraintsInfoFUCHSIA',
    'VkDeviceBufferMemoryRequirements',
}
_input_of_ = {
    'vkCreateBuffer',
}
_output_of_ = set()
