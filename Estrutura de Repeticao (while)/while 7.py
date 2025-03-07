#7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B
#com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para
#que a população do país A ultrapasse a população do país B.

# População dos países
populacao_a = 80000
populacao_b = 200000

# Taxas de crescimento anual
taxa_crescimento_a = 0.03  # 3%
taxa_crescimento_b = 0.015  # 1,5%

# Contador de anos
anos = 0

while True:
    if populacao_a > populacao_b:
        break
    
    populacao_a += populacao_a * taxa_crescimento_a  
    populacao_b += populacao_b * taxa_crescimento_b  
    anos += 1 

print(f"Será necessário {anos} anos para que a população de A ultrapasse a de B.") 