from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from fx_day_rate import df
from wc_propo import df3

# flaskで画像を使う場合は画像ファイルは静的なファイルなのでディレクトリを記述して，インスタンス化
app = Flask(__name__, static_folder="./templates/images")


# みずほ銀行のHPからスクレーパーにより抽出
usd = float(df.iloc[-1, 1])
eur = float(df.iloc[-1, 3])
jpy = 1
gbp = float(df.iloc[-1, 2])
cny = float(df.iloc[-1, 14])
aud = float(df.iloc[-1, 9])
cad = float(df.iloc[-1, 4])
chf = float(df.iloc[-1, 5])
hkd = float(df.iloc[-1, 15])

l_currency = [usd, eur, gbp, cny, aud, cad, chf, hkd]

# 世界通貨シェアを200で割って％として数値を作成
p_usd = (df3.iloc[-1, 0]) / 200
p_eur = (df3.iloc[-1, 1]) / 200
p_jpy = (df3.iloc[-1, 2]) / 200
p_gbp = (df3.iloc[-1, 3]) / 200
p_cny = (df3.iloc[-1, 4]) / 200
p_aud = (df3.iloc[-1, 5]) / 200
p_cad = (df3.iloc[-1, 6]) / 200
p_chf = (df3.iloc[-1, 7]) / 200
p_hkd = (df3.iloc[-1, 8]) / 200
p_etc = (df3.iloc[-1, 9]) / 200

# グラフを描写するために割合をリストにしてwc_pie_cahartへ渡しています
p_wc = [p_usd, p_eur, p_jpy, p_gbp, p_cny, p_aud, p_cad, p_chf, p_hkd, p_etc]

# その他を計算する単位を作る為、取り出した通貨の最小単位を合計して100で割る
wc_min = (
    float(usd)
    + float(eur)
    + float(usd)
    + float(gbp)
    + float(cny)
    + float(aud)
    + float(cad)
    + float(chf)
    + float(hkd)
)
wc_min = wc_min / 9

# 更に通貨シェアを掛けた数値をwcとする。
wc = (
    (p_usd * float(usd))
    + (p_eur * float(eur))
    + (p_jpy * float(usd))
    + (p_gbp * float(gbp))
    + (p_cny * float(cny))
    + (p_aud * float(aud))
    + (p_cad * float(cad))
    + (p_chf * float(chf))
    + (p_hkd * float(hkd))
    + (p_etc * float(wc_min))
)

# wcを考え直し、令和4年11月22日の10円を、FXレートと世界シェアで1wcとして決める
# 計算すると「0.9375038685614582」だったので切りよく11月22日の10円が1wcとする
# 1wcの内訳は「0.039403321137067265, 0.010636837771067801, 0.8500000000000001, 0.0038605452277721683, 0.017658930373360245, 0.0031904711262363073, 0.0028360748723766306, 0.001684976747320887, 0.00823271130625686]

b_usd = (10 * p_usd) / 142.12
b_eur = (10 * p_eur) / 145.72
b_jpy = (10 * p_jpy) / 1
b_gbp = (10 * p_gbp) / 168.37
b_cny = (10 * p_cny) / 19.82
b_aud = (10 * p_aud) / 94.03
b_cad = (10 * p_cad) / 105.78
b_chf = (10 * p_chf) / 148.37
b_hkd = (10 * p_hkd) / 18.22
b_etc = (10 * p_etc) / 142.12

# その他分のシェアはドルのシェアに合計しておく
b_usd = b_usd + b_etc
# 各通貨のバラバラな単位なので、当日のレートを掛け、円に戻して合計する
b_wc = (
    (b_usd * usd)
    + (b_eur * eur)
    + b_jpy
    + (b_gbp * gbp)
    + (b_cny * cny)
    + (b_aud * aud)
    + (b_cad * cad)
    + (b_chf * chf)
    + (b_hkd * hkd)
)

b_wc_list = [b_usd, b_eur, b_jpy, b_gbp, b_cny, b_aud, b_cad, b_chf, b_hkd]

# トップページへ
@app.route("/")
def index():
    return render_template("index.html")


# 円が選択され数値が入力された時
@app.route("/measurement", methods=["GET", "POST"])
def fx_currency():
    if request.method == "POST":
        currency = request.form["currency1"]
        if currency == "JPY":
            i_jpy = int(request.form["number"])
            usd1 = (i_jpy * p_usd) / usd
            eur1 = (i_jpy * p_eur) / eur
            jpy1 = (i_jpy * p_jpy) / jpy
            gbp1 = (i_jpy * p_gbp) / gbp
            cny1 = (i_jpy * p_cny) / cny
            aud1 = (i_jpy * p_aud) / aud
            gbp1 = (i_jpy * p_gbp) / gbp
            cad1 = (i_jpy * p_cad) / cad
            chf1 = (i_jpy * p_chf) / chf
            hkd1 = (i_jpy * p_hkd) / hkd
            etc1 = (i_jpy * p_etc) / wc

            # 入力された金額をwcの基準価格で割りwc建ての価値を出す
            wcjpn = i_jpy / b_wc

            jpy_wc = [
                round(usd1),
                round(eur1),
                round(jpy1),
                round(gbp1),
                round(cny1),
                round(aud1),
                round(cad1),
                round(chf1),
                round(hkd1),
                round(etc1),
                round(wcjpn),
            ]
            print(b_wc_list)
            print(wcjpn)
            # print(df.iloc[-1, 1])
            fx_currency = jpy_wc

        # elif currency == "USD":
        #     fx_currency = fx_currency.USD()

        return render_template(
            "measurement.html",
            fx_currency=fx_currency,
            i_jpy=i_jpy,
            currency=currency,
            l_currency=l_currency,
            # usd=usd,
            # eur=eur,
            # gbp=gbp,
            # cny=cny,
            # aud=aud,
            # cad=cad,
            # chf=chf,
            # hkd=hkd,
            # wcjpn=wcjpn,
            b_wc_list=b_wc_list,
        )

    return redirect("/")


# 通貨シェアと為替レートを考慮して結果を円グラフと数値で表示する
@app.route("/measurement", methods=["POST"])
def measurement():
    currency = request.form["currency1"]
    return render_template("measurement.html", currency=currency)


if __name__ == "__main__":
    app.run(debug=True)
