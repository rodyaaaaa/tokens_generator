# Backend Secret Key Generator

A modular, lightweight, and cryptographically secure utility written in Python to generate secret keys, tokens, and passwords for backend applications.

## Overview

This project provides an easy-to-use Command Line Interface (CLI) and importable modules to generate secure keys. It is built to serve common backend requirements such as Session Secrets (e.g. Django/Flask `SECRET_KEY`), JWT HMAC keys, API tokens with custom prefixes, and random database passwords.

### Key Features
- **Security:** Built using Python's standard `secrets` module for cryptographically strong random values.
- **Flexibility:** Supports Hexadecimal, URL-safe Base64, and Alphanumeric formats.
- **Customization:** Customize token length, add custom prefixes, and output formatting.
- **Integration Ready:** Direct output formatting for `.env` files.
- **Modular & Tested:** Completely split into single-responsibility modules with unit test coverage.

### Quick Links
- Detailed Documentation: [docs/README.md](docs/README.md)
- Programmatic Examples: [docs/examples.py](docs/examples.py)
- Test Suite: [tests/](tests/)

> [!NOTE]
> This application was written with the assistance of Artificial Intelligence (AI).

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Генератор секретних ключів для бекенду

Модульна, легковагова та криптографічно безпечна утиліта на Python для генерації секретних ключів, токенів та паролів для бекенд-додатків.

## Огляд

Цей проєкт надає простий у використанні інтерфейс командного рядка (CLI) та модулі для імпорту для генерації безпечних ключів. Він розроблений для задоволення типових потреб бекенду, таких як секрети сесій (наприклад, Django/Flask `SECRET_KEY`), ключі JWT HMAC, API-токени з префіксами та випадкові паролі баз даних.

### Основні можливості
- **Безпека:** Створено з використанням стандартного модуля `secrets` у Python для криптографічно стійких випадкових значень.
- **Гнучкість:** Підтримує шістнадцятковий (Hex), URL-safe Base64 та буквено-цифровий (Alphanumeric) формати.
- **Кастомізація:** Налаштування довжини токенів, додавання власних префіксів та форматування виводу.
- **Готовність до інтеграції:** Пряме форматування результату для `.env` файлів.
- **Модульність та тестування:** Повністю розділений на модулі з єдиною відповідальністю та покритий юніт-тестами.

### Корисні посилання
- Детальна документація: [docs/README.md](docs/README.md)
- Приклади використання в коді: [docs/examples.py](docs/examples.py)
- Набір тестів: [tests/](tests/)

> [!NOTE]
> Цей застосунок було створено за допомогою штучного інтелекту (ШІ).

### Ліцензія
Цей проєкт ліцензовано за ліцензією MIT - детальніше див. у файлі [LICENSE](LICENSE).


