weather = input("Enter the current weather? (sunny/rainy/cold): ").strip().lower()
match weather:
    case "sunny":
        print("Wear a t-shirt and sunglasses.")
    case "rainy":
        print("Don't forget your umbrella and a raincoat.")
    case "cold":
        print("make sure to wear a warm coat and a scarf.")
    case _:
        print("Sorry, I don't have recommendations for this weather.")
        