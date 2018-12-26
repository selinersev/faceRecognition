
import face_recognition
from scipy.spatial import distance
import shutil


def main():
    path = "/Users/selinersev/Desktop/orl_faces/"
    test = []
    train = []
    train_person_name = []
    test_person_name = []
    train_person_filename = []
    test_person_filename = []
    fail_count = 0
    failure_path = "/Users/selinersev/Desktop/featureExtractionFailure/"

    for i in range(1,41):
        for j in range(1,6):
            img_path = str(path)+'s'+str(i)+'/'+str(j)+'.pgm'
            img = face_recognition.load_image_file(img_path)
            train_faces_encodings = face_recognition.face_encodings(img)
            if len(train_faces_encodings) == 0:
                shutil.copyfile(img_path, failure_path+str(i)+'.'+str(j)+'.pgm')
                #os.rename(img_path, failure_path+str(i)+'.'+str(j)+'.pgm')
                print ('excluded train data --> s'+str(i)+" "+str(j))

            else:
                train.append(train_faces_encodings[0])
                train_person_name.append('s' + str(i))
                train_person_filename.append(str(j)+'.pgm')

    for i in range(1,41):
        for j in range(6,11):
            img_path = str(path)+'s'+str(i)+'/'+str(j)+'.pgm'
            img = face_recognition.load_image_file(img_path)
            test_faces_encodings = face_recognition.face_encodings(img)
            if len(test_faces_encodings) == 0:
                print ('excluded test data --> s'+str(i)+" "+str(j))
            else:
                test.append(test_faces_encodings[0])
                test_person_name.append('s' + str(i))
                test_person_filename.append(str(j)+'.pgm')

    success_count = 0
    test_index = 0
    for testVector in test:
        temp_array = []
        for trainVector in train:
            dst = distance.euclidean(trainVector, testVector)
            temp_array.append(dst)
        min_index = temp_array.index(min(temp_array))
        min_person = train_person_name[min_index]
        test_per_name = test_person_name[test_index]
        min_person_file = train_person_filename[min_index]
        test_per_name_file = test_person_filename[test_index]
        print(min_person)
        print('-----')
        print(test_per_name)
        print (min_person_file+' === '+test_per_name_file)
        print ('*-*-*-*-*-*-*-*-*-*-*-')
        if min_person == test_per_name:
            success_count += 1
        else:
            fail_count += 1
            print ('Fail!!!! ' + min_person)
        test_index += 1

    print ('successCount:'+str(success_count))
    print ('failCount:' + str(fail_count))
    rate = success_count / (success_count + fail_count)
    print('rate:'+str(rate))


if __name__ == "__main__":
    main()