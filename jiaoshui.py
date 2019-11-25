import subprocess
import time
import os


# 使用popen
def execmd(cmd):
    # subprocess.Popen(cmd, stdout=subprocess.PIPE,
    #                  stderr=subprocess.PIPE)
    # f = os.popen(cmd)
    # text = f.read()
    # f.close()
    os.system(cmd)


def loop_click_for_android(run_num=150):
    res = subprocess.Popen('adb devices',
                           shell=True, stdout=subprocess.PIPE)
    res.stdout.read()
    inputs = str(input("请确保已打开测试页面(y/n)： "))

    if inputs == "y":
        num = 0
        node_time = time.time()
        # start_buttun = subprocess.Popen("adb shell input tap 500 1000")
        # if start_buttun:
        while True:
            time.sleep(0.5)
            execmd("adb shell input tap 967 1986")
            num += 1
            print(num)
            if num == run_num:
                return

            # else:


#     print("程序关闭~")
#     exit(1)


if __name__ == '__main__':
    loop_click_for_android(200)
