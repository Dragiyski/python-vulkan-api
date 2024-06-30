from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan11Features'
_member_list_ = ['sType', 'pNext', 'storageBuffer16BitAccess', 'uniformAndStorageBuffer16BitAccess', 'storagePushConstant16', 'storageInputOutput16', 'multiview', 'multiviewGeometryShader', 'multiviewTessellationShader', 'variablePointersStorageBuffer', 'variablePointers', 'protectedMemory', 'samplerYcbcrConversion', 'shaderDrawParameters']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_FEATURES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'storageBuffer16BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uniformAndStorageBuffer16BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storagePushConstant16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storageInputOutput16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multiview': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multiviewGeometryShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multiviewTessellationShader': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'variablePointersStorageBuffer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'variablePointers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'protectedMemory': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'samplerYcbcrConversion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderDrawParameters': {
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
