
`27.02.18`

# Liczby rzeczywiste

ℝ = _rzeczywiste_

## Kres górny ∧ dolny w zbiorze liniowo uporządkowanym.
### Def 1 : ograniczony z góry ∧ z dołu

> Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
> Wtedy:

    A ∈ Ograniczony-z-góry ⇔ 
           ⇔  ∃ m ∈ ℝ   ∀ x ∈ A  :  x ≤ m

    A ∈ Ograniczony-z-dołu ⇔ 
           ⇔  ∃ m ∈ ℝ   ∀ x ∈ A  :  x ≥ m

### Def 2 : kres górny ∧ dolny

_kresem **górnym** nazywamy **najmniejszą** spośród liczb ograniczających zbiór A **z góry**_  
_kresem **dolnym** nazywamy **największą** spośród liczb ograniczających zbiór A **z dołu**_  
k
> Niech:

    A ⊂ ℝ  
    A ≠ ∅  
    A ∈ Liniowo-uporządkowany
> Wtedy:

    Kres-górny(A) =
        = min { z ∈ ℝ | ∀ x ∈ A : x ≤ z  } 
    
    Kres-górny(A) ⇔ sup(A) ⇔ "supremum A"

    Kres-dolny(A) =
        = max { z ∈ ℝ | ∀ x ∈ A : x ≥ z  } 
    
    Kres-dolny(A) ⇔ inf(A) ⇔ "infimum A"


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
### Def 3 : indukcja

> Niech:

    n ∈ ℕ
    f(n) ∈ Funkcja-zdaniowa
> Wtedy:

    [ f(1)  ∧  ∀ n  :  f(n) ⇒ f(n + 1) ]  ⇒  ∀ n : f(n)

### Tw 1 
[wersja w j. angielskim](https://math.stackexchange.com/questions/1982625/induction-proof-if-product-of-n-numbers-is-1-sum-is-n)  
[wiki - uogólnienie (_zależność między średnimi_)](https://pl.wikipedia.org/wiki/Nier%C3%B3wno%C5%9Bci_mi%C4%99dzy_%C5%9Brednimi)  

> Niech:

_A jest ciągiem skończonym o wyrazach z ℝ₊_

    n ∈ ℕ
    Aₙ ⊂ ℝ₊
    |Aₙ| = n
> Wtedy:

    ( ∏ Aₙ = 1 ) ⇒ ( ∑ Aₙ ≥ n )
> Dowód:

_Zastosujemy indukcję._  
_Dla n = 1, Tw jest oczywiste._  
_Wybierzmy teraz dowolne n. Musimy pokazać, że_  
_z prawidłowości Tw dla n, wynika prawidłowość Tw dla n + 1._  

    ∑, ∏ ∈ Przemienne ⇒ "możemy zmieniać kolejność wyrazów" ⇒ 
        a₁ ≤ a₂ ≤ a₃ ≤ ... ≤ aₙ ≤ aₙ₊₁
    
    ( ∏ Aₙ × aₙ₊₁ = 1 ) ⇒ ( a₁ ≤ 1 ∧ aₙ₊₁ ≥ 1 )

    ( ∏ Aₙ × aₙ₊₁ )  =  ( a₂ × a₃ × a₄ × ... × aₙ × ( a₁ × aₙ₊₁ ) )  =  1

_Stąd i z założenia indukcyjnego dostajemy:_

    a₂ + a₃ + a₄ + ... + aₙ + (a₁ × aₙ₊₁) ≥ n
        ⇒
    a₁ + (a₂ + a₃ + a₄ + ... + aₙ) + aₙ₊₁ ≥ n + a₁ + aₙ₊₁ - (a₁ × aₙ₊₁)
        ⇒
    ∑ Aₙ ≥ n + 1 - 1 + a₁ - aₙ₊₁ × (a₁ - 1)
        ⇒
    ∑ Aₙ ≥ n + 1 + (a₁ - 1) × (1 - aₙ₊₁)
    
    (a₁ - 1) × (1 - aₙ₊₁) ≥ 0
        ⇒
    n + 1 + (a₁ - 1) × (1 - aₙ₊₁) ≥ n + 1 ∎

# Ciągi liczbowe
### Def 1 : ciąg liczbowy

    n ∈ ℕ
    (aₙ) ⊂ 𝓟(ℝ)
    (aₙ) ∈ Ciąg-liczbowy ⇔
        ⇔ ∀ f : ℕ → (aₙ)

### Def 2 : klasyfikacja ciągów

Niech:

    (aₙ) ∈ Ciąg-liczbowy
Wtedy:
    
    1⁰ (aₙ) ∈ rosnący     ⇔ ∀ n : aₙ < aₙ₊₁
    2⁰ (aₙ) ∈ niemalejący ⇔ ∀ n : aₙ ≤ aₙ₊₁
    3⁰ (aₙ) ∈ malejący    ⇔ ∀ n : aₙ > aₙ₊₁
    4⁰ (aₙ) ∈ nierosnący  ⇔ ∀ n : aₙ ≥ aₙ₊₁

    5⁰ (aₙ) ∈ monotoniczny ⇔ 1⁰ ∨ 2⁰ ∨ 3⁰ ∨ 4⁰
    6⁰ (aₙ) ∈ ściśle-monotoniczny ⇔ 1⁰ ∨ 3⁰

