# unique-names
count the number of unique names in a transaction.
Given this function:
int countUniqueNames(billFirstName,billLastName,shipFirstName,shipLastName,billNameOnCard)
billFirstName - the first name in the billing address form (could include middle names)
billLastName - the last name in the billing address form
shipFirstName - the first name in the shipping address form (could include middle names)
shipLastName - the last name in the shipping address form
billNameOnCard - the full name as it appears on the credit card.
For example:
countUniqueNames(“Deborah”,”Egli”,”Deborah”,”Egli”,”Deborah Egli”) returns 1
countUniqueNames(“Deborah”,”Egli”,”Debbie”,”Egli”,”Debbie Egli”) returns 1
countUniqueNames(“Deborah”,”Egni”,”Deborah”,”Egli”,”Deborah Egli”) returns 1
countUniqueNames(“Deborah S”,”Egli”,”Deborah”,”Egli”,”Egli Deborah”) returns 1
countUniqueNames(“Michele”,”Egli”,”Deborah”,”Egli”,”Michele Egli”) returns 2
the function able to handle middle names, nicknames and typos.
available online, go search for it. You can also use external libraries as you see fit.
