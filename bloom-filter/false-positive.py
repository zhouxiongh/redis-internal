import redis

client = redis.StrictRedis()
client.delete("codehole")

for i in range(100000):
    client.execute_command("bf.add", "codehole", "user%d" % i)
    # 注意 i+1，这个是当前布隆过滤器没见过的
    ret = client.execute_command("bf.exists", "codehole", "user%d" % (i+1))
    if ret == 1:
        print(i)
        break
