# import os
# import cv2
# import sys
#
#
# def draw_box_corner(draw_img,bbox,length,corner_color):
#     # Top Left
#     cv2.line(draw_img, (bbox[0], bbox[1]), (bbox[0] + length, bbox[1]), corner_color, thickness=3)
#     cv2.line(draw_img, (bbox[0], bbox[1]), (bbox[0], bbox[1] + length), corner_color, thickness=3)
#     # Top Right
#     cv2.line(draw_img, (bbox[2], bbox[1]), (bbox[2] - length, bbox[1]), corner_color, thickness=3)
#     cv2.line(draw_img, (bbox[2], bbox[1]), (bbox[2], bbox[1] + length), corner_color, thickness=3)
#     # Bottom Left
#     cv2.line(draw_img, (bbox[0], bbox[3]), (bbox[0] + length, bbox[3]), corner_color, thickness=3)
#     cv2.line(draw_img, (bbox[0], bbox[3]), (bbox[0], bbox[3] - length), corner_color, thickness=3)
#     # Bottom Right
#     cv2.line(draw_img, (bbox[2], bbox[3]), (bbox[2] - length, bbox[3]), corner_color, thickness=3)
#     cv2.line(draw_img, (bbox[2], bbox[3]), (bbox[2], bbox[3] - length), corner_color, thickness=3)
#
#
# def draw_label_type(draw_img,bbox,label_color):
#     label = str(bbox[-1])
#     labelSize = cv2.getTextSize(label + '0', cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
#     if bbox[1] - labelSize[1] - 3 < 0:
#         cv2.rectangle(draw_img,
#                       (bbox[0], bbox[1] + 2),
#                       (bbox[0] + labelSize[0], bbox[1] + labelSize[1] + 3),
#                       color=label_color,
#                       thickness=-1
#                       )
#         cv2.putText(draw_img, label,
#                     (bbox[0], bbox[1] + labelSize + 3),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.5,
#                     (0, 0, 0),
#                     thickness=1
#                     )
#     else:
#         cv2.rectangle(draw_img,
#                       (bbox[0], bbox[1] - labelSize[1] - 3),
#                       (bbox[0] + labelSize[0], bbox[1] - 3),
#                       color=label_color,
#                       thickness=-1
#                       )
#         cv2.putText(draw_img, label,
#                     (bbox[0], bbox[1] - 3),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.5,
#                     (0, 0, 0),
#                     thickness=1
#                     )
#
#
# def test_box(img,bbox,draw_type=False,box_color=(255,0,255),text_color=(0,255,0)):
#     draw_img = img.copy()
#     pt1 = (bbox[0], bbox[1])
#     pt2 = (bbox[2], bbox[3])
#     cv2.rectangle(draw_img, pt1, pt2, color=box_color, thickness=2)
#     if draw_type:
#         type = bbox[-1]
#         cv2.putText(draw_img, str(type), (int(bbox[0]/2 + bbox[2]/2-20), int(bbox[1]+20)),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=text_color, thickness=1
#                     )
#     return draw_img
#
#
# def test_corner_box(img,bbox, l=20, is_transparent=False,draw_type=False,draw_corner=False,box_color=(255,0,255)):
#     draw_img = img.copy()
#     pt1 = (bbox[0], bbox[1])
#     pt2 = (bbox[2], bbox[3])
#
#     out_img = img
#     if is_transparent:
#         alpha = 0.8
#         #alpha = 0.5
#         cv2.rectangle(draw_img, pt1, pt2, color=box_color, thickness=-1)
#         out_img = cv2.addWeighted(img,alpha,draw_img,1-alpha,0)
#
#     cv2.rectangle(out_img, pt1, pt2, color=box_color, thickness=2)
#
#     if draw_type:
#         draw_label_type(out_img,bbox,label_color=box_color)
#     if draw_corner:
#         draw_box_corner(out_img, bbox, length=l, corner_color=(0,255,0))
#     return out_img
#
#
# def test1():
#     img_name = './pikachu.jpg'
#     img = cv2.imread(img_name)
#     box = [140, 16, 468, 390, "pikachu"]
#     box_color = (255, 0, 255)  # pink
#     out_img = test_corner_box(img, box, l=30, is_transparent=False, draw_type=False, draw_corner=False,
#                                box_color=box_color)
#     cv2.imshow("1", out_img)
#     cv2.waitKey(0)
#
#
# def test2():
#     img_name = './pikachu.jpg'
#     img = cv2.imread(img_name)
#     box = [140, 16, 468, 390, "pikachu"]
#     box_color = (255, 0, 255)  # pink
#     out_img = test_corner_box(img, box, l=30, is_transparent=False, draw_type=True, draw_corner=False,
#                                box_color=box_color)
#     cv2.imshow("2", out_img)
#     cv2.waitKey(0)
#
#
# def test3():
#     img_name = './pikachu.jpg'
#     img = cv2.imread(img_name)
#     box = [140, 16, 468, 390, "pikachu"]
#     box_color = (255, 0, 255)  # pink
#     out_img = test_corner_box(img, box, l=30, is_transparent=False, draw_type=True, draw_corner=True,
#                                box_color=box_color)
#     cv2.imshow("3", out_img)
#     cv2.waitKey(0)
#
#
# def test4():
#     img_name = './pikachu.jpg'
#     img = cv2.imread(img_name)
#     box = [140, 16, 468, 390, "pikachu"]
#     box_color = (255, 0, 255)  # pink
#     out_img = test_corner_box(img, box, l=30, is_transparent=True, draw_type=True, draw_corner=True,
#                                box_color=box_color)
#     cv2.imshow("4", out_img)
#     cv2.waitKey(0)
#
#
# def test5():
#     img1 = cv2.imread("./sample/src.jpg")
#     img2 = cv2.imread("./sample/fill.jpg")
#     alpha = 0.6
#     out_img = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
#     small_image = cv2.resize(out_img,(960,600))
#     cv2.imshow("5", small_image)
#     cv2.waitKey(0)
#
#
# if __name__ == "__main__":
#     test1()
#     test2()
#     test3()
#     test4()
#     test5()
import json
import os, cv2
from tqdm import tqdm

