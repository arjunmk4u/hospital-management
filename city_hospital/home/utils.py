from django.contrib.auth.models import User
from .models import doctors

def create_users_from_model():
    # Retrieve all objects from YourModel
    objects = doctors.objects.all()

    # Iterate over the objects
    for obj in objects:
        # Create a user for each object
        # You may need to customize this part to set the username, email, password, etc. based on your model's fields
        user = User.objects.create_user(username=obj.doc_name, password='defaultpassword')
        
        # Optionally, you can assign the user to specific groups or set other attributes here
        # Example:
        # user.groups.add(some_group)
        # user.is_staff = True
        # user.save()

    # Optionally, you can return a message or perform other actions after creating the users
    return "Users created successfully"
