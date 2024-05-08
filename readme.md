## Fullstack Signup Form
This is a lightweight full stack registration app for my course, Code Camp 2024. Code Camp 2024 is a summer camp where I teach the basics of python to kids 10+ on a weekly basis. The course began on June 22nd, 2024.
## Stack
#### Frontend
- Astro + React
- JS
### Backend
- flask
- python 3.11

## App Flow
This app simply collects data from users for the purpose of getting a count of interested attendees.<br> 
#### Data is entered into the client. 
![sign up page](/assets/form.png)<br>
#### The Data is POSTed to the server. The server saves it to an sqlite3 db. 
![](/assets/api.jpg)<br>
#### The user is sent to a success page with additional info.
![success page](/assets/success_page.png)<br>
#### An admin can GET submission data and get a visual list of interested attendees.
![admin page](/assets/submissions.png)<br>