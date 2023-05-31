# Importerer tid for spørsmål.
import time

# Ordbok av Svar
svar = {
    # Hilsen
    "god dag"           : "god dag til deg og",
    "hallo"             : "hallo",
    "ha det bra"        : "ha det bra",
    
    # Spørsmål
    "hvordan er været"  : "vanlig",
    "hvor gammel er du" : "uendelig år",
    "hva er klokka"     : f"klokka er {time.strftime('%H:%M')}",
}

# Uendelig While Loop, for uendelig spørring av spørsmål. 
while True:
    # Får input fra Brukeren.
    userInput = input('> ')

    # Sjekker hvis svaret finnes. Hvis det ikke gjør det, vil AI-en svare med "hæ".
    if userInput in svar:
        # Bruker "get" funksjonen til å få verdien av key-en ved å bruke brukeren sin input. Setter det i AIoutput variabelen.
        AIoutput = svar.get(userInput)
    else:
        AIoutput = ('hæ')

    # Printer AI-output
    print(f'AI: {AIoutput}')
