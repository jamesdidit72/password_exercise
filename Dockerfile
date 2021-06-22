
FROM python:3
ADD password_exercise/password_functions.py /password_exercise/ 
ADD requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /password_exercise
CMD [ "python", "./password_functions.py" ]
