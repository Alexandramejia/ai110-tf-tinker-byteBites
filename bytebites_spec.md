## Candidate Classes

4 nouns: Customer, Menu Item, Order, Payment

Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

---

## Revised UML Class Diagram

```mermaid
classDiagram
    class Customer {
        +String name
        +String email
        +List~Order~ purchaseHistory
        +placeOrder() Order
        +verify() boolean
    }

    class MenuItem {
        +String name
        +float price
        +String category
        +float popularityRating
        +getDetails() String
    }

    class Order {
        +String orderId
        +List~MenuItem~ items
        +Map~MenuItem, int~ quantities
        +Date date
        +float totalCost
        +addItem(item: MenuItem, qty: int) void
        +removeItem(item: MenuItem) void
        +computeTotal() float
    }

    class Payment {
        +String paymentType
        +float amount
        +boolean isProcessed
        +Order order
        +processPayment() boolean
        +getReceipt() String
    }

    Customer "1" --> "0..*" Order : places
    Order "1" *-- "1" Payment : paid via
    Order "1..*" --> "1..*" MenuItem : contains
```

### Multiplicity Key

| Symbol | Meaning |
|---|---|
| `1` | exactly one |
| `0..*` | zero or more |
| `1..*` | one or more |

### Relationship Notes

| Relationship | Type | Multiplicity | Description |
|---|---|---|---|
| Customer → Order | Association | 1 to 0..* | A customer places zero or more orders; each order belongs to one customer |
| Order → MenuItem | Association | 1..* to 1..* | An order holds one or more items; the same item can appear in many orders |
| Order → Payment | Composition | 1 to 1 | Every order is settled by exactly one payment; payment cannot exist without its order |

### Changes from Draft

- `Order` gains `orderId` (unique transaction identifier)
- `Payment` gains a back-reference to its `Order` to support receipt/lookup flows
- Multiplicity notation tightened to Mermaid-standard (`0..*`, `1..*`) instead of plain English labels
