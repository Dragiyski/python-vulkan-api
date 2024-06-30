from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMaintenance7PropertiesKHR'
_member_list_ = ['sType', 'pNext', 'robustFragmentShadingRateAttachmentAccess', 'separateDepthStencilAttachmentAccess', 'maxDescriptorSetTotalUniformBuffersDynamic', 'maxDescriptorSetTotalStorageBuffersDynamic', 'maxDescriptorSetTotalBuffersDynamic', 'maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic', 'maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic', 'maxDescriptorSetUpdateAfterBindTotalBuffersDynamic']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_7_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'robustFragmentShadingRateAttachmentAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'separateDepthStencilAttachmentAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetTotalUniformBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetTotalStorageBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetTotalBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindTotalBuffersDynamic': {
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
