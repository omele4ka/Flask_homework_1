# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def news_block():
    context = [
        {'title' : 'Какая-то новость',
         'text' : 'варырмымжымжтымыыом',
         'date' : '12.12.2023'},
        {'title' : 'Еще какая-то новость',
         'text' : 'варырмымжымжтымыыом ымгрышм',
         'date' : '12.12.2023'},
        {'title' : 'Супер важная новость',
         'text' : 'варырмымжымжтымыыом',
         'date' : '12.12.2023'}
    ]

    return render_template('news.html', context=context)

if __name__== '__main__':
    app.run(debug=True)