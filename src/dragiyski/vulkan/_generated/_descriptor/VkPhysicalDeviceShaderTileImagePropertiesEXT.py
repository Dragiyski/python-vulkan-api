from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderTileImagePropertiesEXT'
_member_list_ = ['sType', 'pNext', 'shaderTileImageCoherentReadAccelerated', 'shaderTileImageReadSampleFromPixelRateInvocation', 'shaderTileImageReadFromHelperInvocation']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderTileImageCoherentReadAccelerated': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderTileImageReadSampleFromPixelRateInvocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderTileImageReadFromHelperInvocation': {
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
