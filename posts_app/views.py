from django.shortcuts import redirect, render,get_object_or_404
from .models import Question_Table,Answer_Table,Like_Table
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Q

def Home_Page(request):
    user_id = request.user.id
    answers=Answer_Table.objects.select_related('question_id').order_by('-created_on')
    answers = answers.annotate(num_likes=Count('like_table'))
    return render(request, 'home_page.html', {'answers': answers,'user_id': user_id})

@login_required(login_url='/login')
def Questions_Page(request):
    questions=Question_Table.objects.all().order_by('-created_on')
    print(questions)
    return render(request, 'questions_page.html', {'questions': questions})

@login_required(login_url='/login')
def Ask_Question_Page(request):
    if(request.method == 'POST'):
        message=request.POST.get('message')
        if(len(message)>0):
            user_id=request.user.id
            user_name=request.user.username
            question=message
            # print(user_id, user_name, question)
            data=Question_Table(question_text=question,asked_by_user_id=user_id,asked_by_user_name=user_name)
            data.save()
            return redirect('questions')
        else:
            return redirect('askquestion')
    return render(request, 'ask_question_page.html')

@login_required(login_url='/login')
def Answer_Question_Page(request, question_id):
    question = get_object_or_404(Question_Table, pk=question_id)

    if request.method == 'POST':
        message = request.POST.get('message')

        if len(message) > 0:
            user_id = request.user.id
            user_name = request.user.username

            data = Answer_Table(
                answer_text=message,
                answered_by_user_id=user_id,
                answered_by_user_name=user_name,
                question_id=question 
            )

            data.save()
            return redirect('home')
        else:
            return redirect('answerquestion/' + question_id)

    return render(request, 'answer_question_page.html')

@login_required(login_url='/login')
def Add_Like_Page(request, answer_id, answered_by_user_id):
    answer = get_object_or_404(Answer_Table, pk=answer_id)
    print(answer_id, answered_by_user_id)
    # Check if an entry with the same combination already exists
    existing_like = Like_Table.objects.filter(
        Q(answer_id=answer_id) & Q(liked_by_user_id=answered_by_user_id)
    ).first()
    print(existing_like)
    if existing_like is None:
        # Entry doesn't exist, create a new one
        like = Like_Table(answer_id=answer, liked_by_user_id=answered_by_user_id)
        like.save()
        return redirect('home')
    else:
        # Entry already exists, you can handle it accordingly
        # For example, return an error response or redirect to another page
        return redirect('home')



def Hello_World(request):
    return render(request, 'hello_world.html')

