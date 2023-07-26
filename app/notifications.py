from django.contrib import messages

def show_notification(request, message, level):
    messages.add_message(request, level, message)