from django.db import models


class Post(models.Model):
    '''Данные о посте'''
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Контент поста')
    author = models.CharField('Автор', max_length=20)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        
    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
    
    
class Comments(models.Model):
    '''Коментарии к посту'''
    name = models.CharField('Ник', max_length=15)
    text_comment = models.TextField('Текст комментария', max_length=500)
    post = models.ForeignKey(Post, verbose_name='Публикации', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,  verbose_name='Время создания')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        
    def __str__(self) -> str:
        return f'{self.name}, {self.post}'
    
