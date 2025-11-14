import os
import subprocess
import sys
from pathlib import Path
import shutil

project_dir = Path(os.getcwd())
venv_path = project_dir / "venv"

print("🚀 Создаём виртуальное окружение...")

# Создаём venv
subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)

# Определяем pip в виртуальном окружении
if os.name == "nt":
    pip_executable = venv_path / "Scripts" / "pip.exe"
    python_executable = venv_path / "Scripts" / "python.exe"
else:
    pip_executable = venv_path / "bin" / "pip"
    python_executable = venv_path / "bin" / "python"

# Обновляем pip (не критично, ошибки не останавливают)
try:
    subprocess.run([str(pip_executable), "install", "--upgrade", "pip"], check=True)
except subprocess.CalledProcessError:
    print("⚠️ Не удалось обновить pip, продолжаем установку зависимостей...")

# Устанавливаем зависимости в виртуальное окружение
print("📦 Устанавливаем зависимости в venv...")
subprocess.run([str(pip_executable), "install", "."], check=True)

# Создаём .env из .env.example
env_example = project_dir / ".env.example"
env_file = project_dir / ".env"
if env_example.exists() and not env_file.exists():
    shutil.copy(env_example, env_file)
    print("✅ .env создан из .env.example")

print("✅ Установка завершена!")
print(f"Чтобы активировать виртуальное окружение:")
if os.name == "nt":
    print(f"venv\\Scripts\\activate")
else:
    print(f"source venv/bin/activate")
print("После активации можно запускать проект командой: uvicorn app.main:app --reload")
