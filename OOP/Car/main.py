class Car:

  def __init__(self, model = None, year = None):
    self.model = model
    self.year = year
  
  def getModel(self):
    return f"Model: {self.model}"

  def getYear(self):
    return f"Year: {self.year}"


emptyCar = Car()
toyotaCar = Car(model = "Toyota Rav4", year = 2018)

print(f"Model: {emptyCar.getModel()} | Year: {emptyCar.getYear()}")
print(f"Model: {toyotaCar.getModel()}| Year: {toyotaCar.getYear()}")