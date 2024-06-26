import ctypes

class VkRenderPassStripeInfoARM(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = {
        'VkRenderPassStripeBeginInfoARM',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stripeArea': 'stripe_area',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ARM_render_pass_striped',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_INFO_ARM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_INFO_ARM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkRenderPassStripeInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeArea', VkRect2D),
]

VkRenderPassStripeInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stripeArea': VkRect2D,
}
