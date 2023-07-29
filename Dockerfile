FROM python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 80
CMD python server.py
  
