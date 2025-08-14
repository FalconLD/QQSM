from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm
from django.contrib import messages
import os
import platform
from django.http import HttpResponse
from django.template import loader
import threading 

# --- Vistas del Menú y Gestión ---

def home(request):
    """Página de inicio con los botones principales."""
    return render(request, 'game/home.html')

def manage_questions(request):
    """Lista todas las preguntas y permite editarlas o borrarlas."""
    questions = Question.objects.all().order_by('prize_level')
    return render(request, 'game/manage_questions.html', {'questions': questions})

def add_question(request):
    """Muestra un formulario para agregar una nueva pregunta."""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pregunta agregada con éxito!')
            return redirect('manage_questions')
    else:
        form = QuestionForm()
    return render(request, 'game/question_form.html', {'form': form, 'action': 'Agregar'})

def edit_question(request, pk):
    """Muestra un formulario para editar una pregunta existente."""
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pregunta actualizada con éxito!')
            return redirect('manage_questions')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'game/question_form.html', {'form': form, 'action': 'Editar'})

def delete_question(request, pk):
    """Elimina una pregunta."""
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    messages.info(request, 'Pregunta eliminada.')
    return redirect('manage_questions')


# --- Vistas de la Lógica del Juego ---

def play(request):
    """Inicia el juego, resetea el progreso y muestra la primera pregunta."""
    # Guardamos el progreso en la sesión del usuario
    request.session['score'] = 0
    request.session['current_question_index'] = 0
    
    questions = list(Question.objects.all().order_by('prize_level').values_list('pk', flat=True))
    if not questions:
        messages.error(request, 'No hay preguntas en el juego. ¡Agrega algunas primero!')
        return redirect('home')

    request.session['question_pks'] = questions
    
    first_question_pk = questions[0]
    return redirect('play_question', pk=first_question_pk)


def play_question(request, pk):
    """Muestra una pregunta específica del juego."""
    question = get_object_or_404(Question, pk=pk)
    score = request.session.get('score', 0)
    
    context = {
        'question': question,
        'score': score
    }
    return render(request, 'game/play_question.html', context)

def answer_question(request, pk):
    """Valida la respuesta del usuario."""
    if request.method != 'POST':
        return redirect('home')

    question = get_object_or_404(Question, pk=pk)
    user_answer = request.POST.get('answer')

    if user_answer == question.correct_answer:
        # Respuesta correcta
        request.session['score'] = question.prize_level
        
        # Pasamos a la siguiente pregunta
        current_index = request.session.get('current_question_index', 0)
        next_index = current_index + 1
        request.session['current_question_index'] = next_index
        
        question_pks = request.session.get('question_pks', [])
        if next_index < len(question_pks):
            next_question_pk = question_pks[next_index]
            return redirect('play_question', pk=next_question_pk)
        else:
            # ¡Ganó el juego!
            return render(request, 'game/win.html', {'score': question.prize_level})
    else:
        # Respuesta incorrecta
        return render(request, 'game/game_over.html', {'correct_answer': question.get_correct_answer_display(), 'score': request.session.get('score', 0)})
    

def shutdown_server(request):
    """
    Muestra una página de despedida y luego apaga el servidor en un hilo separado.
    """
    def kill_server():
        # Espera un segundo para dar tiempo a que la respuesta HTML se envíe
        threading.Timer(1.0, os.system, args=["taskkill /F /IM python.exe"]).start()

    if platform.system() == "Windows":
        # Inicia el proceso de apagado en segundo plano
        kill_server()

    # Carga y renderiza la plantilla de despedida
    template = loader.get_template('game/shutdown_page.html')
    return HttpResponse(template.render({}, request))