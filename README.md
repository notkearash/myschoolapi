# Basic Mock School REST API
for my very first experience with DRF (Django REST Framework), I decided to mock up a school student system.

---

## Demonstration

First make sure you have python installed on your system.

Then make sure you have the required libraries
```
pip install -r requirements.txt
```
Fire up the server by:
```
./manage.py runserver
```
Now open another terminal and make an object
```
./manage.py shell

>>> from students.models import Student
>>> Student.objects.create(first_name="John", last_name="Doe", age=21, student_id=133713371)
```
Then make a `GET` request to the server.
```
curl http://localhost:8000/student/
# or simply open it in a browser
```
This is the result that you should see:
```
[{"full_name":"John Doe","age":21,"student_id":133713371}]
```

---

## Notes
- Non-professional project. Made for demonstration purposes only.
- Maybe deployed in [my website](https://kearash.io)

---

Licensed by MIT