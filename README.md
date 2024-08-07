Article Flow
============

Необходимо реализовать веб сервис с помощью Django и захостить на сервере (на каком удобно, например, heroku). В
качестве СУБД рекомендуется использование PostgreSQL, но допускается SQLite. Готовым ответом будет являться url
развернутого приложения и ссылка на публичный git репозиторий. Необходимо выгрузить перечень используемых сторонних
библиотек в файл requirements.txt и сохранить его в папке с проектом. Сервис должен предоставлять RESTful API,
позволяющий формировать ленту статей для пользователей. API должно предоставлять ресурсы для:

1. вывода публичных статей для неавторизованных пользователей;
2. авторизации пользователей с помощью Basic Auth. В качестве логина использовать email;
3. регистрации новых пользователей с ролью "подписчик"
   a) обязательные поля email, пароль;
   b) должна быть валидация email на соответствие маски email и на уникальность;
   c) пароль должен быть не короче 8 символов и содержать хотя бы одну цифру и букву любого регистра);
4. чтения статей закрытых статей (только для подписчиков) пользователями с ролью "подписчик";
5. создания новых статей ролью "автор". Пользователям с ролью "подписчик" запрещено создание статей;
6. редактирования и удаления статей. Автор может удалять или редактировать только те статьи которые он написал