from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Question, CustomUser, Result


# =========================
def Home(request):
    if not request.session.get('user_id'):
        return redirect('login_user')

    return render(request, 'home.html')

def QuestionCurdPage(request):
    return render(request, 'Questions/questioncurd.html')

# CREATE QUESTION
def CreateQuestion(request):

    if request.method == "POST":

        Question.objects.create(
            qtext=request.POST['qtext'],
            op1=request.POST['op1'],
            op2=request.POST['op2'],
            op3=request.POST['op3'],
            op4=request.POST['op4'],
            corr_answer=request.POST['corr_answer'],
            subject=request.POST['subject']
        )

        return redirect('show_questions')

    return render(request, 'Questions/createquestion.html')


# SHOW ALL QUESTIONS
def ShowAllQuestion(request):

    questions = Question.objects.all()

    return render(
        request,
        'Questions/showallquestion.html',
        {'questions': questions}
    )


# SHOW QUESTION FOR UPDATE
def ShowQuestionforUpdate(request):

    questions = Question.objects.all()

    return render(
        request,
        'Questions/show_update_question.html',
        {'questions': questions}
    )


# UPDATE QUESTION
def UpdateQuestion(request, qno):

    question = get_object_or_404(Question, qno=qno)

    if request.method == "POST":

        question.qtext = request.POST['qtext']
        question.op1 = request.POST['op1']
        question.op2 = request.POST['op2']
        question.op3 = request.POST['op3']
        question.op4 = request.POST['op4']
        question.corr_answer = request.POST['corr_answer']
        question.subject = request.POST['subject']

        question.save()

        return redirect('show_questions')

    return render(
        request,
        'Questions/updatequestion.html',
        {'q': question}
    )


# SHOW QUESTION FOR DELETE
def ShowQuestionforDelete(request):

    questions = Question.objects.all()

    return render(
        request,
        'Questions/show_delete_question.html',
        {'questions': questions}
    )


# DELETE QUESTION
def DeleteQuestion(request, qno):

    question = get_object_or_404(Question, qno=qno)

    if request.method == "POST":
        question.delete()
        return redirect('show_questions')

    return render(
        request,
        'Questions/deletequestion.html',
        {'q': question}
    )


# =========================
# USER CRUD
# =========================

# CREATE USER
def CreateUser(request):

    if request.method == "POST":

        CustomUser.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            role=request.POST['role']
        )

        return redirect('user_dashboard')

    return render(request, 'users/createuser.html')


# SHOW USER DASHBOARD
def ShowUserforCurdPage(request):

    users = CustomUser.objects.all()

    return render(
        request,
        'users/usercurd.html',
        {'users': users}
    )


# UPDATE USER
def UpdateUser(request, uid):

    user = get_object_or_404(CustomUser, uid=uid)

    if request.method == "POST":

        user.username = request.POST['username']
        user.password = request.POST['password']
        user.email = request.POST['email']
        user.role = request.POST['role']

        user.save()

        return redirect('user_dashboard')

    return render(
        request,
        'users/updateuser.html',
        {'u': user}
    )


# DELETE USER
def DeleteUser(request, uid):

    user = get_object_or_404(CustomUser, uid=uid)

    if request.method == "POST":
        user.delete()
        return redirect('user_dashboard')

    return render(
        request,
        'users/deleteuser.html',
        {'u': user}
    )


# =========================
# LOGIN / LOGOUT
# =========================

# LOGIN
def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = CustomUser.objects.filter(username=username, password=password).first()

        if user:
            request.session['user_id'] = user.uid
            request.session['username'] = user.username

            # redirect to HOME dashboard
            return redirect('home')

        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials'
            })

    return render(request, 'users/login.html')
# LOGOUT
def LogoutUser(request):
    request.session.flush()
    return redirect('login_user')

# =========================
# TEST SECTION
# =========================

# START TEST
def StartTest(request):

    subject = request.GET.get('subject')

    if not subject:
        return redirect('subject')

    questions = list(
        Question.objects.filter(subject=subject)
        .values('qno', 'qtext', 'op1', 'op2', 'op3', 'op4', 'corr_answer', 'subject')
    )

    request.session['questions'] = questions
    request.session['index'] = 0
    request.session['score'] = 0
    request.session['subject'] = subject

    return redirect('next_question')

# NEXT QUESTION

