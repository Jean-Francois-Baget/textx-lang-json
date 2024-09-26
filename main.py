from textx import metamodel_for_language


parser = metamodel_for_language('textxjson')


from textx.export import metamodel_export

metamodel_export(parser, 'json.dot')