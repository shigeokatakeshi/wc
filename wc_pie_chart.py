import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import japanize_matplotlib
from PIL import Image


# リサイズ前の画像を読み込み

# 読み込んだ画像の幅、高さを取得し半分に
# 画像をリサイズする
# ファイルを保存


# これが無いとdef内で上手く動かない
matplotlib.use("Agg")

# def関数にしてwc.py内で動かす
def fx_chart(currency, p_wc):

    # これが無いと画像が二重に生成される
    plt.figure()
    if currency == "円":
        explode = [0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0]
    if currency == "ドル":
        explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if currency == "ユーロ":
        explode = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]

    wedgeprops = {"alpha": 0.8, "edgecolor": "white", "linewidth": 2}
    p_usd = p_wc[0] * 100
    p_eur = p_wc[1] * 100
    p_jpy = p_wc[2] * 100
    p_gbp = p_wc[3] * 100
    p_cny = p_wc[4] * 100
    p_aud = p_wc[5] * 100
    p_cad = p_wc[6] * 100
    p_chf = p_wc[7] * 100
    p_hkd = p_wc[8] * 100
    p_etc = p_wc[9] * 100

    x = [p_usd, p_eur, p_jpy, p_gbp, p_cny, p_aud, p_cad, p_chf, p_hkd, p_etc]
    labels = [
        "ドル",
        "ユーロ",
        "円",
        "ポンド",
        "中国元",
        "オーストラリアドル",
        "カナダドル",
        "スイスフラン",
        "香港ドル",
        "その他",
    ]
    plt.pie(
        x,
        labels=labels,
        autopct="%.f%%",
        startangle=90,
        counterclock=False,
        explode=explode,
        wedgeprops=wedgeprops,
    )
    # plt.legend()
    plt.title("世界為替市場の通貨割合")
    plt.subplots_adjust(left=0, right=1.1, bottom=0, top=0.95)
    # plt.show()
    # 画像を保存
    plt.savefig("static/images/image.png", dpi=300)

    img_file = "static/images/image.png"
    img = Image.open(img_file)
    (width, height) = (400, 330)
    img_resized = img.resize((width, height))
    img_resized.save("static/images/image.png", quality=400)
