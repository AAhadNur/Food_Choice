# <div style="text-align:center">Lunch Voting App Database Schema</div>

<br>

This Markdown file serves as documentation for the logical database schema of the Lunch Voting App.

## Table of Contents

1. [Entities and their Attributes](#entities-and-their-attributes)
2. [Relationship between entities](#relationships-between-entities)
3. [Logical Schema Diagram](#schema-diagram)
4. [ER Diagram](#er-diagram)

<br>

## Entities and their Attributes

### User

- **UserID (PK):** Unique identifier for each user.
- **UserName:** Name or username of the user.
- **UserType:** Employee or administrator.
- **Password:** Securely stored for authentication.
- **Email:** User's email address.
- **PhoneNumber:** Contact phone number.
- **Birthdate:** Date of birth.
- **Address:** Residential or office address.
- **ProfileImage:** URL or reference to the user's profile image.
- **IsActive:** Flag indicating account status.

### Restaurant

- **RestaurantID (PK):** Unique identifier for each restaurant.
- **RestaurantName:** Name or title of the restaurant.
- **Description:** Brief summary of the restaurant.
- **Location:** Physical address of the restaurant.
- **AdministratorID (FK):** ID of the managing administrator (references Users.UserID).
- **ContactNumber:** Restaurant's contact phone number.
- **AverageRating:** Average user rating for the restaurant.
- **ImageURL:** URL or reference to an image representing the restaurant.
- **WinningStreak:** Counter for consecutive winning days.

### Menu

- **MenuID (PK):** Unique identifier for each menu.
- **RestaurantID (FK):** ID of the associated restaurant (references Restaurants.RestaurantID).
- **DishName:** Name of the dish or food item.
- **Description:** Brief summary of the dish.
- **Price:** Price of the dish.
- **Date:** Date for which the menu is applicable.

### Feedback

- **FeedbackID (PK):** Unique identifier for each feedback entry.
- **UserID (FK):** ID of the user providing feedback (references Users.UserID).
- **MenuID (FK):** ID of the related menu (references Menus.MenuID).
- **Date:** Date when the feedback was submitted.
- **FeedbackText:** Actual feedback comments or text.

### Votes

- **VoteID (PK):** Unique identifier for each vote.
- **UserID (FK):** ID of the user casting the vote (references Users.UserID).
- **MenuID (FK):** ID of the menu for which the vote is cast (references Menus.MenuID).
- **VoteTimestamp:** Timestamp indicating when the vote was cast.

### DailyResults

- **ResultID (PK):** Unique identifier for each set of daily results.
- **MenuID (FK):** ID of the winning menu for the day (references Menus.MenuID).
- **ResultDate:** Date for which the results are applicable.
- **WinningRestaurantID (FK):** ID of the restaurant with the winning menu (references Restaurants.RestaurantID).
- **VoteCount:** The total number of votes received on that day.

<br>

## Relationships Between Entities

1. **User to Feedback (One-to-Many):**

   - Each user (`UserID`) can provide multiple feedback entries (`UserID` in `Feedback`).

2. **User to Votes (One-to-Many):**

   - Each user (`UserID`) can cast multiple votes (`UserID` in `Votes`).

3. **Restaurant to Menus (One-to-Many):**

   - Each restaurant (`RestaurantID`) can have multiple menu entries (`RestaurantID` in `Menu`).

4. **Restaurant to DailyResults (One-to-Many):**

   - Each restaurant (`RestaurantID`) may have multiple daily results (`WinningRestaurantID` in `DailyResults`).

5. **Menu to Votes (One-to-Many):**

   - Each menu (`MenuID`) can receive multiple votes (`MenuID` in `Votes`).

6. **Menu to Feedback (One-to-Many):**

   - Each menu (`MenuID`) can have multiple feedback entries (`MenuID` in `Feedback`).

7. **DailyResults to Menu (One-to-Many):**

   - Each set of daily results (`ResultID`) is associated with multiple menu entries (`MenuID` in `DailyResults`).

8. **DailyResults to Restaurant (Many-to-One):**
   - Each set of daily results (`ResultID`) is associated with one winning restaurant (`WinningRestaurantID` in `DailyResults`).

<br>

### Schema Diagram

Logical schema diagram of the project database:

![Schema Diagram](https://github.com/AAhadNur/Food_Choice/blob/main/static/diagrams/schema.png)

[Diagram in Cloud](https://lucid.app/lucidchart/11fb9c5e-156f-4f18-b786-f7221886cf38/edit?viewport_loc=-56%2C-648%2C2080%2C1032%2C0_0&invitationId=inv_cceb442d-7fdb-4b2f-aff4-4aa24ca7777b)

<br>

### ER Diagram

ER Diagram of the project database:

![ER Diagram](https://github.com/AAhadNur/Food_Choice/blob/main/static/diagrams/er.png)