def NextQuestion(request):

    questions = request.session.get('questions', [])
    index = request.session.get('index', 0)
    score = request.session.get('score', 0)

    # ❗ SAFETY CHECK (VERY IMPORTANT)
    if not questions:
        return redirect('subject')

    # -------------------------
    # HANDLE ANSWER
    # -------------------------
    if request.method == "POST":

        # CHECK VALID INDEX FIRST
        if index < len(questions):

            selected = request.POST.get('answer')
            correct = questions[index]['corr_answer']

            if selected == correct:
                score += 1
                request.session['score'] = score

        action = request.POST.get('action')

        # NEXT
        if action == "next":
            index += 1

        # PREVIOUS
        elif action == "prev":
            index = max(0, index - 1)

        # END EXAM
        elif action == "end":
            return redirect('end_test')

        request.session['index'] = index

    # -------------------------
    # END CONDITION (SAFE)
    # -------------------------
    if index >= len(questions):
        return redirect('end_test')

    return render(
        request,
        'Test/starttest.html',
        {
            'q': questions[index],
            'index': index + 1,
            'total': len(questions)
        }
    )

def NextQuestion(request):

    questions = request.session.get('questions', [])
    index = request.session.get('index', 0)
    score = request.session.get('score', 0)

    if not questions:
        return redirect('subject')

    if request.method == "POST":

        # save answer
        selected = request.POST.get('answer')

        if index < len(questions):
            correct = questions[index]['corr_answer']
            if selected == correct:
                score += 1
                request.session['score'] = score

        action = request.POST.get('action')

        if action == "next":
            index += 1

        elif action == "prev":
            index = max(0, index - 1)

        elif action == "end":
            return redirect('end_test')

        request.session['index'] = index

    if index >= len(questions):
        return redirect('end_test')

    return render(
        request,
        'Test/starttest.html',
        {
            'q': questions[index],
            'index': index + 1,
            'total': len(questions)
        }
    )
    questions = request.session.get('questions', [])
    index = request.session.get('index', 0)
    score = request.session.get('score', 0)

    # ❗ SAFETY CHECK (VERY IMPORTANT)
    if not questions:
        return redirect('subject')

    # -------------------------
    # HANDLE ANSWER
    # -------------------------
    if request.method == "POST":

        # CHECK VALID INDEX FIRST
        if index < len(questions):

            selected = request.POST.get('answer')
            correct = questions[index]['corr_answer']

            if selected == correct:
                score += 1
                request.session['score'] = score

        action = request.POST.get('action')

        # NEXT
        if action == "next":
            index += 1

        # PREVIOUS
        elif action == "prev":
            index = max(0, index - 1)

        # END EXAM
        elif action == "end":
            return redirect('end_test')

        request.session['index'] = index

    # -------------------------
    # END CONDITION (SAFE)
    # -------------------------
    if index >= len(questions):
        return redirect('end_test')

    return render(
        request,
        'Test/starttest.html',
        {
            'q': questions[index],
            'index': index + 1,
            'total': len(questions)
        }
    )
    questions = request.session.get('questions', [])
    index = request.session.get('index', 0)
    score = request.session.get('score', 0)

    # -------------------------
    # HANDLE ANSWER SUBMISSION
    # -------------------------
    if request.method == "POST":

        selected = request.POST.get('answer')
        correct = questions[index]['corr_answer']

        if selected == correct:
            score += 1
            request.session['score'] = score

        action = request.POST.get('action')

        # NEXT BUTTON
        if action == "next":
            index += 1

        # PREVIOUS BUTTON
        elif action == "prev" and index > 0:
            index -= 1

        # END EXAM BUTTON
        elif action == "end":
            return redirect('end_test')

        request.session['index'] = index

    # -------------------------
    # END CONDITION
    # -------------------------
    if index >= len(questions):
        return redirect('end_test')

    return render(
        request,
        'Test/starttest.html',
        {'q': questions[index], 'index': index + 1, 'total': len(questions)}
    )
# END TEST
def EndTest(request):

    score = request.session.get('score', 0)

    questions = request.session.get('questions', [])

    subject = request.session.get('subject', 'Unknown')

    total = len(questions)

    username = request.session.get('username', 'Guest')

    Result.objects.create(
        username=username,
        subject=subject,
        score=score,
        total=total
    )

    return render(
        request,
        'Test/result.html',
        {
            'score': score,
            'total': total
        }
    )


# SUBJECT PAGE
def subject(request):

    subjects = Question.objects.values_list(
        'subject',
        flat=True
    ).distinct()

    return render(
        request,
        'Test/subject.html',
        {'subjects': subjects}
    )