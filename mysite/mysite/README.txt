Useful notes from tutorial

after making changes to Models:
-add config to mysite/settings.py INSTALLED_APPS
-run >python manage.py makemigrations polls (or whatever the model is)
this creates a migration. 
We can read a version of the migration with >python manage.py sqlmigrate polls 0001 (pretty cool)
We can use a migration to create model tables in our database >python manage.py migrate

Cool API things from the python shell >python manage.py shell
>>>from polls.models import Choice, Question
>>>Question.objects.all() #we see that there aren't any questions in the system yet
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1
#get question by primary key exact lookup
>>> q2 = Question.objects.get(pk=1)
#try our custom method
>>>q2.was_published_recently()
True

#create choices for the question
>>>q2.choice_set.create(choice_text='not much', votes=0)
>>>q2.choice_set.create(choice_text='The sky', votes=10)
#choice objects have api access to related question objects
>>>c = q2.choice_set.create(choice_text='Just hacking again', votes=5)
>>>c.question
<Question: What's new?>
#Question objects have access to choice objects
>>>q2.choice_set.all()

#follow relationships with double underscores
>>>Choice.objects.filter(question__pub_date__year=current_year)

#delete a choice
>>>c = q2.choice_set.filter(choice_text__startswith='Just hacking')
>>>c.delete


Testing Django client
set up test environment in the shell $python manage.py shell
>>>from django.test.utils import setup_test_environment
>>>setup_test_environment()
