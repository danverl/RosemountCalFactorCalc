def calculateCorrection(referenceTotal, meterTotal):
  return referenceTotal / meterTotal
def calculate16digitCalFactor(oldCalFactor : str, correctionFactor :int):
  #format xxxxx x xx xxxxx xxx
  #eks 09582 5 50 09448 000
  newOutput = ""
  indices = [0,5,6,8,13]
  parts = [oldCalFactor[i:j] for i,j in zip(indices, indices[1:]+[None])]

  gain37hz = int(parts[0]) * correctionFactor
  spacer = parts[1]
  zeroOffset = parts[2]
  gain5hz = int(parts[3]) * correctionFactor
  trailingZeroes = parts[4]

  newOutput = str(gain37hz) + str(spacer) + str(zeroOffset) + str(gain5hz) + str(trailingZeroes)
  
if __name__ == "__main__":
  print("Tool to calcultate correction factor for Rosemount 8700 series flow meters")
  oldCalFactor = input("Input your old 16 digit cal factor")  # Python 3
  referenceTotal = input("Input your reference total")  # Python 3
  meterTotal = input("Input your meter total")  # Python 3
  correction = calculateCorrection(referenceTotal, meterTotal)
  print("The correction factor is ", correction)
