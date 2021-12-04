# Wave 👋🏼

Greeting decentralized. 

Users can now wave right from their computers with anyone they want from across their neighbourhoods to across contients! 

Wave is a simple decentralized application for test purposes of the Python Language.

# Syntax

*Note*: Users must have an account to use Wave

## /wave

Users can wave to any user they want to that has an account on Wave.

The only parameter needed that the user must have is the account hash. All hashes of each user will be printed out on the terminal for reference. 

The hashing algorithm used for transactions and contracts is the sha256 algorithm and is secured by a database in MongoDB.

Everytime a user waves, a "wave" will be made, which essentially is a transaction with a date, user, and user that had been waved to. The transaction will then be added to the global blockchain.


## /view_wave

Users can look at the number of waves and the history of waves of another user. 

Once again, similar to `/wave`, the only prerequisite is that the user must have the account hash of the user they are trying to find. However, the hashes will be printed out for reference for the user.

Wave details include the person who intially waved, the wave hash, and the date teh wave was made.


# More Information

Each user hash is comprised of the transactions, a transactions list, a random value from 100, 10000, and a date. This may be an implementation of proof of history. Moreover, the random values were done to have a unique hash along with the proof of state process.

Made in Python.
