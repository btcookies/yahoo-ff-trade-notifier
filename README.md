# yahoo-ff-trade-notifier

## Architecture

General idea here is to pull a list of leagues last 50 transactions every 5m, pull the id of the latest transaction from s3, report all transactions newer than the latest transaction to GroupMe, store new latest transaction in s3.

To report the latest transaction to GroupMe we can just loop through the list of transactions, format the message, and send the messages to the GroupMe.
