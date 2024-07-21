import cv2
import os
import numpy as np

green_background_path = os.path.join(
    os.path.dirname(__file__), 'images/GreenBackground.png')
ob_image_path = os.path.join(os.path.dirname(__file__), 'images/Object.png')
new_background_path = os.path.join(
    os.path.dirname(__file__), 'images/NewBackground.jpg')

bg1_image = cv2.imread(green_background_path, 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread(ob_image_path, 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(new_background_path, 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

cv2.imshow('Green Background', bg1_image)
cv2.waitKey(0)

cv2.imshow('Object', ob_image)
cv2.waitKey(0)

cv2.imshow('New Background', bg2_image)
cv2.waitKey(0)


def _compute_difference(image1, image2):
    return cv2.absdiff(image1, image2)


difference_single_channel = _compute_difference(bg1_image, ob_image)
cv2.imshow('Difference Single Channel', difference_single_channel)
cv2.waitKey(0)


def _compute_binary_mask(image):
    return cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)


_, binary_mask = _compute_binary_mask(difference_single_channel)
cv2.imshow('Binary Mask', binary_mask)
cv2.waitKey(0)


def _replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = _compute_difference(bg1_image, ob_image)

    _, binary_mask = _compute_binary_mask(difference_single_channel)

    return np.where(binary_mask == 255, ob_image, bg2_image)


cv2.imshow('Replaced Background', _replace_background(
    bg1_image, bg2_image, ob_image))
cv2.waitKey(0)
