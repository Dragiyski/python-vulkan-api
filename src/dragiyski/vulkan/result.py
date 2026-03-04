from .binding._generated._vulkan_enum.VkResult import VkResult as _VkResult
from .binding._generated._vulkan_database import vendor_suffix as _vendor_suffix


class VkException(Exception):
    is_error = False

    @staticmethod
    def from_result(result: int | _VkResult, /, *args, **kwargs) -> 'VkException':
        if not isinstance(result, _VkResult):
            result = _VkResult(result)
        if result == _VkResult.VK_SUCCESS:
            return None
        return _result_exception_map[result.value](*args, **kwargs)


class VkError(VkException):
    is_error = True


def _generate_class_name(name: str) -> str:
    parts = name.split('_')
    return ''.join(part.capitalize() if part not in _vendor_suffix else part.upper() for part in parts)


_result_exception_map = {}


def __init__():
    for result in _VkResult:
        if result.value == 0:
            continue
        name = _generate_class_name(result.name)
        if result.value not in _result_exception_map:
            base_class = VkError if result.value < 0 else VkException
            _result_exception_map[result.value] = type(name, (base_class,), {'enum': result})
        globals()[name] = _result_exception_map[result.value]
    for alias_name in type.__dir__(_VkResult):
        if not alias_name.startswith('VK_'):
            continue
        enum = getattr(_VkResult, alias_name)
        if alias_name == enum.name:
            continue
        if enum.value in _result_exception_map:
            name = _generate_class_name(alias_name)
            globals()[name] = _result_exception_map[enum.value]


__init__()
