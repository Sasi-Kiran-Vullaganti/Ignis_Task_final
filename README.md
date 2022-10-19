# Ignis_Task_final
Task

You will be creating a dynamic html page in django like the image below. You should use mysql database for backend. Users should be able to like and unlike the event by clicking on the ‘heart’ symbol.
Users should be able to add new events. Event name, date, time, location and image.
HELP BOX
Create a table with fields as (‘event_name’, ’data’ ,’time’, ‘location’ ,’image’, ‘is_liked’).
By default, is_liked is false.
Create a form to add a new event/entry to the database.
If the event is liked, the heart should be colored red, else white.
Note : the changes made in the UI should be reflected on the database too.

Step-1 -> Download and unzip the folder and open in vscode.
step-2 -> open terminal and run the cmd--> .\venv\Scripts\activate now "cd Ignis_Task"
step-3 -> pip install -r requirements.txt
step-4 -> python manage.py makemigrations
step-5 -> python manage.py migrate
step-6 -> python manage.py runserver
