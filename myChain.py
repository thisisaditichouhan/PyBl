import hashlib


def generationOfHash(incomingData):
    resultant=hashlib.sha256(incomingData.encode())
    return resultant.hexdigest()

class thisIsBlock:
    def __init__(self,incomingData,hash,previous_hash):
        self.incomingData=incomingData
        self.hash=hash
        self.previous_hash=previous_hash

class thisIsBlockchain:
    def __init__(self):
      lastHash=generationOfHash('gen_last')
      startingHash=generationOfHash('gen_hash')

      genesis=thisIsBlock('gen-data',startingHash,lastHash)
      self.thisIsChain=[genesis]

    def addNewBlock(self,incomingData):
        previous_hash=self.thisIsChain[-1].hash
        hash=generationOfHash(incomingData+previous_hash)
        blockToBeAdded=thisIsBlock(incomingData,hash,previous_hash)
        self.thisIsChain.append(blockToBeAdded)

tib=thisIsBlockchain()
tib.addNewBlock("NEW BLOCK ADDED")
tib.addNewBlock("NEXT BLOCK ADDED")
tib.addNewBlock("CONGRATULATIONS")

for blockChainInDictForm in tib.thisIsChain:
    print(blockChainInDictForm.__dict__)
