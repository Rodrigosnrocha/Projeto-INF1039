from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Tabela de lugares
class Lugar(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    thumb = models.ImageField(default='default.png',blank=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    
    tags = TaggableManager()                                    # Para criar tags no API de lugar tem que criar em forma de lista e.g ["Estudar","Comer"]

    def __str__(self):
        return self.titulo

    # Funcoes para pegar likes e dislikes e mostrar na API de cada lugar
    def likes_count(self):
        return self.likes.filter(voto=1).count()

    def dislikes_count(self):
        return self.likes.filter(voto=-1).count()


class Avaliacao(models.Model):
    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avaliacao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.avaliacao

# Tabela de likes de lugar
class Like(models.Model):
    TIPO_LIKE = (
        (1,"Like"),
        (0,"Neutro"),
        (-1,"Dislike")
    )

    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE, related_name='likes')       # Usa related_name para filtrar por likes no modelo de lugar (likes_count, dislikes_count)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    voto = models.IntegerField(default=0,choices=TIPO_LIKE)

    # Um usuario so pode deixar um voto por lugar
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','lugar_id'],name='unique_user')]

    def __str__(self):
        return self.user.username + ' - ' + self.lugar.titulo