import speedtest
t=speedtest.Speedtest()
b=t.get_best_server()
print(b)

dr=t.download()

ur=t.upload()

print(dr)
print(dr/1024/1024)

print(ur)
print(ur/1024/1024)