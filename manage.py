#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    #Phouw
    os.system(""" DIR="/home/runner/The-Adoption-Center/venv/lib/python3.8/site-packages/django/contrib/auth/templates"
BASE="/home/runner/The-Adoption-Center/html"   
DIR2="/home/runner/The-Adoption-Center/venv/lib/python3.8/site-packages/django/contrib/admin/templates/"

cd /home/runner/The-Adoption-Center/html
for i in *.html
do
        cmp -s $i $DIR/$i
        if [ $? -ne 0 ]
        then
                cp $i $DIR/
                echo "Successfully created a backup for $i"
        else
            echo "$i has no update"
        fi
done

for i in *.html
do
        cmp -s $i $DIR2/$i
        if [ $? -ne 0 ]
        then
                cp $i $DIR2/
                echo "Successfully created a backup for $i"
        else
            echo "$i has no update"
        fi
done

cd /home/runner/The-Adoption-Center/css
for i in *.css
do
        cmp -s $i $DIR/$i
        if [ $? -ne 0 ]
        then
                cp $i $DIR/
                echo "Successfully created a backup for $i"
        else
            echo "$i has no update"
        fi
done

for i in *.css
do
        cmp -s $i $DIR2/$i
        if [ $? -ne 0 ]
        then
                cp $i $DIR2/
                echo "Successfully created a backup for $i"
        else
            echo "$i has no update"
        fi
done


""")

    #Phouw
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
