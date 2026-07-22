#!/usr/bin/env python3
"""Tanıtım PDF — teknik olmayan, pazarlama odaklı."""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "docs" / "ekran-goruntuleri"
OUT = ROOT / "Sosyal-Medya-Icerik-Ajani-Tanitim.pdf"
TOTAL = 9

pdfmetrics.registerFont(TTFont("A", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("AB", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))

W, H = A4
NAVY = HexColor("#0F2744")
TEAL = HexColor("#1A7A6D")
SAND = HexColor("#F7F5F1")
INK = HexColor("#1C1C1C")
MUTED = HexColor("#5A5A5A")
LINE = HexColor("#D8D4CC")
MINT = HexColor("#7DFFCE")
SOFT = HexColor("#C5D0DE")


def wrap(c, text, font, size, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(c, text, x, y, font, size, max_w, leading, color=INK):
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrap(c, text, font, size, max_w):
        c.drawString(x, y, line)
        y -= leading
    return y


def sand_bg(c):
    c.setFillColor(SAND)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def header_bar(c, title):
    c.setFillColor(NAVY)
    c.rect(0, H - 18 * mm, W, 18 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("AB", 11)
    c.drawString(18 * mm, H - 11 * mm, title)
    c.setFillColor(TEAL)
    c.rect(0, H - 19.5 * mm, W, 1.5 * mm, fill=1, stroke=0)


def footer(c, page):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(18 * mm, 12 * mm, W - 18 * mm, 12 * mm)
    c.setFillColor(MUTED)
    c.setFont("A", 8)
    c.drawString(18 * mm, 7 * mm, "Sosyal Medya İçerik Ajansı")
    c.drawRightString(W - 18 * mm, 7 * mm, f"{page} / {TOTAL}")


def content_page(c, title, page):
    sand_bg(c)
    header_bar(c, title)
    footer(c, page)
    return H - 30 * mm


def fit_image(path, max_w, max_h):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return ImageReader(im), w * scale, h * scale


def place_shot(c, filename, caption, y, max_h):
    path = IMG / filename
    max_w = W - 36 * mm
    img, iw, ih = fit_image(path, max_w, max_h)
    x = (W - iw) / 2
    pad = 2 * mm
    c.setFillColor(white)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.roundRect(x - pad, y - ih - pad, iw + 2 * pad, ih + 2 * pad, 3, fill=1, stroke=1)
    c.drawImage(img, x, y - ih, width=iw, height=ih, mask="auto")
    y = y - ih - 5 * mm
    y = draw_wrapped(c, caption, 18 * mm, y, "A", 9, max_w, 12, MUTED)
    return y - 3 * mm


def build():
    c = canvas.Canvas(str(OUT), pagesize=A4)

    # 1 Kapak
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, H * 0.36, W, 7 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("AB", 28)
    c.drawString(22 * mm, H - 58 * mm, "Sosyal Medya")
    c.drawString(22 * mm, H - 72 * mm, "İçerik Ajansı")
    c.setFont("A", 12.5)
    c.drawString(22 * mm, H - 88 * mm, "Telegram’dan onaylayın, yapay zekâ üretsin,")
    c.drawString(22 * mm, H - 96 * mm, "LinkedIn ve Instagram’da yayınlansın.")
    c.setFillColor(SOFT)
    c.setFont("A", 10)
    c.drawString(22 * mm, 30 * mm, "Tanıtım dokümanı  ·  Temmuz 2026")
    c.drawString(22 * mm, 23 * mm, "E-ticaret markaları için otomatik içerik asistanı")
    c.showPage()

    # 2 Sorun & çözüm
    y = content_page(c, "Neden bu proje?", 2)
    y = draw_wrapped(
        c,
        "Sosyal medyada düzenli ve kaliteli içerik üretmek zaman alır. Konu bulmak, metin yazmak, görsel hazırlamak ve doğru platformda paylaşmak — çoğu ekip için yorucu bir döngüdür.",
        18 * mm, y, "A", 11, W - 36 * mm, 16,
    )
    y -= 7 * mm
    box_h = 46 * mm
    c.setFillColor(white)
    c.setStrokeColor(LINE)
    c.roundRect(18 * mm, y - box_h, W - 36 * mm, box_h, 4, fill=1, stroke=1)
    c.setFillColor(TEAL)
    c.setFont("AB", 11)
    c.drawString(24 * mm, y - 9 * mm, "Klasik süreçte ne zor?")
    c.setFillColor(INK)
    c.setFont("A", 10)
    by = y - 18 * mm
    for b in [
        "Her gün konu ve haber takibi",
        "Platforma uygun metin yazmak (LinkedIn ≠ Instagram)",
        "Görsel üretmek veya tasarım beklemek",
        "Yayınlamadan önce ekip içi onay",
    ]:
        c.circle(27 * mm, by + 2, 1.2, fill=1, stroke=0)
        c.drawString(32 * mm, by, b)
        by -= 6.5 * mm
    y -= box_h + 8 * mm

    c.setFillColor(NAVY)
    c.setFont("AB", 12)
    c.drawString(18 * mm, y, "Çözümümüz")
    y -= 7 * mm
    y = draw_wrapped(
        c,
        "Social Media Agent sizin için içerik fikri üretir, metni yazar, görseli oluşturur ve onayınızla LinkedIn veya Instagram’da yayınlar. Siz yalnızca Telegram’dan bakıp Onayla veya Yayınla demeniz yeterli.",
        18 * mm, y, "A", 11, W - 36 * mm, 16,
    )
    y -= 10 * mm
    box_w = (W - 42 * mm) / 3
    labels = [
        ("Üret", "Konu veya gündem haberinden hazır post taslağı"),
        ("Onayla", "Telegram’da iki adım: önce taslak, sonra görsel"),
        ("Yayınla", "Tek tuşla LinkedIn veya Instagram’a gönder"),
    ]
    for i, (t, d) in enumerate(labels):
        x = 18 * mm + i * (box_w + 3 * mm)
        c.setFillColor(NAVY if i != 1 else TEAL)
        c.roundRect(x, y - 40 * mm, box_w, 40 * mm, 4, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("AB", 12)
        c.drawString(x + 4 * mm, y - 11 * mm, t)
        c.setFont("A", 8.5)
        dy = y - 20 * mm
        for line in wrap(c, d, "A", 8.5, box_w - 8 * mm):
            c.drawString(x + 4 * mm, dy, line)
            dy -= 11
    c.showPage()

    # 3 İki yol
    y = content_page(c, "İki kullanım yolu", 3)
    y = draw_wrapped(
        c,
        "Sistem iki şekilde çalışır. İkisinde de son söz sizde: beğenmediğiniz hiçbir şey yayınlanmaz.",
        18 * mm, y, "A", 11, W - 36 * mm, 16,
    )
    y -= 8 * mm

    def path_card(title, points, accent):
        nonlocal y
        h = 58 * mm
        c.setFillColor(white)
        c.setStrokeColor(LINE)
        c.roundRect(18 * mm, y - h, W - 36 * mm, h, 4, fill=1, stroke=1)
        c.setFillColor(accent)
        c.rect(18 * mm, y - h, 3 * mm, h, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("AB", 12)
        c.drawString(26 * mm, y - 10 * mm, title)
        c.setFillColor(INK)
        c.setFont("A", 10)
        my = y - 20 * mm
        for m in points:
            for line in wrap(c, "•  " + m, "A", 10, W - 52 * mm):
                c.drawString(26 * mm, my, line)
                my -= 12
            my -= 1
        y -= h + 7 * mm

    path_card(
        "1) Manuel — Siz konuyu söylersiniz",
        [
            "Telegram’da bota özelden kısa bir form yazarsınız: platform, konu, hedef kitle, ton.",
            "Birkaç saniye içinde grupta hazır bir post taslağı gelir.",
            "Beğenirseniz Onayla → görsel üretilir → Yayınla ile ilgili platforma gider.",
        ],
        TEAL,
    )
    path_card(
        "2) Otomatik — Agent gündemi tarar",
        [
            "Her gün internetteki güncel haberlerden konu seçer ve taslak hazırlar.",
            "LinkedIn veya Instagram diline uygun metin üretir.",
            "Aynı onay akışı: Onayla → görsel → Yayınla. İstemediğinizi Reddet veya İptal edin.",
        ],
        NAVY,
    )
    c.showPage()

    # 4 Faydalar + maliyet
    y = content_page(c, "Ne kazandırır?", 4)
    for title, desc in [
        ("Zaman", "Metin ve görsel hazırlığı dakikalara iner; siz yalnızca karar verirsiniz."),
        ("Kontrol", "İki kademeli onay: önce metin, sonra görsel. İstemediğiniz hiçbir şey yayınlanmaz."),
        ("Tutarlılık", "LinkedIn ve Instagram diline uygun, e-ticaret odaklı profesyonel ton."),
        ("Gündem", "Otomatik hat, güncel haberlerden ilham alan taslaklar üretir."),
        ("Basit arayüz", "Günlük kullanım Telegram üzerinden; karmaşık panellerle uğraşmazsınız."),
    ]:
        c.setFillColor(TEAL)
        c.circle(22 * mm, y - 2, 2.2, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("AB", 11)
        c.drawString(28 * mm, y - 4, title)
        y -= 8 * mm
        y = draw_wrapped(c, desc, 28 * mm, y, "A", 10, W - 50 * mm, 14)
        y -= 5 * mm

    y -= 2 * mm
    c.setFillColor(NAVY)
    c.roundRect(18 * mm, y - 50 * mm, W - 36 * mm, 50 * mm, 5, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("AB", 13)
    c.drawString(26 * mm, y - 12 * mm, "Maliyet")
    c.setFont("A", 11)
    c.drawString(26 * mm, y - 24 * mm, "Onaylanıp görseli üretilen bir post için yaklaşık")
    c.setFont("AB", 20)
    c.setFillColor(MINT)
    c.drawString(26 * mm, y - 36 * mm, "0,02 – 0,03 USD")
    c.setFillColor(SOFT)
    c.setFont("A", 9)
    c.drawString(26 * mm, y - 45 * mm, "Metin + görsel yapay zekâ kullanımı (gözlem, Temmuz 2026). Reddedilen taslaklarda görsel maliyeti oluşmaz.")
    c.showPage()

    # 5 Kim için
    y = content_page(c, "Kimler için?", 5)
    y = draw_wrapped(
        c,
        "Özellikle e-ticaret markaları ve bu markalara içerik üreten ekipler için tasarlandı. Profesyonel ve öğretici bir dil hedeflenir; satış baskısından çok değer ve bilgilendirme odaklıdır.",
        18 * mm, y, "A", 11, W - 36 * mm, 16,
    )
    y -= 10 * mm
    c.setFillColor(NAVY)
    c.setFont("AB", 12)
    c.drawString(18 * mm, y, "Kısaca vaat")
    y -= 8 * mm
    y = draw_wrapped(
        c,
        "Daha az eforla, daha düzenli sosyal medya varlığı. İnsan onayını merkezde tutan, uygun maliyetli bir içerik asistanı.",
        18 * mm, y, "A", 11, W - 36 * mm, 16,
    )
    y -= 14 * mm
    c.setFillColor(white)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.4)
    c.roundRect(18 * mm, y - 52 * mm, W - 36 * mm, 52 * mm, 4, fill=1, stroke=1)
    c.setFillColor(TEAL)
    c.setFont("AB", 11)
    c.drawString(26 * mm, y - 12 * mm, "Sonraki sayfalarda gerçek örnekler")
    c.setFillColor(INK)
    c.setFont("A", 10)
    c.drawString(26 * mm, y - 25 * mm, "1–4    Manuel yol: konudan Instagram yayınına")
    c.drawString(26 * mm, y - 35 * mm, "5–7    Otomatik yol: gündem haberinden LinkedIn yayınına")
    c.setFillColor(MUTED)
    c.setFont("A", 9)
    c.drawString(26 * mm, y - 46 * mm, "Ekran görüntüleri gerçek sistem çıktılarından alınmıştır.")
    c.showPage()

    # 6 Manuel 1-2
    y = content_page(c, "Örnek: Manuel içerik", 6)
    c.setFillColor(TEAL)
    c.setFont("AB", 10)
    c.drawString(18 * mm, y, "Yol A — Siz konuyu verirsiniz")
    y -= 6 * mm
    y = place_shot(
        c,
        "1.png",
        "Adım 1 — İstek: Bota özelden hangi platformda, hangi konuda, kime ve hangi tonda post istediğimizi yazarız.",
        y,
        72 * mm,
    )
    y = place_shot(
        c,
        "2.png",
        "Adım 2 — Taslak: Hazır post taslağı grupta belirir. Beğenirsek Onayla, beğenmezsek Reddet.",
        y,
        72 * mm,
    )
    c.showPage()

    # 7 Manuel 3-4
    y = content_page(c, "Örnek: Manuel içerik (devam)", 7)
    y = place_shot(
        c,
        "3.png",
        "Adım 3 — Görsel + final: Onaydan sonra konuyla uyumlu görsel üretilir; Yayınla veya İptal ile karar verilir.",
        y,
        72 * mm,
    )
    y = place_shot(
        c,
        "4.png",
        "Adım 4 — Yayın: Post, seçilen platformda (bu örnekte Instagram) canlıya alınmış hali.",
        y,
        72 * mm,
    )
    c.showPage()

    # 8 Otomatik 5-6
    y = content_page(c, "Örnek: Otomatik (gündem)", 8)
    c.setFillColor(NAVY)
    c.setFont("AB", 10)
    c.drawString(18 * mm, y, "Yol B — Agent haberlerden taslak üretir")
    y -= 6 * mm
    y = place_shot(
        c,
        "5.png",
        "Adım 1 — Agent, internetteki güncel bir haberi işleyip LinkedIn taslağı önerir. Onayla / Reddet yine sizin elinizde.",
        y,
        72 * mm,
    )
    y = place_shot(
        c,
        "6.png",
        "Adım 2 — Onay sonrası görsel ve final post. Yayınla ile platforma gider, İptal ile durur.",
        y,
        72 * mm,
    )
    c.showPage()

    # 9 Otomatik 7 + kapanış
    y = content_page(c, "Örnek: Otomatik yayın", 9)
    y = place_shot(
        c,
        "7.png",
        "Adım 3 — Yayın: Post, seçilen platformda (bu örnekte LinkedIn) canlıya alınmış hali.",
        y,
        95 * mm,
    )
    y -= 4 * mm
    c.setFillColor(NAVY)
    c.roundRect(18 * mm, 20 * mm, W - 36 * mm, 28 * mm, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("AB", 11)
    c.drawString(26 * mm, 36 * mm, "Özet")
    c.setFont("A", 9.5)
    c.drawString(26 * mm, 28 * mm, "Üret → Onayla → Yayınla. İnsan kontrolünde, uygun maliyetle, LinkedIn & Instagram.")
    c.setFillColor(MINT)
    c.setFont("AB", 9)
    c.drawString(26 * mm, 22 * mm, "Post başına yaklaşık 0,02 – 0,03 USD")

    c.save()
    print(f"OK → {OUT}")


if __name__ == "__main__":
    build()
