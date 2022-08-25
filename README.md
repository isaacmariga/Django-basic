# Farm Hand

## Description

A website which helps you manage your farm and ensure profitability and growth through easy analysis and tracking of all your farm resources.

## Landing Page

![Alt text](/static/farm.png)

## Demo

You can demo the site **[here.](https://kuku-management.herokuapp.com/)**

## Features

- Upload new ventures
- Get expected profits
- Keep track of expenses
- Keep track of deaths
- Keep track of sales
- Store a database of customers
- Calculate and keep track of profits over time

# Specifications

## BDD

| Behavior                                                          | Input                                                                         | Output                                                              |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Users can sign up for an account                                  | Input credentials in the registration form then click Sign Up                 | Users are prompted to login into their account                      |
| Users can upload a new business venture                           | Input type and number of animals, expected sale date and expected sale amount | The venture is created                                              |
| Users can update the expenses, revenues, expenses and incidentals | Click on expenses, sales and death and input the required information         | The expected profits are updated                                    |
| Users can view the business statistics                            | click on the variable they would like information on                          | Graphs of the variable come up with more information                |
| Users keep track of sales and customers                           | Click on sales and input information                                          | Actual profit is calculated and customers are added to the database |
| Users can keep track of their business over time                  | click on profile                                                              | User will get graphs displaying their business over time            |

## Setup/Installation Requirements

Here is a run through of how to set up the application:

- Step 1 : Clone this repository using the git clone link:
  - **`https://github.com/isaacmariga/Farm-hand.git`**
- Step 2 : Navigate to the directory:
  - **`cd Farm-hand`**
- Step 3 : Open the directory created with your favorite IDE. If Atom type **`atom .`** if VSCode type **`code .`** . This will lauch the editor with the project setup,
- Now feel free to hack around the project.

## Known Bugs

- None currently.

## Technologies Used

- Python 3.10
- Django MVC framework
- HTML, CSS and Bootstrap
- Postgressql
- Heroku

### Author

**[Isaac Wangombe.](https://github.com/isaacmariga) 16/07/2022.**

## Support and contact details

Primary E-mail Address: inmariga@gmail.com

### License

_MIT License_ [![License: MIT]](license/MIT)

Copyright (c) 2019 **Isaac Wangombe**
