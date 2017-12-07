# Convert the Dataset into the required format(break the train+test data files into separate files) required by the CNN-code

#store train and test image ids
train_image_ids = []
test_image_ids = []
    
with open('data/train_test_split.txt') as train_test_file:
    for image_id,line in enumerate(train_test_file):
        is_train = int(line.strip().split()[1])
        if is_train == 1:
            train_image_ids.append(image_id+1)
        else:
            test_image_ids.append(image_id+1)

print(train_image_ids[0])
print(len(train_image_ids))
print(len(test_image_ids))


#Splitting Images into two files -- images_train.txt and images_test.txt
with open('data/images.txt', 'r') as f:  
    data = f.readlines() 

with open('data/image_class_labels.txt', "r") as l:
    label=l.readlines()

with open('data/test.txt', "w") as test_image_locations, open('data/train.txt', "w") as train_image_locations:
    for i in range(len(data)):
        line=data[i].strip('\n').split(' ')[1]+' '+label[i].split(' ')[1]
        if i+1 in train_image_ids:
            train_image_locations.write(line)
        else:
            test_image_locations.write(line)