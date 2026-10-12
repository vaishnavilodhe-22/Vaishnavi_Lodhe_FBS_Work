# Write a program to accept an integer amount from user and tell minimum no.of notes needed for representing the amount

amt=int(input(("Enter amount:")))
note_2000=amt//2000
rem_amt=amt%2000
note_500=rem_amt//500
remaining=rem_amt%500
note_100=remaining%100
remaining=remaining//100

print("Notes of 2000:",note_2000)
print("Notes of 500:",note_500)
print("Notes of 100:",note_100)
print("Remaining amount:",remaining)
