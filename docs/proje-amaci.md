# Proje Amacı

Belirlenen kaynaklardan sosyal medya içerik fikirleri üretmek ve AI agent ile platforma uygun sosyal medya formatına dönüştürmek.

## Problem

Sosyal medya içerik üretimi zaman alıcı ve tutarsız olabiliyor. Markalar ve ekipler:

- Güncel kaynaklardan içerik fikri bulmakta zorlanıyor
- Platform bazlı format farklarını (LinkedIn vs Instagram) manuel yönetiyor
- Üretilen içerikleri merkezi bir yerde takip edemiyor
- Onay süreci dağınık (WhatsApp, e-posta, not defteri)

## Çözüm

n8n tabanlı otomasyon:

1. Manuel veya RSS kaynağından içerik fikri al
2. AI agent ile LinkedIn / Instagram içeriği üret
3. Data Table'a kaydet (`waiting_approval`)
4. Telegram'a taslak gönder → insan onaylar
5. Hata olursa WF-03 kaydeder ve bildirir

## Somut hedefler — durum

| Hedef | Durum |
|-------|--------|
| Manuel konu ile LinkedIn + Instagram içerik | ✅ WF-01 |
| RSS'ten otomatik çekip dönüştürmek | ✅ WF-02 (Webrazzi) |
| Merkezi tabloda takip | ✅ `social_media_contents` |
| Telegram taslak + onay başlangıcı | ✅ Grup bildirimi |
| Hata durumunda sistemin kayıpsız yakalaması | ✅ WF-03 + Retry |

## Seçilen platformlar

**LinkedIn** ve **Instagram**

| | WF-01 | WF-02 |
|--|-------|-------|
| Platform seçimi | Set node'da elle | AI içeriğe göre |

## Hedef kitle ve ton

- Hedef kitle: E-ticaret markaları / online satıcılar
- Ton: Profesyonel ve öğretici

## İlk versiyon kapsamı

- [x] Docker ile local n8n
- [x] 3 workflow (manuel, kaynak, error)
- [x] Data Table içerik + hata kaydı
- [x] Telegram taslak + HATA
- [x] Manuel onay (Telegram okuma)
- [x] Duplicate (`source_url`)
- [x] Retry On Fail
- [x] Schedule Trigger (WF-02)
- [ ] execution_logs insert *(PM sonrası)*
- [ ] Ağır fallback *(PM sonrası)*

## Sonradan eklenebilecek özellikler

- İçerik takvimi, rakip analizi, brand voice
- Görsel brief / AI image prompt
- Multi-agent (research, writer, editor)
- Telegram butonlu onay, Form, Sheet
- Schedule ile periyodik WF-02
