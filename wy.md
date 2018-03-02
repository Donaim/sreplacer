
# Liczby rzeczywiste

ℝ = _rzeczywiste_

## Kres dolny & górny w zbiorze liniowo uporządkowanym.
>Def 1 -- ograniczony z góry

Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
Wtedy:

    A ∈ Ograniczony-z-góry ⇔ 
           ⇔  ∃ M ∈ ℝ   ∀ x ∈ A  :  x ≤ M

>Def 2 -- kres górny

_"
kresem górnym nazywamy najmniejszą spośród liczb ograniczających zbiór A z góry
"_

Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
Wtedy:

    Kres-górny(A) =
        = min { z ∈ ℝ | ∀ x ∈ A  : x ≤ z  } 
    
    Kres-górny(A) ⇔ sup(A)


Przykłady:

    sup( (0, 1) ) = 1
---
    A = { 0.2, 0.22, 0.222, ...  }
       sup(A) = 2/9
---
       sup ( (0, 1) ∨ {2} ) = 2
        ((notice: 2 ∈ A))

# Liczby naturalne
ℕ = _naturalne_

## Indukcja
>Def 3 -- indukcja

Niech:

    x ∈ ℕ
    f(x) ∈ Funkcja-zdaniowa
Wtedy:

    [ f(1)  ∧  ∀ n ∈ ℕ  :  f(n) ⇒ f(n + 1) ]  ⇒  ∀ n ∈ ℕ  :  f(n)

>Tw 1

Niech:

        "A jest ciągiem skończonym o wyrazach z ℝ₊"
    Aₙ ⊂ ℝ+
    |Aₙ| = n
    
Wtedy:

    ( ∏ Aₙ = 1 ) ⇒ ( ∑ Aₙ ≥ n )
Dowód:

    "Zastosujemy indukcję.
     Dla n = 1, Tw jest oczywiste.
     Wybierzmy teraz dowolne n. Musimy pokazać, że
     z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 1."

    ∑, ∏ ∈ Przemienne ⇒ "możemy zmieniać kolejność wyrazów" ⇒ 
        a₁ ≤ a₂ ≤ a₃ ≤ ... ≤ aₙ ≤ aₙ₊₁
    
    ( ∏ Aₙ × aₙ₊₁ = 1 ) ⇒ ( a₁ ≤ 1 ∧ aₙ₊₁ ≥ 1 )

    ( ∏ Aₙ × aₙ₊₁ )  =  ( a₂ × a₃ × a₄ × ... × aₙ × ( a₁ × aₙ₊₁ ) )  =  1


