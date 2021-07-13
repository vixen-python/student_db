from django import template
from student.enums import Sex


register = template.Library()


@register.filter
def sex_enum(value: int) -> str:
    return Sex(value).name
