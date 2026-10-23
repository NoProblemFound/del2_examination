Feature: Mina favoritböcker

  Scenario: Inga favoritböcker har valts
    Given att användaren öppnar webplatsen
    When användaren öppnar sidan "Mina böcker"
    Then ska inga böcker visas i favoritlistan

  Scenario: Visa flera favoritböcker
    Given att användaren öppnar webbsidan
    When användaren markerar boken "Python för folk som hatar ormar" som favorit
    Then ska boken "Python för folk som hatar ormar" vara favoritmarkerad
    When användaren markerar boken "Git Blame and Other Ways to Lose Friends" som favorit
    Then ska boken "Git Blame and Other Ways to Lose Friends" vara favoritmarkerad
    When användaren öppnar sidan "Mina böcker"
    Then ska boken "Python för folk som hatar ormar" visas i favoritlistan
    And ska boken "Git Blame and Other Ways to Lose Friends" visas i favoritlistan

  Scenario: Ta bort en favoritböcker
    Given att användaren öppnar webbsidan
    When användaren markerar boken "Python för folk som hatar ormar" som favorit
    And användaren öppnar sidan "Mina böcker"
    Then ska boken "Python för folk som hatar ormar" visas i favoritlistan

    When användaren öppnar sidan "Katalog"
    And användaren avmarkerar boken "Python för folk som hatar ormar" som favorit
    And användaren öppnar sidan "Mina böcker"
    Then ska boken "Python för folk som hatar ormar" inte visas i favoritlistan
