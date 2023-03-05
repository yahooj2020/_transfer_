import os
import requests




def check_html(baseurl,ret_filename):
    templates_path = os.path.join(os.getcwd(), "templates")
    for (dirname, subdir, subfile) in os.walk(templates_path):

        for htmlfile in subfile:
            base_url = "{0}{1}".format(baseurl,htmlfile)
            res = requests.get(base_url)
            if res.status_code !=200:
                original_file = htmlfile.split(".html")[0]
                print(original_file)


                with open(ret_filename,"a",newline="", encoding="utf-8",buffering=2048) as f:
                    f.write(original_file)
                    f.write("\n")
                    f.flush()
                    # flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
                    #
                    # 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
                    f.close()


if __name__ == "__main__":
    base_url = "http://127.0.0.1:8888/detail/"
    ret_filename = "checked_ret"
    check_html(base_url,ret_filename)

