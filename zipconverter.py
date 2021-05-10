import zipfile


def zip_file_maker(zip_file_name, code_file):
    path = 'C:/Users/Rahul/PycharmProjects/boto3demo/Ques_2/'
    my_zip = zipfile.ZipFile(path+zip_file_name, 'w')
    my_zip.write(path+code_file)
    my_zip.close()

    return 'ZipFile {0} created with file containing {1}.'.format(zip_file_name, code_file)