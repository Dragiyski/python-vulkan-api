import ctypes
from .._ctypes import implementation_map as complex_type_map, CPointerType
from .._util import make_python_name
from .property import sparse_array_length_property, array_length_property, field_access


def compile_property_map(descriptor, base_class):
    field_to_property_name = { field_name: make_python_name(field_name, p = True, s = True) for field_name in descriptor._member_info_ }
    duplicate_properties = set()
    duplicate_properties_detection = {}
    length_map = {}
    # First, collect property names and detect duplicates, also organize fields with length into a length_map.
    for member_name in descriptor._member_list_:
        member_info = descriptor._member_info_[member_name]
        property_name = field_to_property_name[member_name]
        if property_name not in duplicate_properties_detection:
            duplicate_properties_detection[property_name] = member_name
        else:
            duplicate_properties.add(property_name)
        if 'length' in member_info:
            if property_name not in length_map:
                length_map[property_name] = {}
            if len(member_info['length']) == 1 or len(member_info['length']) == 2 and member_info['length'][1] == 1:
                length_map[property_name][member_name] = member_info['length']
    del duplicate_properties_detection
    # Next collect information from the length map, this can contain:
    # Contiguous/Sparse pairs: In rare cases Vulkan API provide identical and mutually exclusive fields for contiguous and sparse list of properties.
    # An example of this is `VkAccelerationStructureBuildGeometryInfoKHR`, where:
    # `geometryCount` is the length of:
    # `pGeometries` - pointer to the start of array of geometries, defined in XML as `len="geometryCount"`
    # `ppGeometries` - pointer to start of array of pointer to geometries, defined in XML as `len="geometryCount,1"`
    # The spec is clear that in this case, only one of `pGeometries` or `ppGeometries` must be specified, the other must be `nullptr`.
    # In python, we need only one property to handle this, as it will depend of the value:
    # list -> ppGeometries
    # ctypes.Array -> pGeometries
    # Remove both field from duplicates.
    property_map = {}
    for property_name, field_length_map in length_map.items():
        match len(field_length_map):
            case 2:
                contiguous_field_name = None
                sparse_field_name = None
                for field_name, length_desc in field_length_map.items():
                    match len(length_desc):
                        case 1:
                            contiguous_field_name = field_name
                        case 2:
                            sparse_field_name = field_name
                        case _:
                            raise RuntimeError(f'In property {descriptor._name_}.{property_name}: Unexpected value for length_desc: {length_desc!r}')
                if contiguous_field_name is None or sparse_field_name is None:
                    raise RuntimeError(f'In property {descriptor._name_}.{property_name}: Missing field name in contiguous/sparse pair for property.')
                if tuple(field_length_map[contiguous_field_name][0]) != tuple(field_length_map[sparse_field_name][0]):
                    raise RuntimeError(f'In property {descriptor._name_}.{property_name}: Different length field reference: {contiguous_field_name} = {tuple(field_length_map[contiguous_field_name][0])!r}; {sparse_field_name} = {tuple(field_length_map[sparse_field_name][0])}')
                if not isinstance(descriptor._member_info_[contiguous_field_name]['type'], CPointerType) or descriptor._member_info_[contiguous_field_name]['type'].pointer() is not descriptor._member_info_[sparse_field_name]['type']:
                    raise RuntimeError(f'In property {descriptor._name_}.{property_name}: Invalid type relationship between fields {contiguous_field_name!r} and {sparse_field_name!r}')
                if len(field_length_map[contiguous_field_name][0]) != 1:
                    raise RuntimeError(f'In property {descriptor._name_}.{property_name}: Complex types do not support length in another complex field')
                property_map[property_name] = sparse_array_length_property(
                    descriptor._member_info_[contiguous_field_name]['type'].type,
                    property_name,
                    contiguous_field_name,
                    sparse_field_name,
                    *field_access(field_length_map[contiguous_field_name[0][0]])
                )
        if len(field_length_map) == 2:
            contiguous_field_name = None
            sparse_field_name = None
            for field_name, length_desc in field_length_map.items():
                match len(length_desc):
                    case 1:
                        contiguous_field_name = field_name
                    case 2:
                        sparse_field_name = field_name
            if contiguous_field_name is None or sparse_field_name is None:
                continue
            if tuple(field_length_map[contiguous_field_name][0]) != tuple(field_length_map[sparse_field_name][0]):
                continue
            if not isinstance(descriptor._member_info_[contiguous_field_name]['type'], CPointerType) or descriptor._member_info_[contiguous_field_name]['type'].pointer() is not descriptor._member_info_[sparse_field_name]['type']:
                continue
            property_map[property_name] = {
                'priority': -20,
                'get': make_sparse_c_array_getter(descriptor, base_class, property_name, field_length_map[sparse_field_name][0], contiguous_field_name, sparse_field_name, extension),
                'set': make_sparse_c_array_setter(descriptor, base_class, property_name, field_length_map[sparse_field_name][0], contiguous_field_name, sparse_field_name, extension)
            }
            if len(length_desc[0]) == 1:
                hide_fields.add(length_desc[0][0])
            duplicate_properties.discard(property_name)
        elif len(field_length_map) == 1:
            field_name, length_desc = next(iter(field_length_map.items()))
            if not isinstance(descriptor._member_info_[field_name]['type'], CPointerType):
                continue
            property_map[property_name] = {
                'priority': -20,
                'get': make_c_array_getter(descriptor, base_class, property_name, length_desc[0], field_name, extension),
                'set': make_c_array_setter(descriptor, base_class, property_name, length_desc[0], field_name, extension)
            }
            if len(length_desc[0]) == 1:
                hide_fields.add(length_desc[0][0])
            duplicate_properties.discard(property_name)
    

def compile_complex(descriptor):
    base_class = {'structure': ctypes.Structure, 'union': ctypes.Union}[descriptor._category_]
    property_map = compile_property_map(descriptor, base_class)