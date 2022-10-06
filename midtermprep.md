## Week 1 & 2

- create aws stack
- terminal command reminder
- users
- permissions
- ssh keys
  - private vs public
    - private is on my machine
    - public is in the cloud
  - .ssh/config
    - used to create alias to quickly connect to an instance
  - .ssh/authorized_keys
    - The authorized_keys file in SSH specifies the SSH keys that can be used for logging into the user account for which the file is configured. It is a highly important configuration file, as it configures permanent access using SSH keys and needs proper management.
  - .ssh/known_hosts
    - a file that is used to store the SSH server key fingerprints of the servers that you have connected to in the past
- git & GitHub
  
  - init
    - Create an empty Git repository or reinitialize an existing one
- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub).
    - list of files in local folder than are NOT being tracked by git.
    - list of files in local folder that have changes that need to be committed.
  - `git status`
- clone
  - Copies a repository into a new directory
    - The new repository can be cloned from a local or remote repository.
    - Remote repositories are cloned from protocols supported by Git such as ssh.
    - A repository can also be partially cloned.
  - `git clone git@github.com:WSU-stuff/mystuff.git`
- add
  - Adds files to the index
    - You must use this command to add and new or modified files to your index before committing.
    - Your file will not be added to the repository until you `commit` the change.
  - `git add test.txt`
- rm
  - Removes files from the index
    - This command will not remove files from your working directory
    - `rm --cached` the staged content has to match either the tip of the branch or the file on disk, allowing the file to be removed from just the index
  - `git rm test.txt`
- commit
  - Record the change to the repository 
    - This command will commit the current contents of the index to the repository.
    - A log message describing the changes to the repository is included with the commit.
    - You can use the -m argument to write the commit message in the command line.
  - `git commit -m "Added readme.md"`
- push
  - Upload the content of the local repository to a remote repository.
    - You can push to a specified branch by using the following `git push <remote> <branch>`.
  - `git push my_stuff beta_branch`
- fetch
  - Fetch is used to bring your local copy of the remote repository up to date.
    - When you use the fetch command, it will download the remote contents of your repository and leave your current repository intact.
    - You can fetch from multiple repositories and specific branches.
  - `git fetch my_stuff beta_branch`
- merge  
  - Merge is used to join two or more development histories together.
    - If the merge results in a conflict you can use `git merge --abort` to abort the merging and try to reconstruct the pre-merge state.
    - By using the `--commit` arguement you can perform and merge and submit a commit at the same time.
  - `git merge beta_branch`
- pull
  - The pull command fetches and the remote repository and automatically merges it with your local repository.
    - If the branch you are pulling to is behind the remote branch, the branch will be fast-forwarded to match the remote.
    - If the branches you want to pull to has diverged from the remote branch you will need to specify how to reconcile the divergence with `--rebase` or `--no-rebase`.
  - `git pull --rebase beta_branch`
- branch
  - Branch is used to create, delete, and list branches of your repository.
    - If the `--list` argument is used, all exisitng branches will be listed.
    - The `-d` argument is used to delete branches. The branch cannot be deleted if it contains unmerged changes.
    - To create a new branch, you would use `git branch <name-of-new-branch>`.
    - The `-m` argument can be used to rename a branch.
  - `git branch new_branch`
- checkout
  - Checkout is used to switch branches. 
    - The `-b` argument can be used to create a new branch and immediately switch to it.
  - `git checkout new_branch`


## git files & folders

- .git folder
  - This folder contains all the information related to the projects commits, checkouts, remote repository address, etc. 
    - This folder contains details on every single change made. This information can be used to rollback changes.
    - This folder is hidden to prevent accidental deletion. If this folder is delete you will be unable to rollback changes.
- .gitignore file
  - This folder specifies intentionally untracked files to ignore
    - .gitignore uses globbing patterns to match file names against the .gitignore file
    - It is possible to force an ignored file to be committed by using the `-- force` option with `git add`
