from django.db import models


class Profession(models.Model):
    title = models.CharField('Навзвание', max_length=100)
    desc = models.TextField('Описание')
    img = models.ImageField('Изображение', upload_to='profession_img/', blank=True, null=True)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title


class Importance(models.Model):
    class Meta:
        verbose_name = 'Страница востребованность'
        verbose_name_plural = 'Страница востребованность'

    def __str__(self):
        return 'Страница востребованность'


class Geography(models.Model):
    class Meta:
        verbose_name = 'Страница география'
        verbose_name_plural = 'Страница география'

    def __str__(self):
        return 'Страница география'


class Skill(models.Model):
    class Meta:
        verbose_name = 'Страница навыки'
        verbose_name_plural = 'Страница навыки'

    def __str__(self):
        return 'Страница навыки'


class Item(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    csv_file = models.FileField('Csv файл', upload_to='csv/')
    image_file = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)

    importance_id = models.ForeignKey(Importance, models.DO_NOTHING, related_name='importance_id', null=True)
    geography_id = models.ForeignKey(Geography, models.DO_NOTHING, related_name='geography_id', null=True)
    skill_id = models.ForeignKey(Skill, models.DO_NOTHING, related_name='skill_id', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
