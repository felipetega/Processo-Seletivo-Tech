from django.db import models
class Tecido(models.Model):

  choices_tipo = (
  ('LINHO', 'Linho'),
  ('CAMURÇA', 'Camurça'),
  ('MESCLA', 'Mescla'),
  ('MOLETOM', 'Moletom'),
  )

  choices_cores=(
  ('AZUL', 'Azul'),
  ('AMARELO', 'Amarelo'),
  ('VERMELHO', 'Vermelho'),
  ('VERDE', 'Verde'),
  )

  tipo = models.CharField(max_length=50, choices=choices_tipo)
  cor = models.CharField(max_length=50, choices=choices_cores)
  metros = models.IntegerField()