# src/zo_compiler.py

def compile_to_python(ast):
    output = ""
    for node in ast:
        if node["type"] == "function":
            args = ", ".join(node["args"])
            output += f"def {node['name']}({args}):\n"
            for stmt in node["body"]:
                if stmt["type"] == "print":
                    output += f"    print(\"{stmt['value']}\")\n"
                elif stmt["type"] == "assign":
                    output += f"    {stmt['var']} = {stmt['value']}\n"
            output += "\n"
    return output
