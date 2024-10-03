def get_sales_data():
    sales_data = []
    print("Enter sales data for products. Type 'done' when finished.")
    
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        category = input("Enter category: ")
        try:
            units_sold = int(input("Enter units sold: "))
            unit_price = float(input("Enter unit price: "))
        except ValueError:
            print("Invalid input. Please enter numerical values for units sold and unit price.")
            continue
        
        sales_data.append({
            "product_name": product_name,
            "category": category,
            "units_sold": units_sold,
            "unit_price": unit_price
        })
    
    return sales_data

def calculate_total_sales(sales_data):
    total_sales = 0
    for data in sales_data:
        total_sales += data["units_sold"] * data["unit_price"]
    return total_sales

def calculate_average_sales(total_sales, num_products):
    return total_sales / num_products if num_products > 0 else 0

def find_top_selling_products(sales_data):
    return sorted(sales_data, key=lambda x: x["units_sold"], reverse=True)

def calculate_sales_by_category(sales_data):
    sales_by_category = {}
    for data in sales_data:
        category = data["category"]
        if category not in sales_by_category:
            sales_by_category[category] = {
                "total_sales": 0,
                "total_units": 0
            }
        sales_by_category[category]["total_sales"] += data["units_sold"] * data["unit_price"]
        sales_by_category[category]["total_units"] += 1
    
    return sales_by_category

def calculate_average_sales_by_category(sales_by_category):
    average_sales_by_category = {}
    for category, data in sales_by_category.items():
        total_sales = data["total_sales"]
        total_units = data["total_units"]
        average_sales_by_category[category] = total_sales / total_units if total_units > 0 else 0
    
    return average_sales_by_category

def main():
    # Get sales data from the user
    sales_data = get_sales_data()
    
    if not sales_data:
        print("No sales data provided.")
        return
    
    # Calculate total and average sales
    total_sales = calculate_total_sales(sales_data)
    average_sales = calculate_average_sales(total_sales, len(sales_data))
    
    # Find top-selling products
    top_selling_products = find_top_selling_products(sales_data)
    
    # Calculate sales and average sales by category
    sales_by_category = calculate_sales_by_category(sales_data)
    average_sales_by_category = calculate_average_sales_by_category(sales_by_category)
    
    # Output results
    print(f"\nTotal Sales: {total_sales:.2f} Rs")
    print(f"Average Sales per Product: {average_sales:.2f} Rs")
    
    print("\nTop-Selling Products:")
    for product in top_selling_products:
        print(f"  - {product['product_name']}: {product['units_sold']} units sold")
    
    print("\nSales by Category:")
    for category, data in sales_by_category.items():
        print(f"  - {category}: {data['total_sales']:.2f}  Rs total sales")
    
    print("\nAverage Sales by Category:")
    for category, avg_sales in average_sales_by_category.items():
        print(f"  - {category}: {avg_sales:.2f} Rs average sales per product")

if __name__ == "__main__":
    main()
