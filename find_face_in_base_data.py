#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################################################################################################################
import os
import sys
import dlib
import glob
import shutil
from PIL import Image
from skimage import io
from scipy.spatial import distance
from skimage.draw import polygon_perimeter
###################################################################################################################
def target_person(tar_per, detector, sp, facerec, win):
    try:
        img = io.imread(tar_per)
        win.clear_overlay()
        win.set_image(img)
        dets = detector(img, 1)
        for k, d in enumerate(dets):
            polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()],
                                [d.right(), d.left(), d.left(), d.right()])
            shape = sp(img, d)
            win.clear_overlay()
            win.add_overlay(d)
            win.add_overlay(shape)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        return face_descriptor
    except Exception as e:
        pass
###################################################################################################################
def delete_picture(f):
    try:
        print("Файл: " + str(f) + " удален!")
        os.remove(str(f))
    except Exception as e:
        pass
###################################################################################################################
def image_flip_and_picture_find_face(f, detector, sp, facerec, win):
    try:
        coup_counter = 0
        f_descriptors = []
        faces_dets = []
        while coup_counter <= 4:
            img_1 = Image.open(f)
            img_1.transpose(Image.ROTATE_90).save(str(f))
            coup_counter += 1
            print("Обрабатываемое лицо: " + str(f))
            img = dlib.load_rgb_image(f)
            win.clear_overlay()
            win.set_image(img)
            dets = detector(img, 2)
            print("Найдено лиц: {}".format(len(dets)))

            faces_dets.append(format(len(dets)))

            for k, d in enumerate(dets):
                polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()],
                                    [d.right(), d.left(), d.left(), d.right()])
                shape = sp(img, d)
                win.clear_overlay()
                win.add_overlay(d)
                win.add_overlay(shape)
                face_descriptor = facerec.compute_face_descriptor(img, shape)
                f_descriptors.append(face_descriptor)

        if len(set(faces_dets)) == True:
            delete_picture(f)

        return f_descriptors
    except Exception as e:
        pass
###################################################################################################################
def move_picture(f):
    try:
        name_folder = "copy_img"
        path_name = os.path.abspath(f)
        if not os.path.exists(name_folder):
            os.makedirs(name_folder)
        path = os.path.abspath(name_folder)
        print("\n" + str("- - ") * 20 + "\nВероятно на фото: " + str(path_name) + " один и тот же человек!!!" + "\nФайл скопированн в папку: " + str(path) + "\n" + str("- - ") * 20)
        shutil.move(path_name, path)
    except Exception as e:
        pass
###################################################################################################################
def comparison_of_allocated_descriptors(t_p, f_f, f):
    try:
        a = distance.euclidean(f_f, t_p)
        f_1 = round(a, 2)
        if 0 <= f_1 <= 0.60:
            move_picture(f)
        elif 0.60 <= f_1 <= 1:
            print("Нет совпадений")
            delete_picture(f)
    except Exception as e:
        pass
###################################################################################################################
def main():
    try:
        detector = dlib.get_frontal_face_detector()
        sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
        win = dlib.image_window()
        tar_per = sys.argv[1]
        faces_folder_path = sys.argv[2]
        t_p = target_person(tar_per, detector, sp, facerec, win)
        picture_counter = 0
        for f in glob.glob(os.path.join(faces_folder_path, "*.*")):
            if str(f).split(".")[-1] == "jpg" or str(f).split(".")[-1] == "jpeg" or str(f).split(".")[-1] == "png":
                folder_where_to_f_f = image_flip_and_picture_find_face(f, detector, sp, facerec, win)
                picture_counter += 1
                for f_f in folder_where_to_f_f:
                    comparison_of_allocated_descriptors(t_p, f_f, f)
                print("Просмотренно изображений: " + str(picture_counter))
                print("#" * 100)
            else:
                print("= = " * 20 + "\nФайл: " + str(f) + " нечитаемый!!!\n" + "= = " * 20)
    except Exception as e:
        pass
###################################################################################################################
if __name__ == "__main__":
    main()
