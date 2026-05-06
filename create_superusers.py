import os
import sys
import django

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_superusers.py <project_name>")
        sys.exit(1)
        
    project_name = sys.argv[1]
    
    # Add the project directory to the Python path
    project_dir = os.path.abspath(project_name)
    sys.path.append(project_dir)
    
    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
    
    # Setup Django
    django.setup()
    
    from django.contrib.auth.models import User
    
    # Create superusers if they don't exist
    if not User.objects.filter(username='anjan').exists():
        User.objects.create_superuser('anjan', 'anjan@example.com', 'anjan123')
        print(f"Created superuser 'anjan' in {project_name}")
    else:
        # Update password just in case
        u = User.objects.get(username='anjan')
        u.set_password('anjan123')
        u.save()
        print(f"Updated password for 'anjan' in {project_name}")
        
    if not User.objects.filter(username='anjana').exists():
        User.objects.create_superuser('anjana', 'anjana@example.com', 'anjan123')
        print(f"Created superuser 'anjana' in {project_name}")
    else:
        u = User.objects.get(username='anjana')
        u.set_password('anjan123')
        u.save()
        print(f"Updated password for 'anjana' in {project_name}")

if __name__ == "__main__":
    main()
