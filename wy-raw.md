
# Liczby rzeczywiste

$R = _rzeczywiste_

## Kres dolny & górny w zbiorze liniowo uporządkowanym.
>Def 1 -- ograniczony z góry

Niech:

    A <: $R  
    A != /0  
    A : Liniowo-uporządkowany
Wtedy:

    A : Ograniczony-z-góry <=> 
           <=>  \/ M : $R   /\ x : A  ::  x <= M

>Def 2 -- kres górny

_"
kresem górnym nazywamy najmniejszą spośród liczb ograniczających zbiór A z góry
"_

Niech:

    A <: $R  
    A != /0  
    A : Liniowo-uporządkowany
Wtedy:

    Kres-górny(A) =
        = min { z : $R @ /\ x : A  :: x <= z  } 
    
    Kres-górny(A) <=> sup(A)


Przykłady:

    sup( (0, 1) ) = 1
---
    A = { 0.2, 0.22, 0.222, ...  }
       sup(A) = 2/9
---
       sup ( (0, 1) | {2} ) = 2
        ((notice: 2 : A))

# Liczby naturalne
$N = _naturalne_

## Indukcja
>Def 3 -- indukcja

Niech:
    x : $N
    f(x) : Funkcja-zdaniowa
Wtedy:

    [ f(1)  ,  /\ n : $N  ::  f(n) => f(n + 1) ]  =>  /\ n : $N  ::  f(n)

>Tw 1

Niech:

        "A jest ciągiem skończonym o wyrazach z $R[+]"
    A[n] <: $R+
    |A[n]| = n
    
Wtedy:

    ( $Product A[n] = 1 ) => ( $Sum A[n] >= n )
Dowód:

    "Zastosujemy indukcję.
     Dla n = 1, Tw jest oczywiste.
     Wybierzmy teraz dowolne n. Musimy pokazać, że
     z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 1."

    $Sum, $Product : Przemienne => "możemy zmieniać kolejność wyrazów" => 
        a[1] <= a[2] <= a[3] <= ... <= a[n] <= a[n][+][1]
    
    ( $Product A[n] * a[n][+][1] = 1 ) => ( a[1] <= 1 , a[n][+][1] >= 1 )

    ( $Product A[n] * a[n][+][1] )  =  ( a[2] * a[3] * a[4] * ... * a[n] * ( a[1] * a[n][+][1] ) )  =  1


