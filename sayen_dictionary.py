#Joie Sayen
#JoyOfYahweh
#Dictionary - Exercise No. 5
#Data Structures and Algorithm Analysis

print (
"\n\t\t Spot Music Playlist \n\n 1. SILENT SANCTUARY \t\t 4. MOIRA DELA TORRE \n 2. TJ MONTERDE \t\t\t 5. SPONGE COLA  \n 3. RICO BLANCO")


def joie():
    js = {
        "1": " \n Hindi Na kita Mahal \n Pasensya Ka Na \n Kundiman \n Sayo \n Meron Ng Iba \n 14 ",
        "2": " \n Sa Tuwina \n Mahika \n Tulad Mo \n Ikaw at Ako \n Middle \n Imahinasyon ",
        "3": " \n Your Universe \n Bye Bye Na \n Wag Mo Aminin \n Sayaw \n Amats \n Time For You ",
        "4": " \n Torete \n Malaya \n Sundo \n You're my Sunshine \n Tagpuan \n Titibo tibo ",
        "5": " \n Pare Ko \n Makapiling Ka \n Kay Tagal Kitang Hinintay \n Jeepney \n Tuliro \n Tambay ",}

    sayen = input("\n NO.  ")
    if sayen == 1:
        print js["1"]
    elif sayen == 2:
        print js["2"]
    elif sayen == 3:
        print js["3"]
    elif sayen == 4:
        print js["4"]
    elif sayen == 5:
        print js["5"]
    else:
        print ("No music matched with the no. you've entered!!!")
        return joie()
    return joie()


joie()