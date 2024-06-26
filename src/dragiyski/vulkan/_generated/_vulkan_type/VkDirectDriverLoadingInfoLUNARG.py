import ctypes

class VkDirectDriverLoadingInfoLUNARG(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDirectDriverLoadingListLUNARG',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pfnGetInstanceProcAddr': 'pfn_get_instance_proc_addr',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_LUNARG_direct_driver_loading',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDirectDriverLoadingFlagsLUNARG',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_INFO_LUNARG'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_INFO_LUNARG
        for function in self._init_:
            function(self, *args, **kwargs)


from .._vulkan_callback.vkGetInstanceProcAddrLUNARG import vkGetInstanceProcAddrLUNARG

VkDirectDriverLoadingInfoLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnGetInstanceProcAddr', vkGetInstanceProcAddrLUNARG),
]

VkDirectDriverLoadingInfoLUNARG._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pfnGetInstanceProcAddr': vkGetInstanceProcAddrLUNARG,
}
