## Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

Enhetstest testar en liten del av programmet, till exempel en funktion eller knapp.

Integrationstest testar att flera delar av programmet fungerar tillsammans.

Regressionstest kontrollerar att något som fungerade tidigare fortfarande fungerar efter ändringar.

Prestandatest testar hur snabbt programmet är och om det klarar många användare samtidig

## Beskriv hur det går till när man arbetar med TDD.
När man arbetar med TDD börjar man med att skriva ett test innan man skriver själva koden.

Först skriver man ett test som inte fungerar eftersom koden inte finns än. Sedan skriver man koden så att testet blir 
godkänt. Efter det kan man förbättra koden utan att ändra hur den fungerar. Sedan upprepar man samma process för 
nästa funktion.

## Beskriv hur BDD skiljer sig från TDD.

TDD fokuserar på att testa koden, medan BDD fokuserar mer på hur programmet ska fungera ur användarens perspektiv.
Man beskriver vad systemet ska göra i olika omständigheter och vilket resultat man förväntar sig. På så sätt blir det lättare 
för både utvecklare och testare att förstå hur programmet ska fungera.


## Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja 
## förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

Jag skulle använda enhetstester, integrationstester, regressionstester och E2E-tester.

Enhetstester kontrollerar att enskilda delar fungerar. Integrationstester ser att olika delar fungerar tillsammans. 
Regressionstester kontrollerar att gamla funktioner fortfarande fungerar efter ändringar. E2E-tester testar hela 
användarflöden.

Prestandatest kan också vara bra att testa för att se att om webbsidan fortfarande fungerar när många 
personer använder den samtidigt.
