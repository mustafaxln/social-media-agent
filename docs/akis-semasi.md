# Akış Şeması

## Sistem Genel Akışı

```mermaid
flowchart TD
    Y["/yeni DM"] --> H[WF-04 Hub]
    R[WF-02 RSS] --> B[Insert waiting_approval]
    H -->|yeni| W1[WF-01 AI + Insert]
    W1 --> B
    B --> C[Telegram grup Onayla/Reddet]
    C --> D{1. Onay}
    D -->|Reddet| RJ[rejected]
    D -->|Onayla| E[Image + Cloudinary]
    E --> F[FINAL Yayınla/İptal]
    F --> G{2. Onay}
    G -->|İptal| P[preview_rejected]
    G -->|Yayınla| BUF[Buffer LI/IG]
    BUF --> I[published]
    H -->|callback| C
    W1 -.->|Hata| E3[WF-03]
    E -.->|Hata| E3
    BUF -.->|Hata| E3
```

## Workflow 1 — Manuel (`/yeni` → Execute)

```mermaid
flowchart TD
    A[Execute Workflow Trigger] --> C[AI Agent]
    C --> D[Code telegram_message]
    D --> E[Data Table]
    E --> F[Telegram grup buton]
```

## Workflow 2 — Kaynaktan İçerik

```mermaid
flowchart TD
    A[Schedule / Manual] --> B[RSS Read]
    B --> C[Veri Temizle]
    C --> D[Duplicate Kontrol]
    D --> E[Limit 1]
    E --> F[AI Agent]
    F --> G[Code]
    G --> H[Data Table]
    H --> I[Telegram buton]
```

## Workflow 3 — Error Handling

```mermaid
flowchart TD
    A[Error Trigger] --> B[Hata Mesaji Code]
    B --> C[social_media_errors]
    C --> D[Telegram HATA]
```

## Workflow 4 — Telegram Hub

```mermaid
flowchart TD
    A[Telegram Trigger] --> G[Giris Ayir]
    G --> S{route}
    S -->|yeni| P[Parse /yeni]
    P --> E[Execute WF-01]
    S -->|callback| CP[Callback Parse]
    CP --> A2{action}
    A2 -->|reject| R[rejected]
    A2 -->|cancel| C[preview_rejected]
    A2 -->|approve| IM[Image + Cloudinary]
    IM --> F[Final Telegram]
    A2 -->|publish| B[Buffer LI/IG]
    B --> Pub[published]
```

## 2 Kademeli Onay

```mermaid
flowchart LR
    A[Taslak] --> B[Onayla / Reddet]
    B -->|Onayla| C[Görsel + Final]
    B -->|Reddet| D[rejected]
    C --> E[Yayınla / İptal]
    E -->|Yayınla| F[published]
    E -->|İptal| G[preview_rejected]
```
