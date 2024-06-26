import ctypes

class VkClearValue(ctypes.Union):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkClearColorValue',
        'VkClearDepthStencilValue',
    }
    _included_in_ = {
        'VkClearAttachment',
        'VkRenderPassBeginInfo',
        'VkRenderingAttachmentInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'color': 'color',
        'depthStencil': 'depth_stencil',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkClearColorValue import VkClearColorValue
from .VkClearDepthStencilValue import VkClearDepthStencilValue

VkClearValue._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]

VkClearValue._type_ = {
    'color': VkClearColorValue,
    'depthStencil': VkClearDepthStencilValue,
}
