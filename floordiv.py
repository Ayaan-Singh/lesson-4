amount = int(input("please enter amount for withdrawing"))

note1 = amount//1000
note2 = (amount%1000) // 500
note3 = ((amount%1000)%500) // 100
note4 =  (((amount%1000)%500)%100 ) // 50
note5 = ((((amount%1000)%500)%100 )%50)//10
note6 = (((((amount%1000)%500)%100)%50)%10)//1

print ("notes of 1000 rupee",note1)
print ("notes of 500 rupee",note2)
print ("notes of 100 rupee",note3)
print ("notes of 50 rupee",note4)
print ("notes of 10 rupee",note5)
print ("notes of 1 rupee",note6)