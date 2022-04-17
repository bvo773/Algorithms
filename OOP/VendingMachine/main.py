
class VendingMachine:
  def __init__(self) -> None:
    self.choices = {}

  def addOption(self, key: int, choice: str):
    self.choices[key] = choice

  def showChoices(self):
    for key in self.choices:
      print(f"Option: {key} | Choice: {self.choices.get(key)}")

vendingMachine = VendingMachine()
vendingMachine.addOption(key = 1, choice = "COKE")
vendingMachine.addOption(key = 2, choice = "PEPSI")
vendingMachine.addOption(key = 3, choice = "DIET COKE")
vendingMachine.showChoices()