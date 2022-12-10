sudo docker build . -t app-py
sudo docker run -p 8080:8080 app-py