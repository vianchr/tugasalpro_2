while True :  
    x=int(input("masukan nilai x:"))
    if x == 0 :
        print ("eror akibat terdapat bilangan yang dibagi dengan 0, cobalah bilangan bulat lain") 
    else : 
        hasil = 2*x**3 + 2*x + 15/x
        print (f"jadi nilai fungsi(x) ketika x nya {x} adalah {hasil}")
        break
    

