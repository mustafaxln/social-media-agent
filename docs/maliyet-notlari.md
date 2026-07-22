# Maliyet Notları

> Tahmini birim maliyet (Temmuz 2026 gözlemi). API fiyatları değişebilir.

## Post başına maliyet

| Kalem | Açıklama |
|--------|----------|
| **Tahmini toplam** | **yaklaşık 0,02 – 0,03 USD / post** |
| Metin (gpt-4o-mini) | Kısa prompt + structured JSON |
| Görsel (gpt-image-1-mini) | Onay sonrası 1 görsel |
| Diğer | Cloudinary / Buffer / Telegram — pratikte ihmal edilebilir veya ücretsiz kotada |

Bu rakam **onaylanıp görseli üretilen** bir post için tipik gözlemdir. Reddedilen taslaklarda görsel üretilmez; maliyet daha düşük kalır.

## Ne dahil, ne değil?

| Dahil (değişken) | Hariç / sabit |
|------------------|----------------|
| OpenAI metin + görsel API | n8n self-hosted (Docker, local) |
| | Bilgisayar / elektrik |
| | Buffer Free plan kotası |
| | Cloudflare quick tunnel (ücretsiz) |

## Karşılaştırma (iş değeri)

- Ajans veya freelancer ile tek post üretimi genelde çok daha pahalıdır (zaman + ücret).  
- Bu sistemde insan yalnızca **Telegram’dan onay** verir; yazım ve görsel otomatiktir.  
- Günlük RSS taslağı + ihtiyaç halinde `/yeni` ile manuel konu → aynı düşük birim maliyet.

## Not

Kesin fatura için OpenAI kullanım panosuna bakılmalıdır. Bu dokümandaki aralık **yönlendirici**dir; model veya görsel kalitesi değişirse maliyet artabilir.
