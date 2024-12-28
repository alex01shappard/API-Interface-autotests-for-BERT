# FastAPI и Gradio для BERT-модели бинарной классификации

![Alt text](intro.PNG)


Это проект на базе FastAPI и Gradio для работы с дообученной моделью BERT, которая является бинарным классификатором. Модель предназначена для определения, является ли промпт **jailbreak** (незаконным или несанкционированным запросом) или нет. Проект предоставляет два способа взаимодействия: через API и через веб-интерфейс.

## Описание проекта

Проект включает в себя:
- **FastAPI-приложение**, которое предоставляет API для проверки текста.
- **Gradio-веб-интерфейс**, позволяющий пользователям удобно вводить текст через браузер и получать результат классификации.
- Модель **BERT**, дообученную для задачи бинарной классификации промптов.

Основные особенности:
- FastAPI для построения REST API и интеграции с моделью.
- Gradio для быстрого и минималистичного веб-интерфейса.
- Swagger UI для тестирования API и отправки запросов через браузер.

### Файлы проекта

- **main.py**: Основной файл, который запускает сервер FastAPI. Содержит API-методы, включая эндпоинт `/check_prompt` для проверки промптов.
  
- **prompt_defender.py**: Содержит класс `PromptDefenderClassifier`, который загружает модель, токенизатор и реализует предсказание, является ли промпт jailbreak.

- **gradio_interface.py**: Отдельный файл для запуска веб-интерфейса Gradio. Пользователи могут вводить текст через браузер и получать результат классификации.

- **my_bert_model/**: Папка с весами модели и необходимыми файлами для работы модели BERT.

- **requirements.txt**: Список зависимостей для запуска проекта.

---

## Инструкция по использованию

### 1. Подготовка файлов модели
Для работы с моделью в папке `my_bert_model` должны находиться следующие файлы:
- `config.json`
- `model.safetensors`
- `special_tokens_map.json`
- `tokenizer_config.json`
- `vocab.txt`

Убедитесь, что все необходимые файлы загружены.

---

### 2. Установка зависимостей

Установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 3. Запуск FastAPI API

Для запуска сервера выполните следующую команду:

```bash
uvicorn main:app --reload
```
Документация Документация API автоматически генерируется и доступна по адресу:

Swagger UI: http://127.0.0.1:8000/docs

---

### 4. Запуск Gradio-веб-интерфейса

Для запуска веб-интерфейса выполните:

```bash
python gradio_interface.py
```
Веб-интерфейс будет доступен по адресу: http://localhost:7860.
Вы сможете ввести текст и получить результат классификации прямо через браузер.

---

### Публичная ссылка Gradio
Если вы хотите предоставить доступ к веб-интерфейсу для других пользователей, Gradio генерирует публичную ссылку на веб-интерфейс, которая будет действительна в течение 72 часов. Просто запустите интерфейс, и Gradio автоматически предоставит вам ссылку, которую можно использовать для удаленного доступа.