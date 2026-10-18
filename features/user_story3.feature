Feature: Lägg till bok
  Scenario: Aktivera knappen när titel och författare är ifyllda
    Given att användaren öppnar sidan Lägg till bok
    Then ska ett fält för titel visas
    And ska ett fält för författare visas
    And knappen "Lägg till ny bok" vara inaktiverad

    When användaren fyller i titel och författare
    Then ska knappen "Lägg till ny bok" vara aktiverad