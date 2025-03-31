# Activity 144

print("*** Sistema de Invetarios ***")

num_productos = int(input("Cuantos productos deseas agregar al invetario?"))
product_list = []

for item_num in range(num_productos):
    # Get product data
    print(f"Proporciona valores del producto {item_num+1}")
    product_name = input("Nombre: ")
    product_price = float(input("Precio: "))
    product_cant = int(input("Cantidad: "))
    # Create dictionary from product data
    current_product_dict = {'id': item_num, 'nombre': product_name, 'precio': product_price, 'cantidad': product_cant }
    # Add product to list of products
    product_list.append(current_product_dict)

print(f"Invetario incial: {product_list}")


search_id_product = int(input("Ingresa el ID del producto"))

for product in product_list:
    if product['id'] == search_id_product:
        print(product)
        break

