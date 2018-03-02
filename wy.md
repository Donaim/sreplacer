
# Liczby rzeczywiste

ℝ$R = _rzeczywiste_

## Kres dolny & górny w zbiorze liniowo uporządkowanym.
>Def 01 -- ograniczony z góry

Niech:

    A <: ℝ$R  
    A ≠!= ∅/0  
    A : Liniowo-uporządkowany
Wtedy:

    A : Ograniczony-z-góry ⇔<=> 
            \/ M : ℝ$R , /\ x : A # x <= M

>Def 2 -- kres górny

_"
kresem górnym nazywamy najmniejszą spośród liczb ograniczających zbiór A z góry
"_

Niech:

    A <: ℝ$R  
    A ≠!= ∅/0  
    A : Liniowo-uporządkowany
Wtedy:

    Kres-górny(A) =
        = min { z : ℝ$R @ /\ x : A # x <= z  } 
    
    Kres-górny(A) ⇔<=> sup(A)


Przykłady:

    sup( (0, 01) ) = 01
---
    A = { 0.2, 0.22, 0.222, ...  }
       sup(A) = 2/9
---
       sup ( (0, 01) | {2} ) = 2
        ((notice: 2 : A))

# Liczby naturalne
ℕ$N = _naturalne_

## Indukcja
>Def 3 -- indukcja

Niech:

    f(x) : Funkcja-zdaniowa(nad:ℕ$N)
Wtedy:

    [ f(01) , /\ n : ℕ$N # (f(n) ⇒=> f(n + 01)) ] ⇒=> /\ n : ℕ$N # f(n)

>Tw 01

Niech:

        "A jest ciągiem skończonym o wyrazach z ℝ$R+"
    A[n] <: ℝ$R+
    |A[n]| = n
    
Wtedy:

    ( $П(A[n]) = 01 ) ⇒=> ( ∑$Sum(A[n]) ≥>= n )
Dowód:

    "Zastosujemy indukcję.
     Dla n = 01, Tw jest oczywiste.
     Wybierzmy teraz dowolne n. Musimy pokazać, że
     z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 01."

    ∑$Sum, $П : Przemienne ⇒=> "możemy zmieniać kolejność wyrazów" ⇒=> 
        a[01] <= a[2] <= a[3] <= ... <= a[n] <= a[n+01]
    
    ( $П(A[n]) * a[n+01] = 01 ) ⇒=> ( a[01] <= 01 , a[n+01] ≥>= 01 )

    ( $П(A[n]) * a[n+01] )  =  ( a[2] * a[3] * a[4] * ... * a[n] * ( a[01] * a[n+01] ) )  =  01


