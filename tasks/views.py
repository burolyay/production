from django.shortcuts import render

# Create your views here.
from tasks.models import Task

# Создание новой задачи
Task.objects.create(title='Название задачи', description='Описание задачи')

# Получение всех невыполненных задач
incomplete_tasks = Task.objects.filter(completed=False)
