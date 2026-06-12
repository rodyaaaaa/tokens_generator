# Backend Secret Key Generator Documentation / Документація генератора секретних ключів

This document is available in:
- [English](#english-documentation)
- [Українська](#українська-версія)

---

## English Documentation

A lightweight, modular, and cryptographically secure utility for generating backend secrets (e.g., Flask/Django `SECRET_KEY`, JWT keys, API tokens, database passwords).

### Features

- **Multiple Algorithms:** Generate keys using hexadecimal, URL-safe Base64, or alphanumeric charsets.
- **Custom Lengths:** Specify the exact character length of your keys.
- **Prefixing:** Prepend identifiers (e.g., `sk_prod_`) for modern API key patterns.
- **Dotenv Integration:** Directly format keys as key-value pairs suitable for `.env` files.
- **Batch Generation:** Generate multiple keys simultaneously.

---

### Command Line Interface (CLI) Usage

Run the program from your terminal using:

```bash
python main.py [options]
```

#### CLI Arguments Reference

| Option | Short Option | Default | Description |
| :--- | :--- | :--- | :--- |
| `--help` | `-h` | - | Show the help message and exit. |
| `--length` | `-l` | `32` | Key length in characters. |
| `--type` | `-t` | `hex` | Format type: `hex`, `base64`, `alphanumeric`. |
| `--prefix` | `-p` | `""` | A prefix string prepended to the generated key. |
| `--env` | `-e` | `None` | Output format as a `.env` entry with the specified variable name. |
| `--count` | `-c` | `1` | Number of keys to generate. |

#### CLI Examples

##### 1. Generate standard 32-character Flask secret
```bash
python main.py -t hex -l 32
# Output: a8f0a0c64c92...
```

##### 2. Generate a prefixed API Key
```bash
python main.py -t base64 -l 48 -p "sk_live_"
# Output: sk_live_Kj2F9d7s...
```

##### 3. Generate a `.env` entry for a DB password
```bash
python main.py -t alphanumeric -l 24 -e "DATABASE_PASSWORD"
# Output: DATABASE_PASSWORD=Hk9sF7d2...
```

##### 4. Generate standard 50-character Django SECRET_KEY for `.env` file
```bash
python main.py -t base64 -l 50 -e "SECRET_KEY"
# Output: SECRET_KEY=Q8oU1tojMX8D0BXRSKCHyx54Yb5lGe3zy2dFWzYZUMKg3MP-AJ
```

##### 5. Generate 5 Base64 tokens
```bash
python main.py -t base64 -l 16 -c 5
```

---

### Programmatic Usage

You can import generators and formatters directly into your Python scripts.

> [!NOTE]
> All generator functions rely on Python's built-in `secrets` module, which is suitable for cryptographically secure requirements (e.g. cryptography, passwords, tokens).

Refer to [examples.py](examples.py) for executable demonstrations. Below is a quick overview:

```python
from generators import generate_hex_key, generate_base64_key
from formatters import apply_prefix, format_dotenv

# 1. Generate a raw token
raw_token = generate_base64_key(48)

# 2. Add prefix
api_token = apply_prefix(raw_token, "pk_test_")

# 3. Format as dotenv entry
env_line = format_dotenv("STRIPE_API_KEY", api_token)

print(env_line)
# Output: STRIPE_API_KEY=pk_test_...
```

---

### Testing

The project uses Python's built-in `unittest` framework. To run all unit tests, execute the following command in the project root directory:

```bash
python -m unittest discover -s tests
```

---

## Українська версія

Легковагова, модульна та криптографічно безпечна утиліта для генерації секретів бекенду (наприклад, Flask/Django `SECRET_KEY`, ключів JWT, API-токенів, паролів баз даних).

### Можливості

- **Кілька алгоритмів:** Генерація ключів у шістнадцятковому (hex), безпечному для URL Base64 або буквено-цифровому (alphanumeric) форматах.
- **Власна довжина:** Вказуйте точну довжину ключів у символах.
- **Префікси:** Додавайте ідентифікатори на початку (наприклад, `sk_prod_`) для сучасних форматів API-ключів.
- **Інтеграція з Dotenv:** Пряме форматування результату як пари ключ-значення для файлів `.env`.
- **Генерація пачками:** Створення кількох ключів за один раз.

---

### Використання через Інтерфейс Командного Рядка (CLI)

Запустіть програму з вашого терміналу:

```bash
python main.py [параметри]
```

#### Опис параметрів CLI

| Параметр | Скорочення | За замовчуванням | Опис |
| :--- | :--- | :--- | :--- |
| `--help` | `-h` | - | Показати довідку та вийти. |
| `--length` | `-l` | `32` | Довжина ключа в символах. |
| `--type` | `-t` | `hex` | Тип формату: `hex`, `base64`, `alphanumeric`. |
| `--prefix` | `-p` | `""` | Префікс, що додається на початку ключа. |
| `--env` | `-e` | `None` | Форматувати вивід як запис `.env` із вказаною назвою змінної. |
| `--count` | `-c` | `1` | Кількість ключів для генерації. |

#### Приклади використання CLI

##### 1. Згенерувати стандартний 32-символьний секрет Flask
```bash
python main.py -t hex -l 32
# Результат: a8f0a0c64c92...
```

##### 2. Згенерувати API-ключ із префіксом
```bash
python main.py -t base64 -l 48 -p "sk_live_"
# Результат: sk_live_Kj2F9d7s...
```

##### 3. Створити рядок `.env` для пароля бази даних
```bash
python main.py -t alphanumeric -l 24 -e "DATABASE_PASSWORD"
# Результат: DATABASE_PASSWORD=Hk9sF7d2...
```

##### 4. Згенерувати стандартний 50-символьний Django SECRET_KEY для файлу `.env`
```bash
python main.py -t base64 -l 50 -e "SECRET_KEY"
# Результат: SECRET_KEY=Q8oU1tojMX8D0BXRSKCHyx54Yb5lGe3zy2dFWzYZUMKg3MP-AJ
```

##### 5. Згенерувати 5 токенів Base64
```bash
python main.py -t base64 -l 16 -c 5
```

---

### Використання у коді

Ви можете імпортувати генератори та форматувальники безпосередньо у власні скрипти Python.

> [!NOTE]
> Усі функції генерації покладаються на вбудований модуль `secrets` у Python, який підходить для криптографічно стійких вимог (наприклад, криптографія, паролі, токени).

Зверніться до файлу [examples.py](examples.py) для перегляду робочих прикладів. Нижче наведено короткий огляд:

```python
from generators import generate_hex_key, generate_base64_key
from formatters import apply_prefix, format_dotenv

# 1. Генеруємо сирий токен
raw_token = generate_base64_key(48)

# 2. Додаємо префікс
api_token = apply_prefix(raw_token, "pk_test_")

# 3. Форматуємо як рядок dotenv
env_line = format_dotenv("STRIPE_API_KEY", api_token)

print(env_line)
# Результат: STRIPE_API_KEY=pk_test_...
```

---

### Тестування

Проєкт використовує вбудовану в Python бібліотеку `unittest`. Щоб запустити всі тести, виконайте таку команду в кореневому каталозі проєкту:

```bash
python -m unittest discover -s tests
```
