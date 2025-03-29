import ast
import argparse


class FileParser:
    """
    Parses file to AST
    """
    def __init__(self, filename):
        self.filename = filename
        self.tree = None

    def parse_file(self):
        """
        Parses file makes AST
        """
        with open(self.filename, 'r') as file:
            file_content = file.read()
            self.tree = ast.parse(file_content)

class StyleChecker:
    """
    Analyzes for style checking, imports, classes, functions,
    docstrings, annotations and naming
    """
    def __init__(self, tree):
        self.tree = tree
        self.classes = []
        self.functions = []
        self.imports = []
        self.type_annotation_errors = []
        self.naming_violations = {"classes": [], "functions": []}
        self.docstrings = {"classes": {}, "functions": {}}

    def check_imports(self):
        """
        Takes all imports
        """
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                self.imports.append(node)

    def check_classes_and_functions(self):
        """
        Generates all classes and functions
        """
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                self.classes.append(node)
            elif isinstance(node, ast.FunctionDef):
                self.functions.append(node)

    def check_type_annotations(self):
        """
        Sees if all functions and methods have types
        """
        for func in self.functions:
            if func.returns is None: 
                self.type_annotation_errors.append(f"{func.name} does not have type")
            for arg in func.args.args:
                if arg.annotation is None:
                    self.type_annotation_errors.append(f"{func.name} has argument {arg.arg} without type")

    def check_naming_conventions(self):
        """
        Makes sure all classes and functions follow naming
      
        """
        for cls in self.classes:
            if not cls.name[0].isupper():
                self.naming_violations["classes"].append(cls.name)

        for func in self.functions:
            if not func.name.islower() or "_" not in func.name:
                self.naming_violations["functions"].append(func.name)

    def check_docstrings(self):
        """
        Uses docstrings for classes and functions
        """
        for cls in self.classes:
            self.docstrings["classes"][cls.name] = ast.get_docstring(cls) or "DocString not found"

        for func in self.functions:
            self.docstrings["functions"][func.name] = ast.get_docstring(func) or "DocString not found"


class ReportGenerator:
    """
    Creates style report into txt file
    """
    def __init__(self, filename, style_checker):
        self.filename = filename
        self.style_checker = style_checker

    def generate_report(self):
        
        report_filename = f"style_report_{self.filename.split('/')[-1].replace('.py', '')}.txt"

        with open(report_filename, 'w') as report:
            report.write(f"File structure for {self.filename}\n")
            report.write("="*40 + "\n")
            report.write(f"Total lines: {len(open(self.filename).readlines())}\n")
            report.write("\nImports:\n")
            for imp in self.style_checker.imports:
                report.write(f"  - {ast.dump(imp)}\n")

            report.write("\nClasses:\n")
            for cls in self.style_checker.classes:
                report.write(f"  - {cls.name}\n")

            report.write("\nFunctions:\n")
            for func in self.style_checker.functions:
                report.write(f"  - {func.name}\n")

            report.write("\nDocstrings:\n")
            for cls, doc in self.style_checker.docstrings["classes"].items():
                report.write(f"{cls}: {doc}\n")
            for func, doc in self.style_checker.docstrings["functions"].items():
                report.write(f"{func}: {doc}\n")

            report.write("\nType errors:\n")
            if self.style_checker.type_annotation_errors:
                for error in self.style_checker.type_annotation_errors:
                    report.write(f"  - {error}\n")
            else:
                report.write("  - Functions and methods have types\n")

            report.write("\nNaming errors:\n")
            if self.style_checker.naming_violations["classes"]:
                report.write(f"  - Classes: {', '.join(self.style_checker.naming_violations['classes'])}\n")
            if self.style_checker.naming_violations["functions"]:
                report.write(f"  - Functions: {', '.join(self.style_checker.naming_violations['functions'])}\n")
            if not self.style_checker.naming_violations["classes"] and not self.style_checker.naming_violations["functions"]:
                report.write("  - Names meet naming practices\n")


def main(filename):
    """
    Parses file, checks style, makes report
    """
    parser = FileParser(filename)
    parser.parse_file()

    checker = StyleChecker(parser.tree)
    checker.check_imports()
    checker.check_classes_and_functions()
    checker.check_type_annotations()
    checker.check_naming_conventions()
    checker.check_docstrings()

    report_generator = ReportGenerator(filename, checker)
    report_generator.generate_report()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check file')
    parser.add_argument('filename', type=str, help='file to check')

    args = parser.parse_args()
    main(args.filename)


