# game/models.py

from django.db import models

# Esta es la definición de tu tabla en la base de datos.
# Django la traducirá automáticamente a comandos SQL para PostgreSQL.
class Question(models.Model):
    """
    Representa una única pregunta en el juego "¿Quién Quiere Ser Millonario?".
    Cada instancia de esta clase será una fila en la tabla 'game_question' de tu base de datos.
    """

    # Definimos las opciones para la respuesta correcta.
    # Usar 'choices' es una buena práctica porque:
    # 1. Valida los datos: Solo se puede guardar 'A', 'B', 'C', o 'D'.
    # 2. Mejora la UI: En formularios de Django, se muestra como un menú desplegable.
    ANSWER_CHOICES = [
        ('A', 'Opción A'),
        ('B', 'Opción B'),
        ('C', 'Opción C'),
        ('D', 'Opción D'),
    ]

    # Campo para el texto de la pregunta.
    # CharField es para texto de longitud corta a media.
    # 'verbose_name' es el nombre legible que aparecerá en los formularios y en el panel de administración.
    text = models.CharField(
        max_length=500,
        verbose_name="Texto de la Pregunta"
    )

    # Campos para cada una de las cuatro opciones.
    option_a = models.CharField(max_length=200, verbose_name="Opción A")
    option_b = models.CharField(max_length=200, verbose_name="Opción B")
    option_c = models.CharField(max_length=200, verbose_name="Opción C")
    option_d = models.CharField(max_length=200, verbose_name="Opción D")

    # Campo para almacenar cuál de las opciones es la correcta.
    # max_length=1 es suficiente para guardar una letra.
    # 'choices=ANSWER_CHOICES' vincula este campo a las opciones que definimos arriba.
    correct_answer = models.CharField(
        max_length=1,
        choices=ANSWER_CHOICES,
        verbose_name="Respuesta Correcta"
    )

    # Campo para el valor monetario de la pregunta.
    # IntegerField es para números enteros.
    # 'default=100' asegura que si no especificas un premio, se asigne uno por defecto.
    prize_level = models.IntegerField(
        default=100,
        verbose_name="Nivel de Premio ($)"
    )

    def __str__(self):
        """
        Este método es muy importante. Define cómo se mostrará un objeto 'Question'
        cuando se imprima o se vea en el panel de administración de Django.
        En lugar de ver "<Question object (1)>", verás el texto real de la pregunta,
        lo cual es mucho más útil.
        """
        return self.text