- ~~.git/hooks~~

## GitHub

- Pull requests
  - Pull requests helps you collaborate with others by allowing you to discuss and review changes before they are merged into the base branch.
    - A pull request will create a review page that shows an overview of the changes between your branch and the base branch.
    - You can push commits from your branch directly to your existing pull request. These commits will appear in chronological order.
    - Other contributors can review the changes, leave comments, and add their own commits to the pull request.
    - After you are happy with the changes, you can merge the pull request with your main branch.
   
- SSH authentication to repositories
  - You can use Secure Shell Protocol (SSH) to access and make changes to a repository.
    - When you authenticate with SSH, you use a private key on your local machine to securely connect to the remote repository.
    - You can also use HTTPS to connect to the repository, but this is not recommended as it is worse for automation and is not as secure as SSH.
    - You can easily create a SSH key in your terminal by using `ssh-keygen -t ed25519 -C "your_email@example.com"`.
    - You will then add your public key to Github by going to Access > SSH and GPG Keys > New SSH Key. Here you will paste the public key into the key field and create a title for the key.  

### Project

- git guide

## Week 3

- crash course python notes
    - Everything is tab based
    - Declaring types is optional
    - Files end in .py. These are "scripts" run by the python interpretor
    - `sudo apt install python3` = install python core
    - `sudo apt install python3-pip` = install python module manager
    - `pip3 install -U discord.py` = correct format to install python library
- package version dependencies and usage
- APIs
    - API = Application Programming Interface
    - A library are at the code level, APIs define a set of methods through which a remote system can make use of an application's data and services
  - REST APIs
    - REST = REpresentational State Transfer
    - A philosophy that describes some best practices for implementing APIs
    - querying
    - version dependent (how queries are requested can change)
  - syncronous vs asyncronous APIs
    - synchronous means that code execution will block or wait for the API call to return before continuing
    - Asynchronous calls do not block or wait for the API call to return from the server
  - Requesting and using OAuth keys
    - Look at project 1
- authentication vs authorization
    - Authentication verifies the identity of a user or service
    - Authorization determines their access rights 
- OAuth - allow third party to do x y z
    - focus on authorization
    - You can create tokens that scope permisisons such as read/write
    - Needed when you need to idnetify users and need to indetify the project making the call

- process exploration
  - bot runs as long as starting terminal is open
  - screen / background jobs (2350) - detaching processes
  - cloud solutions?
  - containers?

### Project

- Discord Bot using Discord API w/ discord.py
- managing secrets for a project
- using branches for changes

## Week 4

- linters and unit tests
    - a program used to find "lint" i.e. format inconsistencies, basic bugs, unused variables
    - unit test = a test made by developers that the code is ran through to find logic errors, shit like that
  - Git hooks = when you run add or commit or push, you could have a script that triggered to do additonal actions
- networking review
  - IPv4 addresses
  - Subnets & CIDR notation
    - A connected group of hosts with IP addresses in a particular range
    - IP addresses consist of a network portion and a host portion
    - Network portion = logical network which the address refers to
    - Host portion = a node on that network
    - IPv4 addresses have at least 8 bits to specify the host portion & two bits to the host part
    - Netmask / subnet mask is a 32 bits specification of the network vs the host portion.  
    - /XX = CIDR Notation, where XX is the number of bits in the network portion

    
    ![cidr chart](images/cidr.png)
  - routes
    - Data is sent via a chain of subnets - at each "hop" the packet is told where to go next
    - Routing = looking up a network adderss in the routing table to forward a packet to its destination
  - gateways
    - allows packets to enter and leave your network
  - NAT
    - Network Address Translation
    - NAT allows creation ofa private subnet that get mapped to on public IP 
    - To allow private IP hosts to talk to the Internet, the border router uses NAT - intercepts packet, replaces source with valid external IP and (maybe) different source port number
    - Maintains table of mappings between internal / external address / port pairs to reverse / send back when packets arrive
  - Firewalls
    - Stateless filters check asic information like port number, IPs, protocol, of a packet to take action
    - Stateful filters maintain records of connections ora part of an existing connection
    - network wide (AWS Security Groups)
        - Inbound rules = allowed subnet and for which ports might be listening in the network. Must be set for internal and external requests
        - What is allowed to go out from the network and where
    - per machine (iptables)
        PREROUTING are rules applied to all packets before any routing decisions are made.
        - INPUT are rules applied on packets that will be delivered locally.
        - FORWARD are rules applying to packets that have been routed but are not for locally delivery
        - OUTPUT are packets sent by the local machine.
        - POSTROUTING again are all packets but after they have been through all previous relevant chains.

    - Blacklist = default allow, define packets that ARE NOT allowed in
    - Whitelist = default deny, define which packs ARE allowed in

