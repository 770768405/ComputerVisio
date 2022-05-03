from tqdm import tqdm
import shutil
from pycocotools.coco import COCO


coco = COCO(annotation_file='./val.json')

for i in tqdm(coco.imgs):
    i = coco.imgs[i]
    name = i['file_name']
    id = i['id']
    img_width = i['width']
    img_height = i['height']
    annotations = coco.imgToAnns[id]
    with open('./yolo/val/labels/'+name.split('.')[0]+'.txt', "w") as f:
        for index,annotation in enumerate(annotations):
            x = annotation['bbox'][0]
            y = annotation['bbox'][1]
            w = annotation['bbox'][2]
            h = annotation['bbox'][3]
            category = annotation['category_id']-1

            # 绝对坐标转相对坐标，保存6位小数
            x = round(x / img_width, 6)
            y = round(y / img_height, 6)
            w = round(w / img_width, 6)
            h = round(h / img_height, 6)

            info = [str(i) for i in [category, x, y, w, h]]

            if index == 0:
                f.write(" ".join(info))
            else:
                f.write("\n" + " ".join(info))
    # shutil.copyfile(r'E:\Deep-learning\fewshotlogodetection_round1_train_202204\train\images\\'+name,'./yolo/val/images/'+name)