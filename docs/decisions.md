## 2026-06-25
# Database Design Decisions

---

## Decision

Store **Themes** as a separate table.

### Reason

Themes are reusable concepts that apply across many tickers. Storing them once follows the Alpha Principle by avoiding duplicated data.

---

## Decision

Store **Styles** as a separate table.

### Reason

Styles are reusable visual identities that influence AI-generated artwork and should not be duplicated across designs.

---

## Decision

Do **not** create a Prompts table for the MVP.

### Reason

Prompts are derived from the selected ticker, theme, style, and humor. Since they can be generated dynamically, storing them would duplicate calculated information and violate the Alpha Principle.

---

## Decision

Rename `products` to `product_variants`.

### Reason

A single design can produce multiple purchasable products (shirt, hoodie, mug, sticker, etc.). "Product Variant" better reflects the relationship between a design and the merchandise created from it.

---

## Decision

Defer the `generated_assets` table until a future sprint.

### Reason

The MVP only requires a single generated image. The current architecture allows generated assets to be added later without requiring changes to the existing schema, following the "Design for Extension, Not Prediction" principle.

---

## Decision

Remove unnecessary `status` fields from the MVP schema.

### Reason

Each field should have a clear consumer. If no current feature reads or depends on a status value, it should not exist until a real business need emerges.

# Engineering Decisions
## 2026-06-25

Decision

Use FastAPI instead of Django.

Reason

Already familiar.

Smaller.

Better suited to APIs.

---

Decision

Zero inventory.

Reason

No financial risk.

---

Decision

Generate products from prompts instead of storing static products.

Reason

Infinite scalability.

---

Decision

Public GitHub repository.

Reason

Portfolio value.
