from django.db import migrations


def seed_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    posts = [
        {'title': 'Что такое Django и с чего начать',
         'short': 'Краткий обзор фреймворка Django и шагов первой установки на локальной машине.',
         'body': 'Django — это высокоуровневый Python-фреймворк для веб-разработки, который позволяет быстро создавать безопасные и масштабируемые сайты. В этой статье мы рассмотрим архитектуру MTV, установку и создание первого проекта.'},
        {'title': 'Виртуальное окружение и зависимости',
         'short': 'Зачем нужно виртуальное окружение и как правильно сохранять зависимости в requirements.txt.',
         'body': 'Для каждого Django-проекта рекомендуется создавать отдельное виртуальное окружение, чтобы не смешивать библиотеки разных проектов. С помощью pip freeze удобно сохранять зафиксированные версии пакетов в файл requirements.txt.'},
        {'title': 'Маршруты и представления в Django',
         'short': 'Как работают URL-конфиги и функции-представления, отдающие HTML-шаблоны браузеру.',
         'body': 'В Django запрос пользователя сначала попадает в urls.py, где по маске пути выбирается соответствующая функция-представление из views.py. Представление обрабатывает данные и возвращает ответ, чаще всего это отрисованный HTML-шаблон.'},
    ]
    for p in posts:
        Post.objects.create(**p)


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_posts, migrations.RunPython.noop),
    ]
