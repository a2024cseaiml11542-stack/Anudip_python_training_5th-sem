# Stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock = []
available = 0
healthy = []

for qty in stock:

    # Count out of stock products
    if qty == 0:
        out_of_stock += 1

    # Products needing restock
    if qty < 10:
        restock.append(qty)

    # Available products
    if qty > 0:
        available += 1

    # Healthy stock products
    if qty >= 15:
        healthy.append(qty)

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy)