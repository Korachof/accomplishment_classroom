# Main Requirements

This details the requirements needed to create Accomplishment Storefront. The point of this document is to build the requirements from both a bottom up and a top down approach. From there, a pseudo design document will be created to detail the features for the game, as well as possible future features.

Accomplishment Storefront is a light marketplace game that asks the player and the protagonist to work together to reach each other's goals. For the protagonist, their lifelong goal is to build a store that everyone will want to shop at. A place where everyone will find what they want and need, and that can serve the community in its strange ecosystem. They also have a goal of collecting every item in the Dungeon Journal, an ancient item that they were gifted by their grandfather.

For the player, they will provide goals to accomplish ranging from fairly small, to long-term mega goals. Overtime, they will also input in media they finish in real life (books read, video games finished, movies watched, television season complete), as well as events they attend. Accomplishment Storefront will not only serve as a place to store and remember all of your accomplishments and all things you finished and events you attended, but it will use these accomplishments to build the player's access to uncommon and rare items to acquire. 

This means that the protagonist and the player will become soul-linked, each helping the other accomplish their goals. 

The first iteration of the game will be entirely text-based. 

The second iteration will use sprite pictures in the Dungeon Journal and in item descriptions to add a visual for the  items. 

The third iteration will begin work on revising it into a 2D sprite-based inventory management game. 

<b>Iteration One Requirements</b>
<br>(Each of these will require their own set of requirements)
<br>Text-Based UI
<br>Player Login
<br>Player Password
<br>Player Save Capability 
<br>Unintrusive Save & Exit Button
<br>Unintrusive Help Button
<br>Player Goal Hashmaps
<br>    - Easy Goal
<br>    - Medium Goal
<br>    - Hard Goal
<br>Player Hub/Menu
<br>Script that greets player
<br>Merchant Menu
<br>Container for Player Inventory
<br>Container for Player Accomplishments (hashmap?)
<br>Class for items to sell/buy
<br>    - Name
<br>    - Category
<br>    - Description
<br>    - Buy_Value: Tuple (min, max)
<br>    = Sell_Value: Tuple(min, max)
<br>Class for NPC 
<br>    - Name
<br>    - Type
<br>    - Class
<br>    - Main_Interest
<br>    - Second_Interest
<br>    - Moneyline: Tuple (min, max)
<br>    - Schedule: hashmap (ex: {1: 0.5}: Available 1st day of week, 50% of time.)
<br>    - Impulse_Buy_Rating: INT 1-5 (1 = doesn't purchase often, 5 = impulse shopper)
<br>Item Database
<br>Container for Dungeon Journal (player items unlocked)
<br>... will add more in the near future


