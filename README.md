# Loan-Calculator
Implemented a loan calculator, through the command line.
#Command example
__**python creditcalc.py --principal=1000000 --periods=60 --interest=10 --type diff**__    
`    -----_This command will help you find the differential payment on a loan.`_

--type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, you will see the error message.  
--payment is the monthly payment amount.
--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided.