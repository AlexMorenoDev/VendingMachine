# Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
# que reciba dinero (array de monedas) y un número que indique la selección del producto.
# - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
#   número de monedas).
# - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
#   y retornar todas las monedas.
# - Si no hay dinero de vuelta, el array se retornará vacío.
# - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
# - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

class VendingMachine():
    def __init__(self):
        self.products = {
            1: ("Water", 55),
            2: ("Coca-Cola", 100),
            3: ("Beer", 155),
            4: ("Pizza", 200),
            5: ("Donut", 75)
        }
        self.valid_coins = [5, 10, 50, 100, 200]

    def coins_sum(self, coins):
        result = 0
        for coin in coins:
            if coin not in self.valid_coins:
                return None
            result += coin
        return result

    def calculate_coins(self, value):
        coins = []
        i = len(self.valid_coins) - 1
        while value != 0 and i >= 0:
            if value >= self.valid_coins[i]:
                coins.append(self.valid_coins[i])
                value -= self.valid_coins[i]
                i += 1
            i -= 1
            
        return coins

    def customer_service(self, coins, product_sel):
        sel_prod = self.products[product_sel] 
        inserted_money = self.coins_sum(coins)
        if inserted_money:
            prod_cost = sel_prod[1]
            if prod_cost <= inserted_money:
                remainder = inserted_money - prod_cost
                return sel_prod[0], self.calculate_coins(remainder)
            else:
                print("ERROR: Not enough money!")
                return coins
            
        else:
            print("ERROR: Inserted coin is not admitted by the vending machine!")
            return coins


if __name__ == "__main__":
    vm = VendingMachine()
    print(vm.customer_service([10, 10, 10, 10, 10, 5], 1))
    print(vm.customer_service([10, 10, 10, 10, 10, 10], 1))
    print(vm.customer_service([5, 5, 10, 10, 10, 5, 100], 1))
    print(vm.customer_service([200], 3))
    print(vm.customer_service([50, 50], 5))

