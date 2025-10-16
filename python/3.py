import os
import subprocess
from datetime import datetime

# Путь к вашему репозиторию
repo_path = r"C:\Users\iscan\иск\Рабочий стол\Ханов Искандер\small_progect"

# Сообщение коммита с текущей датой
commit_message = f"Ежедневный коммит: {datetime.now().strftime('%Y-%m-%d')}"

# Выполняем команды git
def run_git_commands():
    os.chdir(repo_path)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

if __name__ == "__main__":
    try:
        run_git_commands()
        print("Коммит выполнен успешно.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении git команд: {e}")