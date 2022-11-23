from flask import Flask
from flask import render_template
from flask import redirect
from flask import request


app = Flask(__name__)

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


i_jpy = 100


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/measurement", methods=["GET", "POST"])
def fx_currency():
    if request.method == "POST":
        currency = request.form["currency1"]
        if currency == "JPY":
            # i_jpy = int(request.form["number"])
            usd1 = (i_jpy * 0.44) / usd
            eur1 = (i_jpy * 0.155) / eur
            gbp1 = (i_jpy * 0.085) / gbp
            cny1 = (i_jpy * 0.065) / cny
            aud1 = (i_jpy * 0.035) / aud
            etc1 = (i_jpy * 0.19) / wc
            jpy_wc = [usd1, eur1, gbp1, cny1, aud1, etc1]
            print(jpy_wc)
            print(request.form["number"])
            fx_currency = jpy_wc

        # elif currency == "USD":
        #     fx_currency = fx_currency.USD()

        # elif currency == "EUR":
        #     fx_currency = fx_currency.EUR()

        # elif currency == "GBP":
        #     fx_currency = fx_currency.GBP()

        # elif currency == "CNY":
        #     fx_currency = fx_currency.CNY()

        # elif currency == "AUD":
        #     fx_currency = fx_currency.AUD()

        return render_template("measurement.html", fx_currency=fx_currency)

    return redirect("/")


@app.route("/measurement", methods=["POST"])
def measurement():
    currency = request.form["currency1"]
    return render_template("measurement.html", currency=currency)


if __name__ == "__main__":
    app.run(debug=True)
