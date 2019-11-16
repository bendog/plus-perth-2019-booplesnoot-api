# Recipe-finder project

# Task
Your final task for this week is to set up your group project repository on GitHub that you will be using for your final project. All team members should be contributing to this repository, so make sure that each team member has been added and is comfortable pushing and pulling to their local environment. A great way of testing this is to collaboratively create a Readme.txt document that each member contributes to, outlining the vision for your project, your team members, their roles and any other key information. You may also want to consider adding some 'house rules' on your Git workflow - e.g. branch naming conventions and who is responsible for merging changes to the master branch or how to deal with merge conflicts.

# Vision
Our recipe finder app recommends recipes and food pairings with ingredients you have at home to reduce food waste, use seasonal produce and save money.

# Team members & roles
  • Project manager: Francesca
  • Git manager: Beverly
  • Front End (React): Chloe
  • Front End (HTML + CSS): Ellie
  • Backend (Database): Zoe
  • Backend (Django): Roxanne

# Git workflow house rules
  • We have 2 repos: api, frontend - keep them separate for  frontend vs database
  • Key intent is to avoid merge conflicts
  • We have a master branch and a test branch
  • The master branch is the same as production and contains deployment ready code
  • No one should be working on master branch
  • The dev branch is ahead of master and contains all new code currently being worked on

  • Create a new branch for each feature or branch you want to develop i.e. 
  • Locally we will work on the dev branch and push this branch to Github repo when a feature or fix is ready and working
  • Before pushing their changes, each developer must fetch any new changes from the dev branch before pushing her new code. 
  • Pull request can't be approved until they are approved by a team member
  • Once approved, the pull request will be automatically merged
  • Can't have everyone creating a pull requests, only Git Manager
  • It is good practice to commit early and often!
  • When dev branch has been tested and is working, the Git Manager will merge this with the master branch
  • Locally we can have several feature and fix branches etc.

# Git style guide
  • Branch naming conventions: branch-type-detail-version e.g. dev-feature-apiCall-v1 | dev-fix-loginForm-v1 
  • Commmit messages: should be descriptive yet succinct e.g. add API call for recipes | fix user login form | update recipe review page
