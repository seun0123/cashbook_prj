from django.shortcuts import render
import requests, json, base64, time


# Create your views here.
def window(request):
    return render(request,'window.html',)

def success(request):
    orderId = request.GET.get('orderId')
    amount = request.GET.get('amount')
    paymentKey = request.GET.get('paymentKey')

    url = "https://api.tosspayments.com/v1/payments/confirm"
    secretKey="test_sk_dP9BRQmyarYg2LEbM4Z3J07KzLNk"
    userpass = secretKey + ':'
    encoded_u = base64.b64encode(userpass.encode()).decode()

    headers = {
        "Authorization" : "Basic %s" % encoded_u,
        "Content-Type" : "application/json"
    }

    params = {
        "orderId" : orderId,
        "amount" : amount,
        "paymentKey" : paymentKey,
    }

    res = requests.post(url, data=json.dumps(params), headers=headers)
    resjson = res.json()
    pretty = json.dumps(resjson, indent=4)
    respaymentKey = resjson["paymentKey"]
    resorderId = resjson["orderId"]
    return render(request, "success.html",
    {
        "res" : pretty,
        "respaymentKey" : respaymentKey,
        "resorderId" : resorderId,
    }
    )

def fail(request):
    code = request.GET.get('code')
    message = request.GET.get('message')

    return render(request, "fail.html",
    {
        "code" : code,
        "message" : message,
        }
    )