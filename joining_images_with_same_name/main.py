import os
import cv2

folder_1_path = "/home/neosoft/Documents/Assignments/joining_files_same_name/folder_1"
folder_2_path = "/home/neosoft/Documents/Assignments/joining_files_same_name/folder_2"
result_folder_path = "/home/neosoft/Documents/Assignments/joining_files_same_name/result_folder"


def write_text_on_image(folder_path, text):
    """
    Return images by writing text on them.
    :param folder_path: The folder's location contains images on which text will be written.
    :param text: The text that will be written on the image.
    :return: The image with written text on it.
    """
    for file_path in os.listdir(folder_path):
        img_path = folder_path + "/" + file_path

        # Reading an image in default mode
        img = cv2.imread(img_path)

        # cv2.putText(image, text, org, font, fontScale, color, thickness, lineType)
        image = cv2.putText(img, text, (90, 120), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 20, 147), 2, cv2.LINE_AA)

        # Save the edited image
        # result_img_path = img_path
        # cv2.imwrite(result_img_path, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


write_text_on_image(folder_1_path, "folder_1")
write_text_on_image(folder_2_path, "folder_2")
same_files = []


def join_same_file_horizontal(folder_1_path, folder_2_path):
    """
    When the names of the images in the folders are the same, join the images horizontally.
    :param folder_1_path: The location of the one folder
    :param folder_2_path: The location of the other folder
    """
    for file_path_1 in os.listdir(folder_1_path):
        for file_path_2 in os.listdir(folder_2_path):
            if file_path_1 == file_path_2:
                same_files.append((file_path_1, file_path_2))
                img_path_1 = folder_1_path + "/" + file_path_1
                img_path_2 = folder_2_path + "/" + file_path_2

                img1 = cv2.imread(img_path_1)
                img2 = cv2.imread(img_path_2)

                # v_img = cv2.vconcat([img1, img2])  # joining vertically
                result_img = cv2.hconcat([img1, img2])  # joining horizontally

                cv2.imshow('Input Image', img1)
                cv2.imshow('Horizontal', result_img)
                # cv2.imshow('Vertical', v_img)

                # result_path = result_folder_path + "/" + file_path_1
                # cv2.imwrite(result_path, result_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print(file_path_2)


join_same_file_horizontal(folder_1_path, folder_2_path)
