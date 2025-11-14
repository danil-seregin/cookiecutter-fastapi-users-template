import os
import subprocess
import sys
from pathlib import Path
import shutil

project_dir = Path(os.getcwd())

print("🚀 Настройка виртуального окружения и установка зависимостей...")

# 1. Создаём виртуальное окружение
venv_path = project_dir / "venv"
subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)

# 2. Путь до pip в виртуальном окружении
if os.name == "nt":
    pip_executable = venv_path / "Scripts" / "pip"
else:
    pip_executable = venv_path / "bin" / "pip"

# 3. Обновляем pip
subprocess.run([str(pip_executable), "install", "--upgrade", "pip"], check=True)

# 4. Устанавливаем зависимости через pyproject.toml
subprocess.run([str(pip_executable), "install", "."], check=True)

# 5. Копируем .env.example → .env, если есть
env_example = project_dir / ".env.example"
env_file = project_dir / ".env"
if env_example.exists() and not env_file.exists():
    shutil.copy(env_example, env_file)
    print("✅ .env создан из .env.example")

print("✅ Всё установлено! Виртуальное окружение готово.")
print(f"Чтобы активировать: source venv/bin/activate (Linux/macOS) или venv\\Scripts\\activate (Windows)")
