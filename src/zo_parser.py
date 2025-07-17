# src/zo_parser.py

def parse_zo_code(code):
    lines = code.strip().split('\n')
    ast = []
    for line in lines:
        line = line.strip()
        if line.startswith("define function"):
            parts = line.replace("define function", "").strip().split("that takes")
            name = parts[0].strip()
            args = [arg.strip() for arg in parts[1].split("and")] if len(parts) > 1 else []
            ast.append({"type": "function", "name": name, "args": args, "body": []})
        elif line.startswith("print"):
            msg = line.replace("print", "").strip().strip('"')
            ast[-1]["body"].append({"type": "print", "value": msg})
        elif line.startswith("set"):
            _, var, _, value = line.split(" ", 3)
            ast[-1]["body"].append({"type": "assign", "var": var, "value": value})
        elif line == "end":
            continue  # just marks function end
        else:
            pass  # support more later
    return ast
