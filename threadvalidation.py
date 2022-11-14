import time
import concurrent.futures
import requests
import threading
import multiprocessing
import sys

img_urls = [
        "https://cdn.pixabay.com/photo/2019/03/07/03/41/troll-4039410_1280.png",
        "https://cdn.pixabay.com/photo/2016/01/20/17/45/figure-1152044_1280.png"
]
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == "__main__":
    arg = sys.argv[1:]
    listpool = []
    listthread = []
    listmulti = []

    try:
        for b in range(int(arg[0])):
        #méthode pool de threads
            start1 = time.perf_counter()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(download_image, img_urls)

            end1 = time.perf_counter()
            listpool.append(round(end1 - start1, 2))
            #print(f"Tasks with pool ended in {round(end1 - start1, 2)} second(s)")
            print('\n')


        #méthode threading.thread
            t = []
            start2 = time.perf_counter()
            for i in range (len(img_urls)):
                t.append(threading.Thread(target=download_image, args=[img_urls[i]]))
                t[i].start()
            for i in range (len(t)):
                t[i].join()
            end2 = time.perf_counter()
            listthread.append(round(end2 - start2, 2))
            #print(f"Tasks with threading.thread ended in {round(end2 - start2, 2)} second(s)")
            print('\n')


        #méthode multiprocessing
            a = []
            start3 = time.perf_counter()
            for i in range (len(img_urls)):
                a.append(multiprocessing.Process(target=download_image, args=[img_urls[i]]))
                a[i].start()
            for i in range (len(a)):
                a[i].join()
            end3 = time.perf_counter()
            listmulti.append(round(end3 - start3, 2))
            #print(f"Tasks with multiprocessing ended in {round(end3 - start3, 2)} second(s)")
            print('\n')
    except:
        print("Saisir un nombre entier")
    else:
        print(listpool)
        print(listthread)
        print(listmulti)
