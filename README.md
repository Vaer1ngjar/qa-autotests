# QA Autotests

Автотесты из лабораторных работ по дисциплине «Тестирование программного обеспечения».

## Состав

| Папка | Что тестируется | Лабораторная |
|-------|-----------------|--------------|
| `tests/unit` | Модульные тесты класса `Calculator` (`src/calculator.py`) | ЛР 6 |
| `tests/api`  | Тесты REST API https://jsonplaceholder.typicode.com | ЛР 5 |

## Локальный запуск

```bash
pip install -r requirements.txt
pytest
```

## CI

Workflow `.github/workflows/run-tests.yml` запускается при каждом push и pull request в ветку `main`:
поднимает Ubuntu, ставит Python (3.12 и 3.13), устанавливает зависимости и запускает `pytest`.
