import json
from pycocotools.coco import COCO

# with open('train.json', 'rt', encoding='UTF-8') as annotations:
#     coco = json.load(annotations)
#
# info = coco['info']
# licenses = coco['licenses']
# images = coco['images']
# annotations = coco['annotations']
# categories = coco['categories']
#
#
#
# with open('val1.json', 'wt', encoding='UTF-8') as coco:
#     json.dump({ 'info': info, 'licenses': licenses, 'images': images,
#         'annotations': annotations, 'categories': categories}, coco, indent=2, sort_keys=True,ensure_ascii=False)

coco = COCO(annotation_file='val.json')
annotations = coco.dataset['annotations']

imgs_id = coco.getImgIds(catIds=1)
for img_id in imgs_id:
    ann_id = coco.getAnnIds(imgIds=img_id,catIds=1)
    if len(ann_id) > 1:
        for id in ann_id:
            pass
imageid_list = []
annaid_list = []
for i,annotation in enumerate(annotations):
    if annotation['category_id'] != 1:
        continue
    annaid_list.append(i)
    if annotation['image_id'] not in imageid_list:
        imageid_list.append({annotation['image_id']:[annotation['bbox']]})
    else:
        imageid_list[annotation['image_id']].append(annotation['bbox'])
print(annaid_list)
print(imageid_list)

i = 0
for each in imageid_list:
    print(i,each.values())
    i+=1

# del_list=[94,92,90,88,86,84,82,79,78,76,74,72,70,68,67,64,63,60,58,56,54,52,50,48,46,45,44,40,38,36,35,34,33,32,31]
del_list = [17,15,13,11,9,8,7,6]

del_anna = [annaid_list[i] for i in del_list]

for i in del_anna:
    del annotations[i]

info = coco.dataset['info']
licenses = coco.dataset['licenses']
images = coco.dataset['images']
categories = coco.dataset['categories']

with open('val1.json', 'wt', encoding='UTF-8') as coco:
    json.dump({ 'info': info, 'licenses': licenses, 'images': images,
        'annotations': annotations, 'categories': categories}, coco, indent=2, sort_keys=True,ensure_ascii=False)