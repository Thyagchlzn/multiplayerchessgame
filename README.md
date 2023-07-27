<br/>
<p align="center">
  <a href="https://github.com/Thyagchlzn/multiplayerchessgame">
    <img src="https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/res/img/icons.png?raw=True" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">Multiplayer chess game  </h2>

  
</p>



## About The Project

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/main.png?raw=True)
</br>
This project is based on the client-server model using TCP protocol and the uses  Pygame for the GUI. 

1. **Client-Server Model:** The architecture is based on the client-server model, where clients (players) connect to a central server to play the game. The server handles communication between clients, manages game sessions, and enforces rules.

2. **TCP Protocol:** Transmission Control Protocol (TCP) is used for communication between clients and the server. TCP ensures reliable and ordered delivery of data, making it suitable for real-time applications like online gaming.

3. **Pygame for GUI:** The graphical user interface (GUI) is implemented using Pygame, a popular Python library for game development. Pygame provides the necessary tools for creating interactive and visually appealing game interfaces.

4. **Privacy-Oriented Approach:** The project allows users to play the chess game without the need to disclose personal information like email, phone number, or date of birth. This privacy-oriented design can attract users who are concerned about sharing personal data online.

5. **Limited Player Capacity:** The server enforces a maximum limit on the number of players allowed to connect simultaneously. This constraint ensures that the server can manage resources efficiently and maintain a smooth gaming experience.

6. **Unique Player Identification:** Each player is assigned a player ID, which serves as their unique identifier during a gaming session. This player ID is used for entering lobbies, sending requests to other players, and identifying users during gameplay.

7. **Dynamic Player IDs:** Player IDs change every time a player reconnects to the server. This approach adds an extra layer of privacy and anonymity to the gaming experience, as users get new identities upon reconnection.

8. **Move Validity and Server Validation:** The server ensures the validity of moves before forwarding them to other players. This validation prevents cheating and ensures that the game proceeds fairly and accurately.

9. **Maintaining Game State:** The server is responsible for maintaining the current state of the chess game and synchronizing it across all connected clients. This ensures that all players have an up-to-date view of the game board and can make informed decisions.

### Prerequisites



```sh
pip install pygame

```

### Installation


 Clone the repo

```sh
git clone https://github.com/Thyagchlzn/multiplayerchessgame.git
```

### Working

* **Online mode**

1. Go to the "online" menu
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/mainmenu.png?raw=True)


2. Enter the server address
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/connectingtoserver.png?raw=True)


3. Chose a specific player with the help of playerid and send request
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/onlinelobby.png?raw=True)


4. If the opponent accepts your request ,match will start
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/twoplayersplaying.png?raw=True)

*  **Administrator**

1. Remove players  using their playerid 
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/server2.png?raw=True)
                                

2.  Temporarily freezing inclusion of players 
<br/>

![Screen Shot](https://raw.githubusercontent.com/Thyagchlzn/multiplayerchessgame/main/snapshots/server3.png?raw=True)
                                


**NOTE:**
  * Use refresh to update status of players
  * Request cannot be sent to players who are busy
