from ._generated.vulkan_error import VkException
from ._generated._vulkan_enum import VkResult

def status_check(code):
    if code == VkResult.VK_SUCCESS:
        return
    if code in VkException.from_code:
        raise VkException.from_code[code]
    raise VkException('Unrecognized error code: %d' % code, code=code)
