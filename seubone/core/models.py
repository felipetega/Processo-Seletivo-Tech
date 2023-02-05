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



  tipo = models.CharField(max_length=50, choices=TIPOS_TECIDO)
  cor = models.CharField(max_length=50, choices=CORES)
  metros = models.IntegerField()

  def __str__(self):
    return f'{self.tipo} - {self.cor} - {self.metros} metro(s)'
