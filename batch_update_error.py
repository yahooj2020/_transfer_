import os



def re_previous_next(htmlfile):
    return pre_filename,pre_filepath,next_filename,next_filepath,htmlfile


def read_file(file):
    with open(file,encoding="utf-8") as f:
        read_all =f.read()
        f.close()
    return read_all

def rewrite_file(file,data):
    with open(file,"w",encoding="UTF-8") as f:
        f.write(data)
        f.close()


def replace(file,old_c,new_c):
    content = read_file(file)
    content = content.replace(old_c,new_c)
    rewrite_file(file,content)




def remove_file(filename):
    for file in os.listdir("."):
        file_list = file.split(".")
        if len(file_list) != 1:
            os.remove(filename)

if __name__ == "__main__":
    error_file_list = ["b.html"]
    execfile_list = []
    templatePath = os.path.join(os.getcwd(),"templates")
    for dirname, subdir, subfile in os.walk(templatePath):
        for one_file in subfile:
            execfile_list.append(os.path.join(dirname,one_file))

    for item in execfile_list:
        single_error_file = item.split("\\")[-1]
        if single_error_file in error_file_list:
            pre_filename,pre_filepath,next_filename,next_filepath,_ = re_previous_next(item)
            replace(pre_filepath,single_error_file,next_filename)
            replace(next_filepath,single_error_file,pre_filename)
            remove_file(item)



