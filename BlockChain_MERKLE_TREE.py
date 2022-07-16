import hashlib

n = int(input("Enter the number of transactions: "))

trans = []
hashes = []
for i in range(n):
    trns = input("Enter the transaction " + str(i+1) + ": ")
    trans.append(trns)

for i in trans:
        hashes.append(hashlib.sha256(i.encode()).hexdigest())
        #conversion of transaction to hash

print("Trxn:-\tHashes")
for i in range(len(hashes)):
    print(trans[i]+"\t"+hashes[i])
    #storing the hash values respectively

if (len(hashes) % 2 != 0):
    hashes.append(hashes[-1])
    #if the hashes length is odd it duplicates the last element in the hashes list

while (len(hashes)>1):
    j=0
    for i in range(0, len(hashes) - 1):
        hashes[j] = hashlib.sha256((str(hashes[i] + hashes[i + 1])).encode()).hexdigest()
        # hash of the i th leaf and i + 1 th leaf are concatenated
	# to find the hash parent to the both

        i += 2
        j += 1

    print("Hash Value After Each Operation: " + str(hashes))

    print("Length of Hashes: "+ str(len(hashes)))

    lastdel = i - j
    
    del hashes[-lastdel:]
    # as we now have the hash to the upper level of the tree, we delete the extra space in the array.
    # in each iteration of this loop the size of the Hashes list is halved.

print("Root Hash Value: " + str(hashes))
