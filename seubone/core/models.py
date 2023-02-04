from django.db import models

TIPOS_TECIDO = (
  ('LINHO', 'Linho'),
  ('CAMURÇA', 'Camurça'),
  ('MESCLA', 'Mescla'),
  ('MOLETOM', 'Moletom'),
  )

CORES=(
  ('AZUL', 'Azul'),
  ('AMARELO', 'Amarelo'),
  ('VERMELHO', 'Vermelho'),
  ('VERDE', 'Verde'),
  )


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

  def __str__(self):
    return f'{self.tipo} - {self.cor} - {self.metros} metro(s)'
