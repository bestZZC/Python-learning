import socket
import sys
import time
import threading
from init import *
from camera import *
jpeg_quality = 60#代表成像质量
buffersize = 65507

host="121.40.110.165"
server_address =(host, 2346)

def client():#从服务器接受信息
    MaxBytes = 1024 * 1024
    host = '121.40.110.165'
    port = 3456
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(30)
    while True:
        try:q
            client.connect((host, port))
            print("already is conected!")
            while True:
                try:
                    recvData = client.recv(MaxBytes)
                    if not recvData:
                        print('接收数据为空，我要退出了')
                        break
                    # localTime = time.asctime(time.localtime(time.time()))
                    # print(localTime, ' 接收到数据字节数:', len(recvData))
                    print(recvData.decode())
                    pass
                except:
                    print("time too long")
                    time.sleep(1)
        except:
            print("没有连上")
            time.sleep(10)

if __name__ == '__main__':
    grabber1 = VideoGrabber(jpeg_quality)#打开读取摄像头线程
    grabber1.setDaemon(True)
    grabber1.start()
    running = True
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#udp视频流
    threading.Thread(target=client, args=()).start()
    tot_frame = 0
    time_sta = time.time()
    while (running):
        time.sleep(0.001)
        buffer = grabber1.get_buffer()
        if buffer is None:
            continue
        # print(len(buffer))
        if len(buffer) > 65507:
            print("The message is too large to be sent within a single UDP datagram. We do not handle splitting the message in multiple datagrams")
            continue
        sk.sendto(buffer.tobytes(), server_address)#发送给客户端
        tot_frame += 1
        # if tot_frame % 100 == 0:
        #     print("{:.2f}fps".format(tot_frame / (time.time() - time_sta)))
    pass
print("Quitting..")
grabber1.stop()#关闭摄像头线程
grabber1.join()
sk.close()