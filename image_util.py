import cv2
import numpy as np
import requests as r

def are_similar(original, image_to_compare, threshold=60):
    # 1) Check if 2 images are equals
    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
            return True
        else:
            print("The images are NOT equal")

    # 1) Check image similarity
    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(original, None)
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    ratio = 0.6
    for m, n in matches:
        if m.distance < ratio*n.distance:
            good_points.append(m)

    print("Number of good points: ", len(good_points))
    if len(good_points) > threshold:
        print('The images are similar')
        return True
    else:
        print('The images are different')
        return False

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = r.get(url)

    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image


if __name__ == '__main__':
    original = cv2.imread("data/images/3.jpeg")
    image_to_compare = cv2.imread("data/images/3-1.jpeg")
    check_similar(original, image_to_compare)
    main()

