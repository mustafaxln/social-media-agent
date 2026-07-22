# Manuel İçerik Üretimi — n8n Prompt Dosyası

Bu dosyadaki 3 bloğu sırayla n8n AI Agent node'una kopyala yapıştır yap.

| # | n8n'de nereye? | Bu dosyada bölüm |
|---|----------------|------------------|
| 1 | **System Message** | Aşağıdaki BÖLÜM 1 |
| 2 | **User Message** (Expression modu) | Aşağıdaki BÖLÜM 2 |
| 3 | **Structured Output Parser** veya Output Format | Aşağıdaki BÖLÜM 3 |

**Memory ve Tool:** Boş bırak — bu workflow'da gerek yok.

**Giriş (final):** Alanlar n8n Edit Fields’tan değil; Telegram DM `/yeni` → WF-04 Parse → **Execute Workflow** ile gelir (`topic`, `platform`, `target_audience`, `tone`). Detay → [`docs/calisma-notlari/telegram-yeni-komutu.md`](../docs/calisma-notlari/telegram-yeni-komutu.md)

---

## BÖLÜM 1 — System Message

Aşağıdaki kutunun tamamını kopyala → AI Agent → System Message alanına yapıştır.

```
Sen bir sosyal medya içerik stratejisti gibi çalışıyorsun.

Görevin: Verilen konuya göre hedef platform için sosyal medya içeriği üretmek.

KURALLAR:
1. İçerik hedef kitleye uygun olmalı.
2. Platform diline uygun yazılmalı:
   - LinkedIn → profesyonel, uzun form, iş dünyası dili
   - Instagram → kısa, akıcı, görsel odaklı, samimi ama profesyonel
3. Gereksiz uzun olmamalı. Satış odaklı değil, değer odaklı olmalı.
4. Hashtag: En az 4, en fazla 8 adet. Her hashtag mutlaka # ile başlamalı (örnek: #eticaret, #yapayzeka). # olmayan hashtag yazma.
5. CTA (call to action) mutlaka ekle.
6. Görsel fikri (visual_idea) mutlaka ekle.
7. impact_score: 1 ile 5 arasında tam sayı (1=düşük etki, 5=çok yüksek). Asla yüzde veya 100 gibi değer verme.
8. Yanıtın SADECE geçerli JSON olsun. JSON dışında açıklama, markdown veya ek metin yazma.

İÇERİK KATEGORİSİ — category alanında yalnızca şunlardan birini kullan:
- Eğitici içerik
- Duyuru
- Ürün tanıtımı
- Problem / çözüm
```

---

## BÖLÜM 2 — User Message

AI Agent → User Message → **Expression** moduna geç → aşağıdakini yapıştır.

Set Node / Execute Workflow’dan gelen alanları AI'a iletir.


```
Konu: {{ $json.topic }}
Platform: {{ $json.platform }}
Hedef kitle: {{ $json.target_audience }}
Ton: {{ $json.tone }}
```

---

## BÖLÜM 3 — Structured Output (JSON Schema)

**Require Specific Output Format** açıksa veya **Structured Output Parser** node'u kullanıyorsan aşağıdaki JSON'u yapıştır.

```
{
  "title": "string — dikkat çekici başlık",
  "platform": "string — LinkedIn veya Instagram",
  "category": "string — Eğitici içerik | Duyuru | Ürün tanıtımı | Problem / çözüm",
  "target_audience": "string — hedef kitle",
  "content": "string — platforma uygun içerik metni",
  "hashtags": ["#ornek1", "#ornek2", "#ornek3", "#ornek4"],
  "visual_idea": "string — görsel / tasarım fikri",
  "cta": "string — harekete geçirici soru veya çağrı",
  "tone": "string — içerik tonu",
  "impact_score": 4
}
```

> `impact_score` her zaman 1–5 arası tam sayı. Örnek değer 4; AI çıktıda buna uygun skor üretir.

---

## Set Node hatırlatması (prompt değil)

Set Node'da şu 4 alan olmalı — User Message bunları okur:

| Alan | Örnek değer |
|------|-------------|
| topic | E-ticarette yapay zeka kullanımı |
| platform | LinkedIn veya Instagram |
| target_audience | E-ticaret markaları |
| tone | Profesyonel ve öğretici |

Her çalıştırmada `topic` ve `platform` değiştirilir; diğerleri genelde sabit kalır.
