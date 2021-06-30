import pickle

tasks = [
    {
        'id': 1,
        'title': 'Zakupy',
        'description': 'Mleko, jajka, mąka, olej, papier toaletowy (jak będzie)',
        'done': False
    },
    {
        'id': 2,
        'title': 'Zrobić zadania z Pythona',
        'description': 'Przygotować projekt z modułu i wysłać Mentorowi',
        'done': False
    }
]

with open("todo.pickle", 'wb') as f:
    pickle.dump(tasks, f)

print(tasks)
print(type(tasks))    

with open("todo.pickle", "rb") as f:
    tasks = pickle.load(f)
print(tasks[0])
print(type(tasks))