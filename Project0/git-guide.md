# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Copies a repository into a new directory
    - The new repository can be cloned from a local or remote repository
    - Remote repoistorys arecloned from protocols supported by Git such as ssh
    - A repository can also be partially cloned
  - `git clone git@github.com:WSU-stuff/mystuff.git`
- add
  - Adds files to the index
    - You must use this command to add and new or modified files to your index before commiting
    - Remote repoistorys are cloned from protocols supported by Git such as ssh
    - A repository can also be partially cloned
    - Your file will not be added to the repository until you `commit` the change
  - `git add test.txt`
- rm
  - Removes files from the index
    - This command will not remove files from your working directory
  - `git rm test.txt`
- commit
  - Record the change to the repository 
    - This command will commit the current contents of the index to the repository
    - A log message describing the changes to the repository is included with the commit
    - You can use the -m argument to write the commit message in the command line
  - `git commit -m "Added readme.md"`
- push
  - Upload the content of the local repository to a remote repositroy 
    - You can push to a specified branch by using the following `git push <remote> <branch>`
  - `git push my_stuff beta_branch`
- fetch
  - Fetch is used to bring your local copy of the remote repository up to date
    - When you use the fetch command, it will download the remote contents of your repository and leave your current repository intact.
    - You are able to fetch from multiple repositories and specific branches.
  - `git fetch my_stuff beta_branch`
- merge  
  - Merge is used to join two or more development histories together
    - If the merge results in a conflict you can use `git merge --abort` to abort the merging and try to reconstruct the pre-merge state
  - `git merge beta_branch`
- pull
  - The pull command fetches and the remote repository and automatically merges it with your local repository
    - If the branch you are pulling to is behind the remote branch, the branch will be fast-forwarded to match the remote.
    - If the branches you want to pull to has diverged from the remote branch you will need to specify how to reconcile the divergence with `--rebase` or `--no-rebase`
  - `git pull --rebase beta_branch`
- branch
  - Branch is used to create, delete, and list branches of your repository
    - If the `--list` argument is used, all exisitng branches will be listed
    - The `-d` argument is used to delete branches. The branch can not be deleted if it contains unmerged changes
    - To create a new branch, you would use `git branch <name-of-new-branch>`
    - The `-m` argument can be used to rename a branch
  - `git branch new_branch`
- checkout
  - Switches branches or restores working tree file
    - The `-b` argument can be used to create a new branch and immediately switch to it
  - `git checkout new_branch`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - This folder contains all the information related to the projects commits, checkouts, remote repository address, etc. 
    - This folder contains details on every single change made. This information can be used to rollback changes.
    - This folder is hidden to prevent accidental deletion. If this folder is delete you will be unable to rollback changes.
- .gitignore file
  - This folder specifies intentionally untracked files to ignore
    - .gitignore uses globbing patterns to match file names against the .gitignore file
    - It is possible to force an ignored file to be commited by using the `-- force` option with `git add`
- ~~.git/hooks~~

## GitHub

- Pull requests
  - Pull requests helps you collaborate with others by allowing you to discuss and review changes before they are merged into the base branch
    - A pull request will create a review page that shows an overview of the changes between your branch and the base branch
    - You can push commits from your branch directly to your existing pull request. These commits will appear in chronological order
    - Other contributors can review the changes, leave comments, and add their own commits to the pull request
    - After you are happy with the changes, you can merge the pull request with your main branch
   
- SSH authentication to repositories
  - You can use Secure Shell Protocol (SSH) to access and make changes to a repository 
    - When you authenticate with SSH, you use a private key on your local machine to securely connect to the remote repository
    - You can also use HTTPS to connect to the repository, but this is not recommended as it is worse for automation and is not as secure as a SSH.
    - You can easily create a SSH key in your terminal by using `ssh-keygen -t ed25519 -C "your_email@example.com"`
    - You will then add your public key to Github by going to Access > SSH and GPG Keys > New SSH Key. Here you will paste the public key into the key field and create a title for the key  
- ~~Actions~~

## Resources I Used

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Atlassian](https://www.atlassian.com/git/tutorials)
- [Github Docs](https://docs.github.com/en)
## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0

