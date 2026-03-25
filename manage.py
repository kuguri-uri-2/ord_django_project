import os
import sys
from typing import List, Optional

class DjangoManager:
    """
    Менеджер для управления Django командами
    """
    
    def __init__(self, settings_module: str = 'ord.settings'):
        self.settings_module = settings_module
        self._configure_environment()
    
    def _configure_environment(self) -> None:
        """Конфигурация переменных окружения"""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)
    
    @staticmethod
    def _get_command_executor():
        """Получение исполнителя команд Django"""
        try:
            from django.core.management import execute_from_command_line
            return execute_from_command_line
        except ModuleNotFoundError as e:
            raise self._create_import_error(e)
    
    @staticmethod
    def _create_import_error(original_error: Exception) -> ImportError:
        """Создание информативной ошибки импорта"""
        return ImportError(
            "Django не найден. Проверьте установку.\n"
            f"Детали: {original_error}"
        )
    
    def execute(self, arguments: Optional[List[str]] = None) -> None:
        """Выполнение команды Django"""
        if arguments is None:
            arguments = sys.argv
        
        executor = self._get_command_executor()
        executor(arguments)

if __name__ == '__main__':
    manager = DjangoManager()
    manager.execute()