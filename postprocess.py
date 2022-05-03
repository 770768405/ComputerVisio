import json

with open('cascade_rcnn_x101_32x4d_fpn_20e_coco_4head.test.json','r',encoding='utf-8') as f:
    file = json.load(f)

# image_id = -1
# category = []
# box_num = []
# score = []
# n = 1
# t = 0
# for j,i in enumerate(file):
#     if i['image_id'] != image_id:
#         t += 1
#         if j != 0:
#             box_num.append(n)
#             n = 1
#         category.append(i['category_id'])
#         score.append(i['score'])
#         image_id = i['image_id']
#     else:
#         n += 1
#         category.append(i['category_id'])
#         score.append(i['score'])
# box_num.append(n)
# temp = []
# change_category = []
# m= 0
# for i in box_num:
#     for j in range(i):
#         temp.append(score[m])
#         m += 1
#     change_category.append(category[m-i+temp.index(max(temp))])
#     temp = []
# x = 0
# for i in file:
#     if i['image_id'] != image_id:
#         image_id = i['image_id']
#         try:
#             c = change_category[x]
#         except Exception as e:
#             print(e)
#             print(x)
#             print(image_id)
#             exit()
#         i['category_id'] = c
#         x += 1
#     else:
#         i['category_id'] = c

for i in file:
    i['score'] = 0.5*(1+i['score'])

with open('cascade_rcnn_x101_32x4d_fpn_20e_coco_4head_score.json','w',encoding='utf-8') as f:
    json.dump(file,f)