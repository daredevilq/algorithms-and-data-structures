from zad1testy import runtests

# Piotr Śmiałek

# Algorytm sprawdza wszystkie mozliwe palindromy o nieparzystej liczbie znakow w podanym stringu i zwraca ilosc znakow najdluzszego.
# Pierwsza petla for odpowiada za wybranie srodkowego znaku [mid_char] - takowy zawsze istnieje,
# poniewaz szukany palindrom ma nieparzysta liczbe znakow. [x] to odleglosc od srodka [mid_char].
# W tym algorytmie korzystam z tego, ze jesli wiem ze  (...)attbcbtta(...) jest palindromem od dlugosci 9 to  (...)ttbcbtt(...) tez jest palindromem i (...)tbcbt(...) itd.
# jesli palindrom jest dlugosci 2*x+1 to jest tez palindrom dlugosci 2*x+1-2 i 2*x+1-4, 2*x+1-6 ... 




def ceasar(s):

    max_leng=0

    for mid_char in range(len(s)):
        for x in range(len(s)):
            if mid_char-x>=0 and mid_char+x<len(s):
                if s[mid_char+x]!=s[mid_char-x]:
                    break
                else:
                    max_leng=max(max_leng,2*x+1)
    return max_leng         


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
