# Checkpoint 3 — WF-04 Onay sonrası görsel (gpt-image-1-mini)

**Durum:** Uygulamada  
**Model:** `gpt-image-1-mini` (en düşük maliyet)  
**Kural:** Sadece **approved** → görsel. **rejected** → status güncelle, dur.

## Hedef akış (WF-04)

```
Telegram Trigger
  → Callback Parse (Code)
  → IF / Switch (action)
       │
       ├─ rejected → Update status=rejected → DUR
       │
       └─ approved → Update status=approved
                   → Get row (içerik + visual_idea)
                   → OpenAI Image (mini)
                   → (ileride: LinkedIn/IG publish)
```
