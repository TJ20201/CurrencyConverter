# Contributing Guide
## Getting started
### Pull Requests
#### Opening Pull Requests
If you want to open a pull request, target the `unstable` branch. This branch is used for development versions and gets pushed into `stable` once a version is finished.
### Issues
#### Create a new Issue
If you find a problem with conversion, check if the issue already exists and if it doesn't then open a new issue and describe your problem.
#### Solving an Issue
If you feel like solving an issue, search through open ones until you find one that you want to fix and you may open a pull request to fix it.
### Changes
#### UI Changes
If you want to make changes to the UI, such as a new button or updating a menu then feel free to open a new pull request for the change if it doesn't exist already.
#### Currency Changes
If you want to make a change to the currency data, such as updating rates or creating a new currency, 
##### Adding a currency
First, make sure that the currency has a conversion under every other currency. (example: `GBP_ABC`) It should also have its own set of currency conversions with other currencys (example: `ABC_GBP`, `ABC_USD`, etc). Once you have confirmed it has the required conversions with correct values, create a PR for the currency.
##### Updating a currency
If you are updating a currency, for example updating its rates, edit both the target rate and all other currencies containing by it. (example: currency `ABC` was changed to a `0.001` rate for currency `DEF`, all other variables with `ABC` inside should be rechecked in case they have changed also)