## CS6388MiniProject

# Download Dependencies for this Mini Project (Installation instructions for macOS)

1. Install Node.js
 
 Run the command in a new open Terminal:
 
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh | bash
  
2. Install MongoDB with Homebrew


Run the two following commands seperately to install Homebrew first:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    brew install wget
    
Now run the next command:

    brew install mongodb-community@4.4

3. Install git with Homebrew

Run the following command:

     brew install git

4. Install Python3 with Homebrew

Run this command in the terminal:

     brew install python
     

# Download webgme-cli

Run the following command:

    npm install -g webgme-cli
    
# Start MongoDB

In a new terminal run the command:

    brew services start mongodb-community@4.4
    
 # Start the MiniProject

Open another terminal and clone the repository:

    git clone https://github.com/mollym55/CS6388MiniProject.git
 
 Now cd into the repository:
  
    cd CS6388MiniProject
