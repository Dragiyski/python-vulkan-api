import ctypes

class VkDeviceGroupRenderPassBeginInfo(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderPassBeginInfo',
        'VkRenderingInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'deviceMask': 'device_mask',
        'deviceRenderAreaCount': 'device_render_area_count',
        'pDeviceRenderAreas': 'device_render_areas',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkDeviceGroupRenderPassBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceMask', ctypes.c_uint32),
    ('deviceRenderAreaCount', ctypes.c_uint32),
    ('pDeviceRenderAreas', ctypes.POINTER(VkRect2D)),
]

VkDeviceGroupRenderPassBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceMask': ctypes.c_uint32,
    'deviceRenderAreaCount': ctypes.c_uint32,
    'pDeviceRenderAreas': ctypes.POINTER(VkRect2D),
}
