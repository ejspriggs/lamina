<h1 align='center'>
    ACNH Museum Tracker 🔍
</h1>

<h2>Team Members</h2>

* Kayley Kincheloe: Scrum Master and Designer
* Edward Spriggs: Git Guru
* Mour Wagner: Database Manager

<h2>🔗 Links</h2>
<h3>Pitch Deck with Wireframes & ERD</h3>
<a href="https://docs.google.com/presentation/d/1hSvMbeh3tumd23tFobdpVU4SNaY2C3vNPDBU97DwbbE/edit#slide=id.p">Pitch Deck</a>
<br>
<h3>Trello Board</h3>
<a href="https://trello.com/b/Cb7wbZp8/acnh-museum-tracker">Trello</a>
<br>
<h3>Deployed Heroku App</h3>
<a href="https://acnh-museum-tracker-333e554cc1e4.herokuapp.com/">Museum Tracker</a>

### 📝 Description
<p>A full-stack web application that helps users track what items they've donated to their museum in Animal Crossing: New Horizons game on the Nintendo Switch.</p>

### ⬇️ Installation
If you plan on modifying the app, please follow these directions to make sure you have all the packages/settings necessary to run the app locally:
* Set up a virtual environment called '.env' by entering the following command:
```python3 -m venv .env```
* Run this command in your virtual environment to add the libraries needed to run this project:
```pip install -r requirements.txt```
* If you want to run the app locally, remove all lines in the 'DATABASE' section after 'NAME':
<img src="README Images/database-settings.png">
* You will then need to change the 'NAME' value to match your local Postgresql database
* If you plan on using a cloud database for this, replace the "DATABASE" section of settings.py with your own database information.

### 🖥️ Technologies Used
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white">


### 📷 Screenshots
<details>
<summary>Logging In</summary>
<br>
To log in, simply click the log in button and sign in with your username and password.
If you are new to the site, click the "sign up" button to create an account for future logins.
<img src="README Images/frontpage.png">
</details>

<details>
<summary>Collectibles</summary>
<br>
See how many of each collectible you have left to collect!🔍
Click on one to see a list of those collectibles!
<img src="README Images/collectibles.png">
</details>

<details>
<summary>Item Lists</summary>
<br>
View the list of items you have not collected yet. Select "Details" when you need any information on 
where or when to find that specific collectible. Select "Make Donation" when you have collected that item to move it into your museum!
<img src="README Images/list-of-items.png">
</details>

<details>
<summary>Configuration Pages</summary>
<br>
See what items you've donated to your museum. When "Remove Donation" button is clicked/pressed, the item is removed from the configuration page. The item will reappear on the index page. When the user is finished, they can click on the "Return to Main Page" button at the bottom to redirect them to the index page.
<img src="README Images/current-donations.png">
</details>

### ⚠️❌💫 Biggest Challenges
* Issues with Viewing/Confirming CSS Changes
* Building a Profile Page
* Using Django to interact with Postgresql database

### Key Learnings/Takeaways
* A stronger/better understanding of Django models and how they interact with Postgresql
* Better understanding of Python with the help of teammates, and more confident in building more Python projects in the future

### ▶️ Next Steps
* Abilty for users to view their profiles, and make changes to it. 