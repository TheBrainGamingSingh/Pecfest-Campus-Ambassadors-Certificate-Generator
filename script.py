import csv
import cv2


font                   = cv2.FONT_HERSHEY_TRIPLEX
fontScale              = 3
fontColor              = (0,0,0)
lineType               = 2

with open('stu.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        img = cv2.imread('certificate.jpg')
        print(f'\t{row[0]} works in the {row[1]}')
        bottomLeftCornerOfText = (1200,1280)
        cv2.putText(img,f'{row[0]}',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
        bottomLeftCornerOfText = (550,1480)
        cv2.putText(img,f'{row[1]}',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
        out = row[0] + '_' + row[1]
        cv2.imwrite(f'{out}.jpg', img)
        
