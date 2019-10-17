def zad2(data_text):
   length=len(data_text)
   letter=list(data_text)
   big_letters=data_text.upper()
   small_letters=data_text.lower()

   dict={"lenght": length, "letter":letter, "big_letter":big_letters, "small_letter":small_letters}
   for key, value in dict.items():
        print(key, " = ", value)
text="Szymon Jagaczewski"
zad2(text)