train_json = r'E:\Deep-learning\fewshotlogodetection_round1_train_202204\train\annotations\instances_train2017.json'
train_path = r'E:\Deep-learning\fewshotlogodetection_round1_train_202204\train\images/'

def visualization_bbox1(num_image, json_path,img_path):# ???????????????num???????????? ?????????json?????????????????????
    with open(json_path,encoding='utf-8') as annos:
        annotation_json = json.load(annos)

    print('the annotation_json num_key is:',len(annotation_json))  # ??????json????????????????????????
    print('the annotation_json key is:', annotation_json.keys()) # ??????json??????????????????
    print('the annotation_json num_images is:', len(annotation_json['images'])) # json??????????????????????????????

    image_name = annotation_json['images'][num_image - 1]['file_name']  # ???????????????
    id = annotation_json['images'][num_image - 1]['id']  # ????????????id

    image_path = os.path.join(img_path, str(image_name).zfill(5)) # ??????????????????
    image = cv2.imread(image_path, 1)  # ???????????????????????????????????????
    num_bbox = 0  # ?????????????????????bbox?????????

    for i in range(len(annotation_json['annotations'][::])):
        if  annotation_json['annotations'][i-1]['image_id'] == id:
            num_bbox = num_bbox + 1
            x, y, w, h = annotation_json['annotations'][i-1]['bbox']  # ????????????
            image = cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 255), 2)

    print('The unm_bbox of the display image is:', num_bbox)

    # ????????????1??????plt.imshow()??????
    # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #??????????????????CV???BGR??????RGB
    # plt.show() #????????????

    # ????????????2??????cv2.imshow()??????
    cv2.namedWindow(image_name, 0)  # ????????????
    cv2.resizeWindow(image_name, 1000, 1000) # ??????500*500?????????
    cv2.imshow(image_name, image)
    cv2.waitKey(0)

def draw_all(json_path,img_path):
    with open(json_path,encoding='utf-8') as annos:
        annotation_json = json.load(annos)

    print('the annotation_json num_key is:',len(annotation_json))  # ??????json????????????????????????
    print('the annotation_json key is:', annotation_json.keys()) # ??????json??????????????????
    print('the annotation_json num_images is:', len(annotation_json['images'])) # json??????????????????????????????

    for image in tqdm(annotation_json['images']):
        image_name = image['file_name']
        id = image['id']

        image_path = os.path.join(img_path, str(image_name).zfill(5)) # ??????????????????
        image = cv2.imread(image_path, 1)  # ???????????????????????????????????????


        for i in range(len(annotation_json['annotations'][::])):
            if annotation_json['annotations'][i - 1]['image_id'] == id:
                x, y, w, h = annotation_json['annotations'][i - 1]['bbox']  # ????????????
                image = cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 255), 2)

        if not os.path.exists('./draw'):
            os.makedirs('./draw')
        cv2.imwrite(os.path.join('./draw',image_name),image)

if __name__ == "__main__":
   # visualization_bbox1(1, train_json, train_path)
    draw_all(train_json, train_path)



