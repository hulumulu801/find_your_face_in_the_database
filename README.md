# В разработке

Этот скрипт ищет в базе данных изображений заданное лицо.

# Описание файлов:
  
  - find_face_in_base_data.py - сам скрипт
  
  - shape_predictor_68_face_landmarks.dat - предварительно обученная модель сверточной нейронной сети для выделений на фотографий лица с помощью 68 ключевых точек от dlib
  
  - dlib_face_recognition_resnet_model_v1.dat - сверточная нейронная сеть выделяющая дескрипторы из лиц людей, так же от dlib

# Как установить на Linux(Ubuntu, Debian):

  - устанавливаем dlib:
  
    sudo apt-get update && sudo apt-get install build-essential cmake -y && sudo apt-get install libopenblas-dev liblapack-dev -y
    
    sudo apt-get install libx11-dev libgtk-3-dev -y && sudo apt-get install python python-dev python-pip -y && sudo apt-get install python3 python3-dev python3-pip -y && sudo apt-get install cmake -y
    
    sudo apt-get install python-matplotlib python-numpy python-pil python-scipy -y
    
    
