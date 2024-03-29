# Indicate the Gurobi reference image
FROM gurobi/python:10.0.0

# Set the application directory
WORKDIR /app

# Install the application dependencies
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
#ADD . /app

# Command used to start the application
# CMD ["python","main.py"]