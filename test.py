#!/usr/bin/env python3

from bamboo import dcfile, module

astron_keywords = ['clsend', 'ownsend', 'clrecv', 'ownrecv',
                   'airecv', 'broadcast', 'ram', 'required', 'db']

mod = module.Module()
for word in astron_keywords:
    mod.add_keyword(word)
dcfile.parse_dcfile(mod, 'sample.dc')

print() # Newline after prompt

# Inspect module classes
print('Classes')
for class_num in range(0, mod.num_classes()):
    cls = mod.get_class(class_num)
    print('  ' + cls.name())
    for field_num in range(0, cls.num_fields()):
        field = cls.get_field(field_num)
        print(field.name())
    #    print('    ' + field.name() + ' : ' + field.type().to_string())
    #    print_type(field.type(), 3)
