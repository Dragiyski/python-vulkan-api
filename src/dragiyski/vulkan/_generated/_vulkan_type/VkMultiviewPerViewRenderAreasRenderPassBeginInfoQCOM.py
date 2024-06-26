import ctypes

class VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM(ctypes.Structure):
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
        'perViewRenderAreaCount': 'per_view_render_area_count',
        'pPerViewRenderAreas': 'per_view_render_areas',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_multiview_per_view_render_areas',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_RENDER_AREAS_RENDER_PASS_BEGIN_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_RENDER_AREAS_RENDER_PASS_BEGIN_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('perViewRenderAreaCount', ctypes.c_uint32),
    ('pPerViewRenderAreas', ctypes.POINTER(VkRect2D)),
]

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'perViewRenderAreaCount': ctypes.c_uint32,
    'pPerViewRenderAreas': ctypes.POINTER(VkRect2D),
}
