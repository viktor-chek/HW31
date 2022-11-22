from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def not_published(v):
    if v:
        raise ValidationError(f"Значение поля is_published при создании объявления не может быть True")


def birth_date(date):
    difference = relativedelta(date.today(), date).years

    if difference < 9:
        raise ValidationError(f"Для пользователей младше 9 лет регистрация запрещена")
