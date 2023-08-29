# Тестовое задание от стартапа на вакансию "Python-разработчик".(Выполнено)
(Срок 1 неделя)

1. **Project Setup and Version Control:**
   - Create a new Django project and set up a virtual environment.
   - Initialize a Git repository for version control.

2. **API Design and Implementation:**
   - Design RESTful API endpoints for user registration, login, fetching user profile, updating user profile, and deleting the account using Django Rest Framework (DRF).
   - Implement the endpoints with appropriate view functions and serializers.

3. **Secure Password Hashing and Storage:**
   - Implement secure password hashing and storage using a Django hashing algorithm (e.g., Argon).
   - Ensure that plain passwords are not stored in the database.


4. **Validation, Error Handling, and Documentation:**
   - Apply appropriate validation and error handling techniques for API endpoints.
   - Document the API endpoints, request/response formats, and error handling.

5. **Custom User Model and Authentication:**
   - Create a custom user model that includes email as the unique identifier.
   - Implement email-based authentication and authorization mechanisms for protecting API routes.


6. **Message Queue with Celery:**
   - Integrate Celery for sending OTP to users during login.
   - Send 6-digit OTP codes to users' emails and verify them for login. Implement OTP expiration.

7. **Database and Deployment:**
   - Choose a database of your choice (e.g., PostgreSQL).
   - Set up database models for storing user profiles and other relevant data.
   - Document how to set up and deploy the backend application.

## Используемые технологии:
- Python
- Django
- Django Rest Framework
- Celery
- RabbitMQ
- Swagger
- PostgreSQL

## Запуск
1) Клонировать проект
2) Установить все пакеты из файла requirements.txt
3) Запустить Docker
4) Скачать в Docker образ: docker pull rabbitmq
5) Запустить RabbitMQ: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
6) Запустить работника Celery: celery -A app worker -l info -P gevent  
7) Для удобства отслеживания статуса сообщений: celery -A app flower 