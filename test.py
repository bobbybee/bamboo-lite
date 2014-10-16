#!/usr/bin/env python3

from bamboo import dcfile, module

astron_keywords = ['clsend', 'ownsend', 'clrecv', 'ownrecv',
                   'airecv', 'broadcast', 'ram', 'required', 'db']

mod = module.Module()
for word in astron_keywords:
    mod.add_keyword(word)
dcfile.parse_dcfile(mod, 'sample.dc')

# Helper functions for printing complex types
def print_type(typ, indent):
    tab = '  ' * indent
    subtype = typ.subtype()
    if subtype == module.kTypeMethod:
        method = typ.as_method()
        for param_num in range(0, method.num_parameters()):
            param = method.get_parameter(param_num)
            if not param.name():
                print(tab + param.type().to_string())
            else:
                print(tab + param.name() + ' : ' + param.type().to_string())
            print_type(param.type(), indent + 1)

    elif subtype == module.kTypeStruct:
        struct = typ.as_struct()
        for field_num in range(0, struct.num_fields()):
            field = struct.get_field(field_num)
            if not field.name():
                print(tab + field.type().to_string())
            else:
                print(tab + field.name() + ' : ' + field.type().to_string())
            print_type(field.type(), indent + 1)

# Inspect module classes
print('Classes')
for class_num in range(0, mod.num_classes()):
    cls = mod.get_class(class_num)
    print('  ' + cls.name())
    for field_num in range(0, cls.num_fields()):
        field = cls.get_field(field_num)
        print('    ' + field.name() + ' : ' + field.type().to_string())
        print_type(field.type(), 3)
