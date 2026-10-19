Feature: Spara en ny bok

  Scenario: Lägga till en ny bok i katalogen
    Given att användaren öppnar webbsidan
    When användaren klickar på knappen "Lägg till bok"
    And användaren fyller i titelfältet med "Min bok"
    And användaren fyller i författarfältet med "Min författare"
    And användaren klickar på knappen "Lägg till ny bok"
    Then ska titel- och författarfälten vara tomma
    When användaren öppnar katalogen
    Then ska den nya boken visas längst ner i listan
