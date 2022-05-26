I extracted text from a PDF file. I implemented code both with and without contours.
To convert pdf to images, I used pdf2image. I saved the images in a folder. Using pytesseract ocr, I extracted text by looping through each image in a folder.

1) With the use of contours:
   I used imread() to read an image. The image was then converted to grayscale and THRESH_BINARY_INV simple thresholding and Otsu’s Binarization were applied to it. 
   I used a rectangular structural element, and after choosing a kernel size, dilation is applied to the threshold image, and contours are found from bottom to top using cv2.findContours(). 
   ![Screenshot from 2022-05-24 16-11-20](https://user-images.githubusercontent.com/99475439/170015254-a17a3086-8b53-4897-98a2-085414ad330b.png)
   I cropped text blocks by looping through each contour and passing them to pytesseract ocr, which reads and stores text in a list.
   As data is read as text boxes, it is easy to separate data and remove extra spaces, new lines, leading and trailing spaces, so I sort the data into recipe names, ingredients, and procedures.
   A csv file was later created and data was stored in it.
   ![recipes_using_contours](https://user-images.githubusercontent.com/99475439/170016807-08ed1a1a-1d7c-4b32-afdc-3e01908823a1.png)

2) Without using contours:-
   I read an image with imread(). The image is then passed to pytesseract ocr, which reads and stores text in a list.
   The data is then sorted into recipe names, ingredients, and procedures using regular expressions, and extra spaces, new lines, leading and trailing spaces are removed.
   A csv file was later created and data was stored in it.
   ![recipes_without_using_contours](https://user-images.githubusercontent.com/99475439/170017019-7295fdaf-e276-419f-be1b-a307aaad7bd2.png)
