Feature: Visa information på webbplatsen
  Scenario: Visa titel och välkomstsektion på startsidan
    Given att användaren öppnar startsidan
    Then ska titeln "Läslistan" visas högst upp på sidan
    And rubriken "Välkommen!" visas
    And texten "Sidan för dig som gillar att läsa. Välj dina favoriter." visas
