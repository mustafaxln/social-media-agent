# Faz 2 — Workflow 1 Kurulum Notları

**Durum:** Tamamlandı (Faz 3 ile Telegram + Data Table eklendi)

## Kararlar

| Alan | Seçim |
|------|-------|
| Platformlar | LinkedIn, Instagram (her çalıştırmada elle) |
| İçerik türleri | Eğitici, Duyuru, Ürün tanıtımı, Problem/çözüm |
| Hedef kitle | E-ticaret markaları |
| Ton | Profesyonel ve öğretici |
| AI | OpenAI `gpt-4o-mini` |
| Prompt | `prompts/manuel-icerik-prompt.md` |

## Set Node (örnek)

```json
{
  "topic": "E-ticarette yapay zeka kullanımı",
  "platform": "LinkedIn",
  "target_audience": "E-ticaret markaları",
  "tone": "Profesyonel ve öğretici"
}
```

## Final akış (Faz 3 sonrası)

```
Manual Trigger → Set → AI Agent → Code → Insert row → Telegram
```

## AI Agent

- System / User / Structured Output → prompt dosyasındaki 3 bölüm
- Memory: yok | Tool: yok

## Export

`WF-01 Manuel İçerik Üretme.json`

## Tamamlandı

- [x] LinkedIn + Instagram test
- [x] Structured JSON çıktı
- [x] Export
- [x] Ekran görüntüsü → `docs/ekran-goruntuleri/`
