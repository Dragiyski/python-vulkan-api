import ctypes

class VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveTopologyListRestart', ctypes.c_uint32),
        ('primitiveTopologyPatchListRestart', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'primitiveTopologyListRestart': 'primitive_topology_list_restart',
        'primitiveTopologyPatchListRestart': 'primitive_topology_patch_list_restart',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_primitive_topology_list_restart',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVE_TOPOLOGY_LIST_RESTART_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVE_TOPOLOGY_LIST_RESTART_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'primitiveTopologyListRestart': ctypes.c_uint32,
    'primitiveTopologyPatchListRestart': ctypes.c_uint32,
}
