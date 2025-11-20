def calculateCorrection(referenceTotal, meterTotal):
  return referenceTotal / meterTotal
def calculate16digitCalFactor(oldCalFactor : str, correctionFactor :int):
  #format xxxxx x xx xxxxx xxx
  newOutput = ""
  indices = [0,5,6,8,13]
  parts = [oldCalFactor[i:j] for i,j in zip(indices, indices[1:]+[None])]

  gain37hz = int(parts[0]) * correctionFactor
  spacer = parts[1]
  zeroOffset = parts[2]
  gain5hz = int(parts[3]) * correctionFactor
  trailingZeroes = parts[4]

  newOutput = str(gain37hz) + str(spacer) + str(zeroOffset) + str(gain5hz) + str(trailingZeroes)

def test():
  #old 09582 5 50 09448 000
  #ref total 5976.5
  #dut total 5983.064
  #correction 0.9989029033
  #new 09571 5 50 9437 000
  oldCalFactor = 0958255009448000
  referenceTotal = 5976.5
  dutTotal = 5983.064
  correction = calculateCorrection(referenceTotal, dutTotal)
  if int(calculate16digitCalFactor(oldCalFactor, correction)) = 095715509437000:
    print("Test passed")
  else:
    print("Test failed")
  
if __name__ == "__main__":
  print("Tool to calcultate correction factor for Rosemount 8700 series flow meters")
  oldCalFactor = input("Input your old 16 digit cal factor")  # Python 3
  referenceTotal = input("Input your reference total")  # Python 3
  meterTotal = input("Input your meter total")  # Python 3
  correction = calculateCorrection(referenceTotal, meterTotal)
  print("The correction factor is ", correction)
  print("Your new factor is ", calculate16digitCalFactor(oldCalFactor, correction))
