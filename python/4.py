import os
from datetime import datetime

class PythonCodeGenerator:
    def __init__(self):
        self.templates = {
            'class': self._class_template,
            'function': self._function_template,
            'script': self._script_template,
            'flask_app': self._flask_template
        }
    
    def _class_template(self, class_name, attributes=None, methods=None):
        attributes = attributes or []
        methods = methods or []
        
        code = f"class {class_name}:\n"
        code += "    def __init__(self"
        
        # Добавляем атрибуты в конструктор
        for attr in attributes:
            code += f", {attr}=None"
        
        code += "):\n"
        
        # Инициализация атрибутов
        for attr in attributes:
            code += f"        self.{attr} = {attr}\n"
        
        code += "\n"
        
        # Добавляем методы
        for method in methods:
            code += f"    def {method}(self):\n"
            code += f"        # TODO: Implement {method}\n"
            code += f"        pass\n\n"
        
        return code
    
    def _function_template(self, func_name, parameters=None, return_type=None):
        parameters = parameters or []
        param_str = ", ".join(parameters)
        
        code = f"def {func_name}({param_str})"
        if return_type:
            code += f" -> {return_type}"
        code += ":\n"
        code += f"    \"\"\"\n"
        code += f"    Description of {func_name}\n"
        code += f"    \"\"\"\n"
        code += f"    # TODO: Implement function logic\n"
        code += f"    pass\n"
        
        return code
    
    def _script_template(self, script_name):
        code = f"#!/usr/bin/env python3\n"
        code += f"# -*- coding: utf-8 -*-\n"
        code += f"\"\"\"\n"
        code += f"{script_name}\n"
        code += f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        code += f"\"\"\"\n\n"
        code += f"import sys\n"
        code += f"import os\n\n"
        code += f"def main():\n"
        code += f"    # Main function\n"
        code += f"    print(\"Hello from {script_name}!\")\n\n"
        code += f"if __name__ == \"__main__\":\n"
        code += f"    main()\n"
        
        return code
    
    def _flask_template(self, app_name):
        code = f"from flask import Flask, render_template, request, jsonify\n\n"
        code += f"app = Flask(__name__)\n\n"
        code += f"@app.route('/')\n"
        code += f"def index():\n"
        code += f"    return render_template('index.html')\n\n"
        code += f"@app.route('/api/data', methods=['GET'])\n"
        code += f"def get_data():\n"
        code += f"    return jsonify({{'message': 'Hello from {app_name}!'}})\n\n"
        code += f"if __name__ == '__main__':\n"
        code += f"    app.run(debug=True)\n"
        
        return code
    
    def generate_code(self, code_type, **kwargs):
        if code_type in self.templates:
            return self.templates[code_type](**kwargs)
        else:
            raise ValueError(f"Unknown code type: {code_type}")
    
    def save_to_file(self, code, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Code saved to: {filename}")

# Пример использования
def main():
    generator = PythonCodeGenerator()
    
    # Генерация класса
    class_code = generator.generate_code(
        'class',
        class_name='Person',
        attributes=['name', 'age', 'email'],
        methods=['get_info', 'save_to_db', 'validate']
    )
    
    # Генерация функции
    func_code = generator.generate_code(
        'function',
        func_name='calculate_statistics',
        parameters=['data', 'method'],
        return_type='dict'
    )
    
    # Генерация скрипта
    script_code = generator.generate_code(
        'script',
        script_name='data_processor.py'
    )
    
    # Сохранение в файлы
    generator.save_to_file(class_code, 'person_class.py')
    generator.save_to_file(func_code, 'functions.py')
    generator.save_to_file(script_code, 'main_script.py')
    
    # Вывод сгенерированного кода
    print("=== Сгенерированный класс ===")
    print(class_code)
    print("\n=== Сгенерированная функция ===")
    print(func_code)

if __name__ == "__main__":
    main()