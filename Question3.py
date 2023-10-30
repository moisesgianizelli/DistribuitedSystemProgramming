# Behavioral design pattern (Strategy Design Pattern) [30 Marks]
# Suppose we want to buy a stock for some amount, at some given price, and we have to strategize to
# decide, depending upon the strategy, we will change the amount for which we want to buy the stock.
# And we will change the price at which we would like to buy the stock.
# Assume that we have two strategies, one is aggressive, and one is passive. If we are moving with
# aggressive strategy, then what we will do is we will invest our whole amount at the current price of
# the stock. And if we are moving with the passive strategy, then what we will do is we would invest
# only 50% of the amount and that to at 90% of the current price. So, we will wait in this case so that
# the stock price comes down to the 90% of its current one, and then only we will invest, and we will
# invest only half of our amount i.e., 50%.
# So, these are the two strategies which we would like to use and whenever we are buying the stock,
# we will specify with which strategy we are moving with.
# Use python to demonstrate above concept of strategy design pattern. Share code along with a word
# document including snapshots with detailed explanation

class Stock:
    def __init__(self, currentStockPrice, totalAmountToInvest):
        self.currentStockPrice = currentStockPrice
        self.totalAmountToInvest = totalAmountToInvest


class Strategy:
    def buyStock(self, stock):
        pass


class AggressiveStrategy(Strategy):
    def buyStock(self, stock):
        currentStockPrice = float(stock.currentStockPrice)
        totalAmountToInvest = float(stock.totalAmountToInvest)
        investmentAggressive = currentStockPrice * totalAmountToInvest
        print("Your investment will be:", investmentAggressive)


class PassiveStrategy(Strategy):
    def buyStock(self, stock):
        totalAmountToInvest = float(stock.totalAmountToInvest)
        currentStockPrice = float(stock.currentStockPrice)

        # Invest 50% of the amount at 90% of the current price
        investment = (totalAmountToInvest * 0.5) * (currentStockPrice * 0.9)
        print("You invested 50% at 90% and your current investment is:", investment)

        # Check new conditions
        newStockPrice = float(input("New price of the stock: "))
        if newStockPrice <= currentStockPrice * 0.9:
            newInvestment = (totalAmountToInvest * 0.5) * (newStockPrice * 0.9)
            print("Your investment will be", (newInvestment + investment))
        else:
            print(
                "We keep the other half until the price drops so your investment still:", investment)


while True:
    currentStockPrice = input("Please enter the current stock price: ")
    totalAmountToInvest = input(
        "Please enter the total amount you want to invest: ")
    stock = Stock(currentStockPrice, totalAmountToInvest)

    userStrategyChoice = input(
        "Select a strategy 1 aggressive or 2 passive): ")
    if userStrategyChoice == "1":
        strategy = AggressiveStrategy()
    elif userStrategyChoice == "2":
        strategy = PassiveStrategy()
    strategy.buyStock(stock)
    userChoice = input(
        "Do you want to repeat the investment process? (yes/no): ")
    if userChoice.lower() != 'yes':
        break


# MAKE THE WORD DOCUMENT WITH THE STRATEGY
