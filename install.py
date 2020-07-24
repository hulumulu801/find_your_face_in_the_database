#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#########################################################################################################################################################################################################################
def download_shape_predictor(abs_path_shape_predictor):
    os.system("wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && bunzip2 shape_predictor_68_face_landmarks.dat.bz2")
    if os.path.exists(abs_path_shape_predictor + "shape_predictor_68_face_landmarks.dat"):
        print("- - " * 20 + "\nФайл shape_predictor_68_face_landmarks.dat успешно скачан!\n" + "- - " * 20)
    else:
        print("- - " * 20 + "\nФайл shape_predictor_68_face_landmarks.dat отсутствует! \nСкачайте файл по ссылке:\nhttp://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2\n" + "- - " * 20)
#########################################################################################################################################################################################################################
def download_dlib(abs_path_dlib):
    os.system("wget https://files.pythonhosted.org/packages/05/57/e8a8caa3c89a27f80bc78da39c423e2553f482a3705adc619176a3a24b36/dlib-19.17.0.tar.gz")
    if os.path.exists(abs_path_dlib + "dlib-19.17.0.tar.gz"):
        print("- - " * 20 + "\nФайл dlib-19.17.0.tar.gz успешно скачан!\n" + "- - " * 20)
        os.system("tar -xvzf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")
        os.system("python3 " + str(abs_path_dlib) + "dlib-19.17.0/" + "setup.py install")
        os.system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0/")
        os.system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")
    else:
        print("- - " * 20 + "\nФайл dlib-19.17.0.tar.gz отсутствует! \nСкачайте файл по ссылке:\nhttps://files.pythonhosted.org/packages/05/57/e8a8caa3c89a27f80bc78da39c423e2553f482a3705adc619176a3a24b36/dlib-19.17.0.tar.gz\n" + "- - " * 20)
#########################################################################################################################################################################################################################
def install_pip(abs_path_pip):
    os.system("pip3 install -r" + str(abs_path_pip))
#########################################################################################################################################################################################################################
def main():
    path = os.path.abspath("./")
    abs_path_shape_predictor = path + "/"
    abs_path_dlib = path + "/"
    abs_path_pip = path + "/" + "requirements.txt"

    if not os.path.exists(abs_path_shape_predictor + "shape_predictor_68_face_landmarks.dat"):
        download_shape_predictor(abs_path_shape_predictor)
    if not os.path.exists(abs_path_dlib + "dlib-19.17.0"):
        download_dlib(abs_path_dlib)
    install_pip(abs_path_pip)
#########################################################################################################################################################################################################################
if __name__ == "__main__":
    main()
