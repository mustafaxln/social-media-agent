# Faz 2 — Workflow 1 Kurulum Notları

## Kararlar

| Alan | Seçim |
|------|-------|
| Platformlar | LinkedIn, Instagram (her çalıştırmada elle seçilir) |
| İçerik türleri | Eğitici, Duyuru, Ürün tanıtımı, Problem/çözüm |
| Hedef kitle | E-ticaret markaları / online satıcılar |
| Ton | Profesyonel ve öğretici |
| AI | OpenAI (API key n8n credential olarak) |

## Set Node alanları

```json
{
  "topic": "E-ticarette yapay zeka kullanımı",
  "platform": "LinkedIn",
  "target_audience": "E-ticaret markaları",
  "tone": "Profesyonel ve öğretici"
}
```

`platform` her çalıştırmada `LinkedIn` veya `Instagram` olarak değiştirilir.

## n8n kurulum adımları

1. n8n → **Credentials** → **OpenAI** ekle (API key)
2. Yeni workflow oluştur: `WF-01 Manuel İçerik Üretme`
3. Node'ları sırayla ekle:

### 1. Manual Trigger

### 2. Set Node

Fields to Set → Manual Mapping:

| Name | Value |
|------|-------|
| topic | `E-ticarette yapay zeka kullanımı` (test için; sonra değiştir) |
| platform | `LinkedIn` |
| target_audience | `E-ticaret markaları` |
| tone | `Profesyonel ve öğretici` |

### 3. AI Agent

- Chat Model: **OpenAI Chat Model** (credential bağla)
- System Message: `prompts/manuel-icerik-prompt.md` içeriğini kopyala
- User Message:

```
Konu: {{ $json.topic }}
Platform: {{ $json.platform }}
Hedef kitle: {{ $json.target_audience }}
Ton: {{ $json.tone }}
```

- **Require Specific Output Format** → açık
- Output format: JSON schema veya Structured Output Parser kullan

### 4. Structured Output Parser (AI Agent'a bağlı)

Schema örneği — `prompts/manuel-icerik-prompt.md` altındaki JSON alanları.

## Test

1. Set Node'da konu ve platformu gir
2. **Execute workflow** çalıştır
3. Çıktıda title, content, hashtags, visual_idea, cta, impact_score gelmeli

## Tamamlandığında

- [x] Workflow test edildi (LinkedIn + Instagram)
- [x] JSON export alındı → `WF-01 Manuel İçerik Üretme.json`
- [x] Ekran görüntüsü → `docs/ekran-goruntuleri/`
