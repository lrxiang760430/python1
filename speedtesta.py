import speedtest
import time
t=speedtest.Speedtest()
b=t.get_best_server()
print(f"最佳测速服务器信息:{b}")

dr=t.download()
dr=dr/1024/1024
dr=round(dr,2)

ur=t.upload()
ur=ur/1024/1024
ur=round(ur,2)

#print(dr)
#print(dr/1024/1024)
print(f"下载速度为{dr}Mbps")

#print(ur)
#print(ur/1024/1024)
print(f"上传度为{ur}Mbps")

time.sleep(60)