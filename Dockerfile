# Use a base image with Python
FROM python:3.10  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

COPY chatbot.py .  

EXPOSE 7860 
CMD ["python", "chatbot.py"]
