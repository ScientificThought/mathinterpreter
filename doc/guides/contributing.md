# mathinterpreter

This project was created to showcase applications of software engineering techniques and is currently closed. Nevertheless, you find below a guide that can be adapted or used in any other project with similar scope.

## Contributing code

There are many ways to setup a developing environment. We show how to do it using a recommended procedure that must work in most systems. If it doesn't work for you and your setup, please create a new issue.

You start by jump into the folder you use to develop your projects and inside this folder create a new directory called `mathinterpreter-dev`. Next you will create a new virtual environment inside this folder and activate it, as follows:

```bash
mkdir mathinterpreter-dev
cd mathinterpreter-dev
python -m venv env
. env/bin/activate
```
Then you will `git clone` this project using:

```bash
git clone https://github.com/ScientificThought/mathinterpreter.git .
```
and subsequently install the package you just download using `pip`:

```bash
pip install -e .[dev]
```
Note that we used  `-e` for *editable installation*, so that you can edit your changes and test it without needing to reinstall the package, and the option `.[dev]` is used to include dev dependencies into the current directory.
After this you are ready to go, run `pytest` to check if tests are passing on `main` branch. 

You can now find any or many issues of your interest, propose a new features (but please, remember to create a new issues for them), and so one. Once a development environment is setup you don't need to repeat this procedure again. Any work is going to be done on new branchs. It is possible that it will be necessary to update your development branch and also the main branch as you start work on this project to reflect changes made by others and this will be discussed later.

Below the list of steps for contributing are presented in more detail. 

### Creating branches, stagging and commiting code

Choose an adequate name for your branch and create it using:
```bash
git branch fix_problematic_issue
```
Note that the branch name doesn't need to be so much special as you are possibly going erase this branch later after getting your code changes incorporated into main. Now you make all code changes using the code editor of your choice. 

As recommended by Test-Driven Development, if you are proposing a new feature or fixing a previously unnoticed bug your first step will be to create a new test, which will fail at first and pass after your fix. Remember to call `pytest` in the terminal to check whether tests are passing or failing after each effective change.

After doing your changes add your work to the git stagging area. If you worked on a single file or in many files and want to include all of them in your commit, go to the project root directory and type:
```bash
git add .
```
In case you made changes to many files but only want to include those in a single file to the commit, specify it using:
```bash
git add address/to/changed_file.py
```
Now, commit your changes with a reasonable message. Do not forget to mention the issue your are solving, numbered `xyz` in the example below:
```bash
git commit -m "Fix problematic issue #xyz"
```

Suppose you are finished and want to contribute to the repository. It's is time to push your changes.

### Pushing your changes to remote for the first time
If this is your first push to the remote repository you will need to create a remote branch, which in this case is named `origin`. There are more than one way of doing this but the command below does the job:
```bash
git push --set-upstream origin fix_problematic_issue
```
But then you checkout immediately so that you do not make any changes on this branch by mistake.
```bash
git checkout main
```

### Doing the Pull Request (web approach on GitHub)
Now navigate to the GitHub repository and you will see a big green button "Compare & Pull Request". 
Click on it and you will be redirected to a Pull Request Form. Fill it, and click "Submit Pull Request".

Now it us up to the mainteiners to accept your code, refuse it, or ask you to make changes. Be patient, as you are working in a distributed context it is possible that the person responsible for looking into your PR is working on something else. In the mean time between you submitted your PR and received an answer, it is possible that the main branch of the remote repository changed. What do you do in this case? That is what I explain in the next section.

### Updating a branch to reflect changes in remote repository

Suppose someone update the remote repository and  you are no longer up-to-date with the contents implemented there and you want to incorporate those changes in your branch. It could be either your development branch or your main branch. What do you do? A good place to start with is this post from Atlassian about [`git fetch`command](https://www.atlassian.com/git/tutorials/syncing/git-fetch). But in a short explanation, you locally have a copy of the remote repo and you can update this copy by doing a fetch. Next you have to incorporate those changes into your local copy, by doing a merge. The resulting procedure presented next.

To download all remote branchs from the remote server `origin` with a copy on your machine, use:
```bash
git fetch origin
```
Then you merge those new remote data with your `current_branch` using:
```bash
git checkout current_branch
git merge origin/main
```
If there is any merge conflict, git will ask you to resolve that and open up the default editor for you to decide how to fix the merge conflict! This is a little bit more complicated and [this referrence can be useful](https://support.atlassian.com/bitbucket-cloud/docs/resolve-merge-conflicts/). Since this is a very small project, it will possibly not happen, follow the reference that was just indicated.

### Subsequent pushes
It is common that after you created your Pull Request you change your mind and decide to take another approach to solve the problem or suppose you were doing a documentation contribution and just decided to create another sentence to explain bether a certain point. It turn out that in this case you will need to checkout your development branch again, change some code, stage and commit those changes.

The same should happen if a reviewer asks to make some changes in your code. If you did what was asked you to do before you would be now on the `main` branch and will need to checkout again in your development branch, using:
```bash
git checkout fix_problematic_issue
```
Now fix your code, commit, and push it again:
```bash
git commit -m "Use different approach to fix #xyz"
git push
git checkout main
```
Note that you don't need to `--set-upstream` anymore because you already created a remote branch. At this point there is no need to do another Pull Request, the git server on the remote repository understands that any commit you push on that branch 
will be part of the PR you asked before.

# Deleting remote and local branchs (after a PR is merged, for example)

After your PR is accepted you may want to clean your local environment by deleting the branchs of the PR. This is particularly important if you make a few PR per day, in a week of work you can be loaded with more than a dozen branchs. On large projects this is important to avoid disk usage (maybe someone just put some big data file or a video there by mistake without properly configuring git), but it is also important on small project to reduce cognitive overhead. 

In this case what you need is to delete those branches! To do it locally, move outside of the branch you want to delete and use:
```bash
git branch -d branch_name
```
The remote branch can be deleted in a straightforward manner using the GitHub web interface, but you can also delete it using the terminal as described on this blog [post](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/).