## Week 5

- the cloud = delivery of computing services - including servers, storage, databases, networking, software, analytics, and intelligence over the internet
  - types of cloud services
    - Public = All hardware, software, and infrastructure is owned by the provider (AWS, Azure, Digital Ocean, Google)
    - Private = hardware exists on prem or hosted by private company
    - Hybrid = A little bit of both
    - IaaS = Infrastrucute as a service
        - rent IT infrastructure - servers and virtual machines (VMs), storage, networks, operating systems - from a cloud provider on a pay-as-you-go basis. I.e EC2, Cloudformation
    - PaaS = Platform as a service
        - supply an on demand enviroment for developing testing delivering and managaing software application. i.e digital ocean, heroku
    - Serverless
        - building app functionality without spending time continually managing the servers and infrastructure required to do so
    - SaaS = Software as a service
        - Gmail, Pilot, Microsoft Office Online

  - regions
    - a physical location around the world where we cluster data centers
    - Each group of logical data centers are called an Availability Zone
    - Availability Zone (AZ)
        - one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region
        - All AZs in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between AZs
  - access management of cloud resources
    - IAM = Identity and Access Management
        - IAM allows specification of what users are allowed to do on your cloud
    - token based **authorization** can create(?) access(?) delete(?) view billing(?)
- intro to navigating AWS
  - EC2 instance types
    - the machine your instance runs on i.e. t2.micro
  - images / AMI
    - AMI = Amazon Machine Image. AMI are machine images built to work in AWS
  - VPC = Virtual Private Cloud
    - virtual network dedicated to your AWS account
  - subnet
    - range of ips in my VPC
  - gateway
    - attaches to the VPC to enable communcation between resources in your VPC and the world
  - route tables
    - set rules that determine where network traffic is directed
  - security group
    - firewall

## Week 6 / 7

- intro to contents of CloudFormation Template
  - using YAML/JSON formatted files
- system logs & service control
    - systemd = servuce manage, interface with systemctl
    - `systemctl list-units` – lists active services
    - `systemctl list-sockets` – lists sockets in memory
    - Systemctl can be used to control services – most common controls:
        - status
        - start
        - stop
        - reload – reloads configuration files
        - restart
    journalctl = query the systemd journal
        - `journalctl --since 05-11-2022 00:00:00`
- installing and configuring a webserver
  - apache vs nginx
    -     Basic architecture – Apache creates a single thread to handle each connection request, while a single NGINX process can simultaneously take care of multiple connections. 
    Performance – NGINX performs faster than Apache in providing static content, but it needs help from another piece of software to process dynamic content requests. On the other hand, Apache can handle dynamic content internally.
    - Directory-level configuration – Apache comes with .htaccess files, allowing users to make changes to their site’s configuration without editing the main server settings. Meanwhile, NGINX doesn’t support directory-level configuration.
    - Modules – Apache’s modules can be loaded dynamically, while NGINX modules need to be compiled within the core software.
    - Security – both Apache and NGINX are secure and reliable. They also have several security tools to protect a site against DDoS attacks.
    - Support – Apache and NGINX offer community support and documentation to help beginners with any issues.