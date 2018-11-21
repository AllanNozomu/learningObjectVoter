import re
from masteraula.questions.models import Question

question_list=[]
prog = re.compile("(.|\n)*(<img[\\\/ \w \d]*?src=\"(.|\n)+?\"[\\\/ \w \d]*?>)(.|\n)*")
for question in Question.objects.all():
    result = prog.match(question.statement)
    if result:
        disciplines = [d.name for d in question.disciplines.all()]
        if 'Português' in disciplines and not question.learning_object:
            question_list.append((question.id, result.groups()[1]))
question_list.sort()

html_str = '''
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script>
            function send(cb){
                $.get("http://localhost:8765/" + cb.id + "=" + (cb.checked ? "1" : "0"));
            }
            function save(){
                $.get("http://localhost:8765/save");
            }
        </script>
    </head>
    <body>'''

question_list_ids = [q[0] for q in question_list] 
questions = Question.objects.filter(id__in=question_list_ids)
for question in questions:
    html_str = html_str + ("<hr><p> Questao %d </p>" % question.id)
    html_str = html_str + question.statement
    html_str = html_str + ('<input type="checkbox" id="%d" onchange="send(this);">' % question.id)

html_str = html_str +  '<input type="button" id="1" onclick="save();">SALVAR</input></body></html>'

html_file = open('portugues.html', 'w')
html_file.write(html_str)
html_file.close()