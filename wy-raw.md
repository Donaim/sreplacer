
`27.02.18`

# Liczby rzeczywiste

$R = _rzeczywiste_

## Kres górny , dolny w zbiorze liniowo uporządkowanym.
### Def 1 :: ograniczony z góry , z dołu

> Niech:

    A <: $R  
    A != /0  
    A : Liniowo-uporządkowany
> Wtedy:

    A : Ograniczony-z-góry <=> 
           <=>  \/ m : $R   /\ x : A  ::  x <= m

    A : Ograniczony-z-dołu <=> 
           <=>  \/ m : $R   /\ x : A  ::  x >= m

### Def 2 :: kres górny , dolny

_kresem **górnym** nazywamy **najmniejszą** spośród liczb ograniczających zbiór A **z góry**_  
_kresem **dolnym** nazywamy **największą** spośród liczb ograniczających zbiór A **z dołu**_  
k
> Niech:

    A <: $R  
    A != /0  
    A : Liniowo-uporządkowany
> Wtedy:

    Kres-górny(A) =
        = min { z : $R @ /\ x : A :: x <= z  } 
    
    Kres-górny(A) <=> sup(A) <=> "supremum A"

    Kres-dolny(A) =
        = max { z : $R @ /\ x : A :: x >= z  } 
    
    Kres-dolny(A) <=> inf(A) <=> "infimum A"


> Przykłady:

    sup( (0, 1) ) = 1
---
    A = { 0.2, 0.22, 0.222, ...  }
       sup(A) = 2/9
---
    A = (0, 1) || {2}
       sup(A) = 2
        ((notice: 2 : A))

# Liczby naturalne
$N = _naturalne_

## Indukcja
### Def 3 :: indukcja

> Niech:

    n : $N
    f(n) : Funkcja-zdaniowa
> Wtedy:

    [ f(1)  ,  /\ n  ::  f(n) => f(n + 1) ]  =>  /\ n :: f(n)

### Tw 1 
[wersja w j. angielskim](https://math.stackexchange.com/questions/1982625/induction-proof-if-product-of-n-numbers-is-1-sum-is-n)  
[wiki - uogólnienie (_zależność między średnimi_)](https://pl.wikipedia.org/wiki/Nier%C3%B3wno%C5%9Bci_mi%C4%99dzy_%C5%9Brednimi)  

> Niech:

_A jest ciągiem skończonym o wyrazach z $R[+]_

    n : $N
    A[n] <: $R[+]
    |A[n]| = n
> Wtedy:

    ( $Product A[n] = 1 ) => ( $Sum A[n] >= n )
> Dowód:

_Zastosujemy indukcję._  
_Dla n = 1, Tw jest oczywiste._  
_Wybierzmy teraz dowolne n. Musimy pokazać, że_  
_z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 1._  

    $Sum, $Product : Przemienne => "możemy zmieniać kolejność wyrazów" => 
        a[1] <= a[2] <= a[3] <= ... <= a[n] <= a[n][+][1]
    
    ( $Product A[n] * a[n][+][1] = 1 ) => ( a[1] <= 1 , a[n][+][1] >= 1 )

    ( $Product A[n] * a[n][+][1] )  =  ( a[2] * a[3] * a[4] * ... * a[n] * ( a[1] * a[n][+][1] ) )  =  1

_Stąd i z założenia indukcyjnego dostajemy:_

    a[2] + a[3] + a[4] + ... + a[n] + (a[1] * a[n][+][1]) >= n
        =>
    a[1] + (a[2] + a[3] + a[4] + ... + a[n]) + a[n][+][1] >= n + a[1] + a[n][+][1] - (a[1] * a[n][+][1])
        =>
    $Sum A[n] >= n + 1 - 1 + a[1] - a[n][+][1] * (a[1] - 1)
        =>
    $Sum A[n] >= n + 1 + (a[1] - 1) * (1 - a[n][+][1])
    
    (a[1] - 1) * (1 - a[n][+][1]) >= 0
        =>
    n + 1 + (a[1] - 1) * (1 - a[n][+][1]) >= n + 1 $qed

# Ciągi liczbowe
### Def 1 :: ciąg liczbowy

    n : $N
    (a[n]) <: $Ro($R)
    (a[n]) : Ciąg-liczbowy <=>
        <=> /\ f :: $N -> (a[n])

### Def 2 :: klasyfikacja ciągów

Niech:

    (a[n]) : Ciąg-liczbowy
Wtedy:
    
    1^0 (a[n]) : rosnący     <=> /\ n :: a[n] < a[n][+][1]
    2^0 (a[n]) : niemalejący <=> /\ n :: a[n] <= a[n][+][1]
    3^0 (a[n]) : malejący    <=> /\ n :: a[n] > a[n][+][1]
    4^0 (a[n]) : nierosnący  <=> /\ n :: a[n] >= a[n][+][1]

    5^0 (a[n]) : monotoniczny <=> 1^0 | 2^0 | 3^0 | 4^0
    6^0 (a[n]) : ściśle-monotoniczny <=> 1^0 | 3^0

