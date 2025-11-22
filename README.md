Real-Time Personal Expense Tracker

Project Title
Real-Time Personal Expense Tracker

General Description of the Project - 
This Real-Time Personal Expense Tracker is a Single-Page Application (SPA) designed to allow users to create, manage, and keep track of their personal finances in real time, securely and efficiently. A modern front-end framework has been created for it [we will use HTML/JS with Tailwind CSS in this mockup] and Google Firestore will be used to store data and provide a real-time experience by persisting data in the cloud, maintaining up-to-date data with the user across sessions.

Features- 
     1.Expense CRUD: Add, retrieve, update, and delete individual expense items.
     2.Categorization: Expenses may be labeled with pre-defined tags (examples include: Food, Transport, Bills).
     3.Real-Time Balance: Automatically calculates and shows the running total of expenses (balance) each time an expense has been added, updated, or deleted.
     4.Persistent Storage: All expense data, created within the application is securely stored and synchronized with Firestore.
     5.User Authentication: Firebase Authentication will be used for securely isolating user data (the initial auth token is provided through the environment).
     6.Responsive User Interface: Using Tailwind CSS to create a clean and responsive view for both mobile and desktop.
     
Technology/Tools Used - 
      Front-End: HTML5, Tailwind CSS, and JavaScript (ES6+).
      Database: Google Firestore (for real-time, NoSQL).

Steps to Install & Run the Project-
      1.Environment Setup: Ensure the host environment provides the necessary global variables (__app_id, __firebase_config, and __initial_auth_token) for Firebase    connection.
      2.Save the Code: Save the application code into a single file (e.g., index.html).
      3.Open in Browser: Open the index.html file directly in a web browser, or launch it within the Canvas environment.
      4.Automatic Login: The application automatically initializes Firebase and attempts to sign the user in using the provided custom token.
      5.Start Tracking: Once initialized, the user can start adding new expense entries via the dedicated form.

Instructions for Testing-
    Creation - Action: Add a new expense of $50 under 'Food'.
               Expected Result : Expected Result.
    Real-Time Read - Action : Add another entry and immediately refresh the page or simulate another user viewing the data (if multi-user).
                     Expected Result :The newly added entry and updated balance are instantly visible.
    Update - Action :Edit the $50 'Food' expense to $20 under 'Bills'.
             Expected Result : The list updates, and the total balance adjusts by $30 (reverts $50, adds $20).
    Deletion - Action : Delete one of the expense entries.
               Expected Result : The entry disappears from the list, and the total balance is correctly recalculated.
    Persistence - Action : Add an expense, close the browser, and reopen the app.
                  Expected Result : The expense entry remains visible and persistent from Firestore.
