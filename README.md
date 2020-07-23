# В разработке

Этот скрипт ищет в базе данных изображений заданное лицо.

# Описание файлов:
  
  - find_face_in_base_data.py - сам скрипт
  
  - shape_predictor_68_face_landmarks.dat - предварительно обученная модель сверточной нейронной сети для выделений на фотографий лица с помощью 68 ключевых точек от dlib
  
  - dlib_face_recognition_resnet_model_v1.dat - сверточная нейронная сеть выделяющая дескрипторы из лиц людей, так же от dlib
