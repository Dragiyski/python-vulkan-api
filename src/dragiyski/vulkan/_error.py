from ._generated._vulkan_enum.VkResult import VkResult

class VkException(Exception):
    pass

class VkError(VkException):
    pass

class VkStatus(VkException):
    pass

def __init__():
    for enum in VkResult:
        Base = VkError if enum.value < 0 else VkStatus
        words = enum.name.split('_')
        class_name = []

_code_ = {}
__all__ = ['VkException', 'VkError', 'VkStatus']
__init__()