import json
from pycocotools.coco import COCO
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

json_path = r'E:\Deep-learning\fewshotlogodetection_round1_train_202204\train\annotations\instances_train2017.json'
# 绘制图像尺度分析图
with open(json_path,encoding='utf-8') as f:
    annotation_json = json.load(f)

h = []
w = []
y = [0,0,0,0,0]
x = ['1000','2000','3000','4000','4000+']
x_scale = ['0.5','1.0','1.5','2.0','2.0+']
y_scale = [0,0,0,0,0]
for each in annotation_json['images']:
    h.append(each['height'])
    w.append(each['width'])

    if each['height']  * each['width'] < 1000*1000:
        y[0] += 1
    elif each['height']  * each['width'] < 2000*2000:
        y[1] += 1
    elif each['height']  * each['width'] < 3000*3000:
        y[2] += 1
    elif each['height']  * each['width'] < 4000*4000:
        y[3] += 1
    else:
        y[4] += 1
    if each['height'] / each['width'] < 0.5:
        y_scale[0] += 1
    elif each['height']  / each['width'] < 1.0:
        y_scale[1] += 1
    elif each['height']  / each['width'] < 1.5:
        y_scale[2] += 1
    elif each['height']  / each['width'] < 2.0:
        y_scale[3] += 1
    else:
        y_scale[4] += 1
fig,ax = plt.subplots(1,3,figsize = (10,6))

ax[0].scatter(h,w,s=3)
ax[0].set_title('h_w')
ax[1].bar(x,y)
ax[1].set_title('h*w')
ax[2].bar(x_scale,y_scale)
ax[2].set_title('h/w')

fig.savefig('image.jpg')
fig.show()


# 绘制bbox分析图
box_h_list = []
box_w_list = []
box_y_list = [0,0,0,0,0]
box_x_list = ['100','200','300','400','400+']
categories = {i+1:0 for i in range(len(annotation_json['categories']))}
x_box_scale = ['0.5','1.0','1.5','2.0','2.0+']
y_box_scale = [0,0,0,0,0]

for bbox in annotation_json['annotations']:
    category = bbox['category_id']
    categories[category] += 1
    box_x,box_y,box_w,box_h = bbox['bbox']
    box_h_list.append(box_h)
    box_w_list.append(box_w)

    if box_h/box_w < 0.5:
        y_box_scale[0] += 1
    elif box_h/box_w < 1.0:
        y_box_scale[1] += 1
    elif box_h/box_w < 1.5:
        y_box_scale[2] += 1
    elif box_h/box_w < 2.0:
        y_box_scale[3] += 1
    else:
        y_box_scale[4] += 1

    if box_h*box_y < 100*100:
        box_y_list[0] += 1
    elif box_h*box_y < 200*200:
        box_y_list[1] += 1
    elif box_h*box_y < 300*300:
        box_y_list[2] += 1
    elif box_h*box_y < 400*400:
        box_y_list[3] += 1
    else:
        box_y_list[4] += 1


fig2,ax2 = plt.subplots(2,2)
ax2[0][0].scatter(box_h_list,box_w_list,s=3)
ax2[0][0].set_title('h_w')
ax2[0][1].bar(box_x_list,box_y_list)
ax2[0][1].set_title('h*w')
ax2[1][0].bar(x_box_scale,y_box_scale)
ax2[1][0].set_title('h/w')
ax2[1][1].bar(categories.keys(),categories.values())
ax2[1][1].set_title('category')

fig2.savefig('bbox.jpg')
fig2.show()

coco = COCO(json_path)
ratio_x = ['0.01','0.02','0.03','0.04','0.05','0.06','0.7','0.08','0.09','0.1','0.2','0.3','0.4','0.5','0.5+']
ratio_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ratio_list = []
ratio_h = []
ratio_w = []
for i in coco.imgToAnns:
    bboxes = coco.imgToAnns[i]
    image_id = bboxes[0]['image_id']
    imgInfo = coco.loadImgs(image_id)[0]
    temp_h = imgInfo['height']
    temp_w = imgInfo['width']
    for box in bboxes:
        temp_box_w = box['bbox'][2]
        temp_box_h = box['bbox'][3]
        ratio= (temp_box_w*temp_box_h)/(temp_h*temp_w)
        ratio_list.append(ratio)
        ratio_h.append(temp_box_h/temp_h)
        ratio_w.append(temp_box_w/temp_w)
        if ratio < 0.01:
            ratio_y[0] += 1
        elif ratio < 0.02:
            ratio_y[1] += 1
        elif ratio < 0.03:
            ratio_y[2] += 1
        elif ratio < 0.04:
            ratio_y[3] += 1
        elif ratio < 0.05:
            ratio_y[4] += 1
        elif ratio < 0.06:
            ratio_y[5] += 1
        elif ratio < 0.07:
            ratio_y[6] += 1
        elif ratio < 0.08:
            ratio_y[7] += 1
        elif ratio < 0.09:
            ratio_y[8] += 1
        elif ratio < 0.1:
            ratio_y[9] += 1
        elif ratio < 0.2:
            ratio_y[10] += 1
        elif ratio < 0.3:
            ratio_y[11] += 1
        elif ratio < 0.4:
            ratio_y[12] += 1
        elif ratio < 0.5:
            ratio_y[13] += 1
        else:
            ratio_y[14] += 1
fig3,ax3 = plt.subplots(1,3,figsize=(14,6))
ax3[0].bar(ratio_x,ratio_y)
ax3[1].scatter(ratio_list,ratio_list,s=1)
ax3[2].scatter(ratio_h,ratio_w,s=1)
fig3.savefig('ratio.jpg')
fig3.show()