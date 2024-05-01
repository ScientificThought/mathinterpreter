# Python - Math Interpreter

## Contributing to the development

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
git clone https://github.com/ScientificThought/py-math-interpreter.git .
```
And subsequently install the package you just download using `pip`:

```bash
pip install -e .[dev]
```
Note that we used `-e` for *editable installation*, so that you can edit you changes and test it without needing to reinstall, and the option `.[dev]` is used to include dev dependencies into the current directory.
After this you are ready to go, run `pytest` to check if tests are passing on `main` branch. 

You can now find any or many issue of your interest, proposed a new features (but please, remember to create a new issues for them), and so one. Once developing is setup you don't need to repeat this procedure again. Any work is going to be done on new branchs and, possibly, it is possible that it will be necessary to update your development branchs and also the main as you start work on this project to reflect changes made by other onto main. Below I will list the steps for contributing following steps. 

### Creating branches and contributing

Choose an adequate name for this branch, reflecting the changes you are going to make, *e.g.* `fix_problematic_issue`, and create a branch:
```bash
git branch fix_problematic_issue
```
Note that the branch name doesn't need to be so much special as you are possibly going erase this branch latter, after your fix gets incorporated into main. Now you make all code changes using the code editor of your choice. 

As recommended by Test-Driven Development, if you are proposing a new feature or fixing a previously unnoticed bug your first step will be to create a new test, which will fail at first and pass after you do your fix.
Remember to call `pytest` in the terminal to check whether tests are passing or failing after each effective change.

Suppose you are finished and want to contribute to the repository. It's is time to push your changes.

### Pushing your changes
Just push:
```bash
git push
```
But then you checkout immediately so that you do not, by mistake, make any changes to this branch. 
```bash
git checkout main
```
### Doing the Pull Request
Now navigate to the GitHub repository and you will see a big green button "Compare & Pull Request". 
Click it and you will be redirected to a Pull Request Form. Fill it, and click "Submit Pull Request".

Now it us up to the mainteiners to accept your code. Refuse it, or ask you to make changes. Be patient, as you are working in a distributed manner, it is possible that the person responsible for looking into your PR is working on something else. In the mean time between you submiting your PR and receiving an answer, it is possible that the main branch of the remote repository changed. What do you do in this case? 
That is what I explain in the next section.

### Updating a branch to reflect changes in remote repository

<!-- If the mainteiner ask you some new change, you will go to your branch again, update it to reflect any change made by others on the main branch of the remote repository.

### -->






