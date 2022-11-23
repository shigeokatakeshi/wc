import json
import requests

# 今は手入力だがBISのHPからスクレーパーにより抽出予定
usd = 140
eur = 145
jpy = 100
gbp = 168
cny = 20
aud = 93

# 取り出した通貨の最小単位を合計して100で割る
wc = usd + eur + jpy + gbp + cny + aud
wc = wc / 100

# 更に通貨シェアを掛けた数値をwcとする,とりあえずその他の19％はwcで出す。
wc = (
    (0.44 * usd)
    + (0.155 * eur)
    + (0.085 * jpy)
    + (0.065 * gbp)
    + (0.035 * cny)
    + (0.03 * aud)
    + (0.19 * wc)
)

i_jpy = 1000000


def JPY():
    usd = usd * i_jpy * 0.44
    eur = eur * i_jpy * 0.155
    gbp = gbp * i_jpy * 0.085
    cny = cny * i_jpy * 0.065
    aud = aud * i_jpy * 0.035
    etc = wc * i_jpy * 0.19

    response = [usd, eur, gbp, cny, aud, etc]

    return response


def dog():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    response = json.loads(res.text)["message"]
    return response


def fox():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    response = json.loads(res.text)["message"]
    return response
