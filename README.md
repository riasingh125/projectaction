# Message Board App

## Overview
This is a simple Message Board application built using Flask and Socket.IO. The application allows users to post messages, which are then displayed in real-time to all connected clients. Additionally, there's a feature to change the font color of the message board dynamically.

## Components and Interactions

### Backend (Flask)
- **Flask App**: The main application is built using Flask
- **Socket.IO**: Socket.IO is used to enable real-time communication between the server and clients.

### Frontend (HTML, CSS, JavaScript)
- **HTML Templates**: The application has a simple HTML structure with templates for rendering the message board and handling user input.
- **CSS Styling**: The styling is done using CSS to create an aesthetically pleasing message board.
- **JavaScript**: Client-side scripting is used to handle user interactions, such as posting messages and changing font colors.
- **Socket.IO Client**: The Socket.IO client library is included to establish a connection with the server for real-time updates.

### Interaction Flow
1. Users can enter messages in the provided textarea.
2. Clicking the "Post Message" button triggers a Socket.IO event to send the message to the server.
3. The server receives the message, adds a timestamp, and broadcasts it to all connected clients.
4. Clients receive the message and dynamically update the message board in real-time.
5. The "Change Font Color" button allows users to change the font color of the message board.

## Fulfillment of Requirements
- **Real-Time Updates**: Utilizes Socket.IO to achieve real-time communication between the server and clients.
- **User Interaction**: Users can post messages, and the application dynamically updates the message board without requiring a page refresh.
- **Additional Feature**: The "Change Font Color" button provides an additional interactive feature for users.

## How to Start the Application

1. Install the required Python packages:
   ```bash
   pip install Flask Flask-SocketIO
   run the application
   click on the link in the terminal it provides
   have fun!

- **I was going to use Node.js and npm to make it a lot easier, but node.js wasn't updating/wasn't being recognized so i had to go the other route**
- **In the future, I'd probably insert a couple pictures, a navbar (hamburger and all) with different chatrooms, and maybe some cooler features like randomly placing the messages**
- **I have a css file that I don't use because I don't think my vscode recognized it as a css file, but for organization, I would typically separate css and html**
- **I also usually use react, but this functionality could have used HTML too so i did it that way**
- **I tried deploying it on GitHub pages, it didn't work because the requirements, so ignore the docs folder in the other branch it was just a tester**

