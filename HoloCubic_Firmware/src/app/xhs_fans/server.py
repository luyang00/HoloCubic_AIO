from mitmproxy import ctx
import json
import requests
user_profile_url = 'https://edith.xiaohongshu.com/api/sns/v3/user/info?user_id='
request = None



# import requests
# headers={
#     'x-b3-traceid':'0404257dee110e0f',
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36',
#     'xy-common-params': r"deviceId=29cc9550-420e-3d88-8654-784e0e2c1584&identifier_flag=0&tz=Asia%2FShanghai&fid=1651906880109bc8776ed517682ef655758db8402038&app_id=ECFAAF01&device_fingerprint1=202205071501266bded536fe40f70009d94a6ae3ac26db01d1e0c32f309fc5&uis=light&launch_id=1651912129&project_id=ECFAAF&device_fingerprint=202205071501266bded536fe40f70009d94a6ae3ac26db01d1e0c32f309fc5&versionName=6.95.0&platform=android&sid=session.1651907171529043398761&t=1651926662&build=6950211&x_trace_page_current=my_follow_page&lang=zh-Hans&channel=YingYongBao",
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G977N Build/LMY48Z) Resolution/1600*900 Version/6.95.0 Build/6950211 Device/(samsung;SM-G977N) discover/6.95.0 NetType/WiFi',
#     'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AHeeFURaxAzNfjl7NiTJ38/eAKz8N+1MV+2aQ3FAxJGWHdZO72jypljuBZji1Fa3i4rvFROWWNhMGh',
#     'xy-platform-info': 'platform=android&build=6950211&deviceId=29cc9550-420e-3d88-8654-784e0e2c1584',
#     'accept-encoding': 'gzip',
#     "cookie": "MultiDictView[]"
# }
# url='https://edith.xiaohongshu.com/api/sns/v3/user/info?'

# param = {
#     'user_id':'5c164c04000000000602bb85'
# }
# response = requests.get(url=url,params=param,headers=headers) #三个参数
# ctx = response.text
# print(ctx)


def request(flow):
    # 获取请求对象
    request = flow.request
    if user_profile_url in request.url:
        pass
        # # 实例化输出类
        # info = ctx.log.info
        # # 打印请求的url
        # info(request.url)
        # # 打印请求方法
        # info(request.method)
        # # 打印host头
        # info(request.host)
        # # 打印请求端口
        # info(str(request.port))
        # # 打印所有请求头部
        # info(str(request.headers))
        # # 打印cookie头
        # info(request.cookies))


def response(flow):
    response = flow.response
    request_url = flow.request.url
    if user_profile_url not in request_url:
        return
    resp = json.loads(response.text)
    print(resp['data']['imageb'])
    print(resp['data']['desc'])
    print('fans:',resp['data']['interactions'][1]['count'])
    print(resp['data']['note_num_stat'])






    # url = response.url
    # if user_profile_url in request.url:
    #     info(str(response.text))
#     # 获取响应对象
#     response = flow.response
#     # 实例化输出类
#     info = ctx.log.info
#     # 打印响应码
#     info(str(response.status_code))
#     # 打印所有头部
#     info(str(response.headers))
#     # 打印cookie头部
#     info(str(response.cookies))
#     # 打印响应报文内容
#     info(str(response.text))
# headers={
#     'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G977N Build/LMY48Z) Resolution/900*1600 Version/6.95.0 Build/6950211 Device/(samsung;SM-G977N) discover/6.95.0 NetType/WiFi'
# }
# url='https://edith.xiaohongshu.com/api/sns/v3/user/info?user_id=5c164c04000000000602bb85'
