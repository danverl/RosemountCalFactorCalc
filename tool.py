import unittest

def calculateCorrection(referenceTotal, meterTotal):
  return float(meterTotal) / float(referenceTotal)

def calculate16digitCalFactor(oldCalFactor, correctionFactor):
  indices = [0,5,6,8,13]
  parts = [str(oldCalFactor)[i:j] for i,j in zip(indices, indices[1:]+[None])]

  gain37hz = round(int(parts[0]) * correctionFactor)
  spacer = parts[1]
  zeroOffset = parts[2]
  gain5hz = round(int(parts[3]) * correctionFactor)
  padding1 = ""
  padding2 = ""
  if gain37hz < 10000: 
    padding1 = "0"
  else:
    padding1 = ""
  if gain5hz < 10000: 
    padding2 = "0"
  else:
    padding2 = ""
  
  return f"{padding1}{gain37hz}{spacer}{zeroOffset}{padding2}{gain5hz}000"
  
class TestCalculation(unittest.TestCase):
  def test_calfactor_known_values(self):
    self.assertEqual(calculate16digitCalFactor("0958255009448000", float(calculateCorrection(5982.562, 6015.34))),"0963455009500000")
    
  def test_correction_factor_calculation_1(self):
    self.assertEqual(float(calculateCorrection(100, 100)), 1)
    
  def test_correction_factor_calculation_half(self):
    self.assertEqual(float(calculateCorrection(100, 50)), 0.5)
    
  def test_correction_factor_calculation_half_pos(self):
    self.assertEqual(float(calculateCorrection(50, 100)), 2)
    
if __name__ == "__main__":
  #unittest.main()
  print("Tool to calcultate correction factor for Rosemount 8700 series flow meters")
  oldCalFactor = input("Input your old 16 digit cal factor")  # Python 3
  referenceTotal = input("Input your reference total")  # Python 3
  meterTotal = input("Input your meter total")  # Python 3
  correction = calculateCorrection(referenceTotal, meterTotal)
  print("The correction factor is ", correction)
  print("Your new factor is ", calculate16digitCalFactor(oldCalFactor, correction))