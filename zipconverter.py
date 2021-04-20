import zipfile


def zip_file_maker(zip_file_name,code_file):

    my_zip = zipfile.ZipFile(zip_file_name, 'w')
    my_zip.write(code_file)
    my_zip.close()

    return 'ZipFile {0} created with file containing {1}.'.format(zip_file_name,code_file)