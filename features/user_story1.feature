Feature: Visa böcker i katalogen
  Scenario: Katalogen visas när webbplatsen öppnas
    Given att användaren öppnar webbplatsen
    Then visas knappen "Katalog"
    And visas knappen "Lägg till bok"
    And visas knappen "Mina böcker"
    And visas knappen "Statistik"
    And en lista med böcker visas
