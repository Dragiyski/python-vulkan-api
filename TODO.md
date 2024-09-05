# Registry:

The purpose of the registry is to download the vk.xml and video.xml files upon installation. All other work will be on runtime (no code generation).

# Vulkan

## Loader

The loader module will contain LibraryLoader, InstanceLoader, and DeviceLoader.

LibraryLoader will contain CDLL/WinDLL instance.

InstanceLoader will contain the LibraryLoader instance and a handle of type VkInstance.

DevideLoader will contain the InstanceLoader instance and a handle of type VkDevice.

All of this will have dynamic attributes, which will do the following:

1. For all types of data, they will get an attribute from VulkanBinding, which can be VulkanXMLBinding or other bindings. The binding can return:
  * A simple value: for when it process constant, an object macro, or enum value
  * An IntEnum: for when it refers to &lt;enums&gt; tag.
  * A callable: for when it refers to a vulkan command.
  * A callable wrapper: from when it refers to a callback.
  * A structure/union class: for when it refers to structure/union type.
  
  The data for the node (if not cached) will be processed upon request, which can result in processing other nodes. For example `vkCreateInstance` command will process `VkInstanceCreateInfo` which is a type, `VkAllocationCallbacks` which is a type. The latter will process some callback functions.

  The binding can be interchangeable, with `VulkanXMLBinding` can bind everything directly to `ctypes`. `VulkanApiBinding` can be a binding that takes `VulkanBinding` to construct and can apply modifications to regular binding. For example, `vkEnumerateInstanceLayerProperties` that takes pointer to return structure and return `VkResult` can be restructured to throw exception on error and return a newly created `VkLayerProperties`, which itself can be restructured to be `list` instead of accpting and returning array length.

  Note: To achieve that `vkEnumerateInstanceLayerProperties` properties may return a python function instead of c binding, and that function might generate an independent class `VkLayerProperties` that is not a `ctypes.Structure`, but it contain a private property to the `ctypes.Structure`. Thus `vkEnumerateInstanceLayerProperties` from `VulkanApiBinding` can actually call into `VulkanXMLBinding` (potentially multiple times - one for length and one for the array).

2. If the request item is a command, after processing the command type, a call to `vkGetInstanceProcAddr` or `vkGetDeviceProcAddr` (for `DeviceLoader` only) must be called to retrieve a pointer to the actual command. If not `NULL` pointer returned, the command exists and the returned pointer must be wrapped by the binding.

## Documentation

Documentation must be stored in the classes `__annotations__`. Do note that `__annotations__` is a `dict` on functions. While classes do not have `__annotations__` as they do not have arguments (`__init__` and `__new__` functions does have, but the classes themselves don't), dynamic functions can be classes implementing `__call__`, allowing instances of the class to behave like function.

## XML processing

Everything named in the XML must be aggregated into `dict[str, set[Node]]`. In most cases there will be only one `Node`, but not all cases. In case of more than one node, the node path (examining ancestors) must be used to determine the node's role. For example `features / feature / enum` node associated with enum and `enums / enum` on the same name, the latter takes preferences.
