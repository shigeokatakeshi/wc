import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

from wc import p_wc

# plt.rcParams['font.family'] = "MS Gothic"


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

# plt.pie(X)

# plt.pie(x, labels=["", "", "", "", "", "", "", "", "", ""])
explode = [0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0]
wedgeprops = {"alpha": 0.8, "edgecolor": "white", "linewidth": 2}
plt.pie(
    x,
    labels=labels,
    autopct="%.f%%",
    startangle=90,
    counterclock=False,
    explode=explode,
    wedgeprops=wedgeprops
)
# plt.legend()
plt.title("世界為替市場の通貨割合")
# plt.show()
plt.savefig("templates/images/image.png")
