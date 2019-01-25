import urllib
import urllib3
import json
import sys

def DNN_judge(text):
    http = urllib3.PoolManager()
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn?access_token=24.622919d482aad3d8ff925c11144238bf.2592000.1550716334.282335-11177554"
    data = {"text":text}
    encode_data = json.dumps(data).encode('GBK')
    # JSON:在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据：
    request = http.request('POST',
                           url,
                           body=encode_data,
                           headers={'Content-Type': 'application/json'}
                           )
    result = str(request.data, 'GBK')
    return result
