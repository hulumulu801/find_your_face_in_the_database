# Описание работы скрипта:

Этот скрипт ищет в базе данных изображений заданное лицо.

**Видео:**

[![Поиск конкретного лица в базе данных с фотографиями.](https://img.youtube.com/vi/N4evIIOrjHw/0.jpg)](https://www.youtube.com/watch?v=N4evIIOrjHw)

# Описание файлов:
  
  - find_face_in_base_data.py - сам скрипт
  
  - requirements.txt - требования для pip
  
  - install.py - установщик
  
  - shape_predictor_68_face_landmarks.dat - предварительно обученная модель сверточной нейронной сети для выделений на фотографий лица с помощью 68 ключевых точек от dlib
  
  - dlib_face_recognition_resnet_model_v1.dat - сверточная нейронная сеть выделяющая дескрипторы из лиц людей, так же от dlib

# Как установить на Linux(Ubuntu, Debian):

  - **устанавливаем git:**
  
    sudo apt install git
    
  - **устанавливаем pip3:**
  
    sudo apt install python3-pip

  - **скачиваем репозиторий:**
    
    git clone https://github.com/hulumulu801/find_your_face_in_the_database.git

  - **устанавливаем dlib:**
  
    sudo apt-get update && sudo apt-get install build-essential cmake -y && sudo apt-get install libopenblas-dev liblapack-dev -y
    
    sudo apt-get install libx11-dev libgtk-3-dev -y && sudo apt-get install python3 python3-dev python3-pip -y && sudo apt-get install cmake -y
    
    sudo apt-get install python3-matplotlib python3-numpy python3-pil python3-scipy -y
    
  - **запускаем install.py:**
  
    cd find_your_face_in_the_database/
  
    python3 install.py
    
# Использование: 

  python3 find_face_in_base_data.py /путь/до/искомого/файла /путь/до/паки/с/файлами/
