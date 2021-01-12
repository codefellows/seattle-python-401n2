Feature: Calculating Score

    Scenario Outline: Ones
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 1      | 100   |
            | 11     | 200   |
            | 111    | 1000  |
            | 1111   | 2000  |
            | 11111  | 3000  |
            | 111111 | 4000  |


    Scenario Outline: Fives
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 5      | 50    |
            | 55     | 100   |
            | 555    | 500   |
            | 5555   | 1000  |
            | 55555  | 1500  |
            | 555555 | 2000  |


    Scenario Outline: Normals
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 2      | 0     |
            | 22     | 0     |
            | 222    | 200   |
            | 2222   | 400   |
            | 22222  | 600   |
            | 222222 | 800   |
            | 3      | 0     |
            | 33     | 0     |
            | 333    | 300   |
            | 3333   | 600   |
            | 33333  | 900   |
            | 333333 | 1200  |
            | 4      | 0     |
            | 44     | 0     |
            | 444    | 400   |
            | 4444   | 800   |
            | 44444  | 1200  |
            | 444444 | 1600  |
            | 6      | 0     |
            | 66     | 0     |
            | 666    | 600   |
            | 6666   | 1200  |
            | 66666  | 1800  |
            | 666666 | 2400  |

    Scenario Outline: Three Pairs
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 112233 | 1500  |
            | 123123 | 1500  |


    Scenario Outline: Straight
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 123456 | 1500  |
            | 654321 | 1500  |
            | 132465 | 1500  |


    Scenario Outline: Zilches
        Given I roll <roll>
        Then I score <score> points

        Examples:
            | roll   | score |
            | 223346 | 0     |
            | 234623 | 0     |
