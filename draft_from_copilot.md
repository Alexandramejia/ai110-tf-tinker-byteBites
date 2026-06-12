## UML Class Diagram

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
        +processPayment() boolean
        +getReceipt() String
    }

    Customer "one" --> "many" Order : places
    Order "one" --> "one" Payment : paid via
    Order "many" --> "many" MenuItem : contains
```

### Relationship Notes

| Relationship | Type | Multiplicity | Description |
|---|---|---|---|
| Customer → Order | Association | One-to-Many | A customer places zero or more orders; each order belongs to one customer |
| Order → MenuItem | Association | Many-to-Many | An order holds one or more items; the same item can appear in many orders |
| Order → Payment | Composition | One-to-One | Every order is settled by exactly one payment; payment cannot exist without its order |
