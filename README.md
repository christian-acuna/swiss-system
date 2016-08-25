### Swiss-system Game  Tournament Planner
---

This Swiss style tournament planner is built with a Python module that uses PostgreSQL database to keep track of players and matches them in a multi-player game tournament.


### About

A Swiss system is used for competitions with a large number of entries so that a full round-robin is not feasible. This non-eliminating tournament format features a pre-determined number of rounds of competition.


### What's included

Inside the directory, you'll find the following files:

    Swiss-system Tournament Planner/
      tournament/
      ├──tournament_test.py
      ├──tournament.py
      ├──tournament.sql
      pg.config.sh
      README.md
      Vagrantfile

### Prerequisites

- Vagrant
- VirtualBox


### Installation

If you don't already have Vagrant VM, download and install it on your machine.

- Fork this repo from Github and navigate the project folder
- Extract the zipped files to your Vagrant directory
- From the terminal, cd to your /vagrant directory
- Type "vagrant up" to launch the virtual machine
- Then enter "vagrant ssh" to get into the machine
- In the VM, cd to the /tournament folder
- Setup the PostgreSQL database with this command: "psql -f tournament.sql"

#### How to run
    ```
    # Start up vagrant
    $ vagrant up
    # SSH into the virtual machine box
    $ vagrant ssh

    # Go to the directory
    $ cd /vagrant/tournament
    # Launch the PSQL
    $ psql tournament
    # Import the psql
    tournament=> \i tournament.sql
    # Quit the psql command line interface
    tournament=> \q

    # Go back to the tournament directory
    $ cd /vagrant/tournament
    # Run tests
    $ python tournament_test.py
    ```
