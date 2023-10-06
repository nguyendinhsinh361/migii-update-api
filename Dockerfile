FROM python:3.11.4

WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install 'uvicorn[standard]'

# Install python-dotenv
RUN pip install python-dotenv

# Copy the .env file into the container
COPY .env /code/.env

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]