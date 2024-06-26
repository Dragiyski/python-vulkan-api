import ctypes

class VkTilePropertiesQCOM(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkExtent3D',
        'VkOffset2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDynamicRenderingTilePropertiesQCOM',
        'vkGetFramebufferTilePropertiesQCOM',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'tileSize': 'tile_size',
        'apronSize': 'apron_size',
        'origin': 'origin',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_tile_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_TILE_PROPERTIES_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_TILE_PROPERTIES_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkExtent3D import VkExtent3D
from .VkOffset2D import VkOffset2D

VkTilePropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('tileSize', VkExtent3D),
    ('apronSize', VkExtent2D),
    ('origin', VkOffset2D),
]

VkTilePropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'tileSize': VkExtent3D,
    'apronSize': VkExtent2D,
    'origin': VkOffset2D,
}
