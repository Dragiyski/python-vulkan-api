from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderCorePropertiesAMD'
_member_list_ = ['sType', 'pNext', 'shaderEngineCount', 'shaderArraysPerEngineCount', 'computeUnitsPerShaderArray', 'simdPerComputeUnit', 'wavefrontsPerSimd', 'wavefrontSize', 'sgprsPerSimd', 'minSgprAllocation', 'maxSgprAllocation', 'sgprAllocationGranularity', 'vgprsPerSimd', 'minVgprAllocation', 'maxVgprAllocation', 'vgprAllocationGranularity']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderEngineCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderArraysPerEngineCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'computeUnitsPerShaderArray': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'simdPerComputeUnit': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'wavefrontsPerSimd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'wavefrontSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sgprsPerSimd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minSgprAllocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxSgprAllocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sgprAllocationGranularity': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vgprsPerSimd': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minVgprAllocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxVgprAllocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vgprAllocationGranularity': {
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
