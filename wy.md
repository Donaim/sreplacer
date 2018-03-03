
# Liczby rzeczywiste

ℝ = _rzeczywiste_

## Kres dolny ∩ górny w zbiorze liniowo uporządkowanym.
### Def 1 -- ograniczony z góry

> Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
> Wtedy:

    A ∈ Ograniczony-z-góry ⇔ 
           ⇔  ∃ M ∈ ℝ   ∀ x ∈ A  :  x ≤ M

### Def 2 -- kres górny

_kresem górnym nazywamy najmniejszą spośród liczb ograniczających zbiór A z góry_

> Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
> Wtedy:

    Kres-górny(A) =
        = min { z ∈ ℝ | ∀ x ∈ A  : x ≤ z  } 
    
    Kres-górny(A) ⇔ sup(A) ⇔ "supremum A"


> Przykłady:

    sup( (0, 1) ) = 1
---
    A = { 0.2, 0.22, 0.222, ...  }
       sup(A) = 2/9
---
    A = (0, 1) ∪ {2}
       sup(A) = 2
        ((notice: 2 ∈ A))

# Liczby naturalne
ℕ = _naturalne_

## Indukcja
### Def 3 -- indukcja

> Niech:

    n ∈ ℕ
    f(n) ∈ Funkcja-zdaniowa
> Wtedy:

    [ f(1)  ∧  ∀ n  :  f(n) ⇒ f(n + 1) ]  ⇒  ∀ n : f(n)

### Tw 1

> Niech:

_A jest ciągiem skończonym o wyrazach z ℝ₊_

    n ∈ ℕ
    Aₙ ⊂ ℝ₊
    |Aₙ| = n
> Wtedy:

    ( 𝓟roduct Aₙ = 1 ) ⇒ ( ∑ Aₙ ≥ n )
> Dowód:

_Zastosujemy indukcję._  
_Dla n = 1, Tw jest oczywiste._  
_Wybierzmy teraz dowolne n. Musimy pokazać, że_  
_z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 1._  

    ∑, 𝓟roduct ∈ Przemienne ⇒ "możemy zmieniać kolejność wyrazów" ⇒ 
        a₁ ≤ a₂ ≤ a₃ ≤ ... ≤ aₙ ≤ aₙ₊₁
    
    ( 𝓟roduct Aₙ × aₙ₊₁ = 1 ) ⇒ ( a₁ ≤ 1 ∧ aₙ₊₁ ≥ 1 )

    ( 𝓟roduct Aₙ × aₙ₊₁ )  =  ( a₂ × a₃ × a₄ × ... × aₙ × ( a₁ × aₙ₊₁ ) )  =  1


