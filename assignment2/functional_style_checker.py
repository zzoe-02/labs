import ast
import os
import sys
from typing import List, Dict, Union, Tuple

def read_file_content(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def parse_ast(source_code: str) -> ast.AST:
    return ast.parse(source_code)


def extract_imports(tree: ast.AST) -> List[Union[ast.Import, ast.ImportFrom]]:
    return [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]

def extract_classes(tree: ast.AST) -> List[ast.ClassDef]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
def extract_functions(tree: ast.AST) -> List[ast.FunctionDef]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
def extract_docstrings(classes: List[ast.ClassDef], functions: List[ast.FunctionDef]) -> Dict[str, Dict[str, str]]:
    class_docs = {cls.name: ast.get_docstring(cls) or f"{cls.name}: DocString not found" for cls in classes}
    function_docs = {func.name: ast.get_docstring(func) or f"{func.name}: DocString not found" for func in functions}
    return {'classes': class_docs, 'functions': function_docs}
def check_type_annotations(functions: List[ast.FunctionDef]) -> List[str]: 
    return list(filter(None, [
        f"{func.name} does not have type" if func.returns is None else None
        for func in functions
    ] + [
        f"{func.name} has argument {arg.arg} without type"
        for func in functions
        for arg in func.args.args if arg.annotation is None
    ]))
def check_naming_conventions(classes: List[ast.ClassDef], functions: List[ast.FunctionDef]) -> Dict[str, List[str]]:
    class_violations = [cls.name for cls in classes if not cls.name[0].isupper()]
    function_violations = [
        func.name for func in functions
        if not func.name.islower() or ("_" not in func.name and len(func.name) > 1)
    ]
    return {
        'classes': class_violations,
        'functions': function_violations 
    }

def _report(
    filepath: str,
    total_lines: int,
    imports: List[Union[ast.Import, ast.ImportFrom]],
    classes: List[ast.ClassDef],
    functions: List[ast.FunctionDef],
    docstrings: Dict[str, Dict[str, str]],
    type_errors: List[str],
    naming_violations: Dict[str, List[str]]
) -> None:
    filename = os.path.basename(filepath)
    report_path = f"style_report_{filename.replace('.py', '')}.txt"
    
    with open(report_path, 'w') as f:
        f.write(f"File for {filepath}\n")
        f.write("="*40 + "\n")
        f.write(f"total lines: {total_lines}\n\n")

        f.write("Imports:\n")
        f.writelines([f"  - {ast.dump(imp)}\n" for imp in imports])

        f.write("\nClasses:\n")
        f.writelines([f"  - {cls.name}\n" for cls in classes])

        f.write("\nFunctions:\n")
        f.writelines([f"  - {func.name}\n" for func in functions])

        f.write("\nDocstrings:\n")
        for cls, doc in docstrings["classes"].items():
            f.write(f"{cls}: {doc}\n\n")
        for func, doc in docstrings["functions"].items():
            f.write(f"{func}: {doc}\n\n")

        f.write("\nType errors:\n")
        if type_errors:
            f.writelines([f"  - {err}\n" for err in type_errors])
        else:
            f.write("  - All use type annotations\n")

        f.write("\nNaming errors:\n")
        if naming_violations["classes"]:
            f.write(f"  - Classes: {', '.join(naming_violations['classes'])}\n")
        if naming_violations["functions"]:
            f.write(f"  - Functions: {', '.join(naming_violations['functions'])}\n")
        if not naming_violations["classes"] and not naming_violations["functions"]:
            f.write("  - follows naming conventions\n")

def main() -> None:
    if len(sys.argv) < 2:
        print("enter file path")
        sys.exit(1)

    filepath = sys.argv[1]
    source_code = read_file_content(filepath)
    tree = parse_ast(source_code)

    imports = extract_imports(tree)
    classes = extract_classes(tree)
    functions = extract_functions(tree)
    docstrings = extract_docstrings(classes, functions)
    type_errors = check_type_annotations(functions)
    naming_violations = check_naming_conventions(classes, functions)
    total_lines = len(source_code.splitlines())

    _report(
        filepath,
        total_lines,
        imports,
        classes,
        functions,
        docstrings,
        type_errors,
        naming_violations
    )

if __name__ == "__main__":
    main()
