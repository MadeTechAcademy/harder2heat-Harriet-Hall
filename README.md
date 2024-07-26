[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WI6KUGd1)
# Harder2Heat

In bootcamp, you explored and created an MVP which displayed how you are able to use 3rd party information to show which homes are difficult to heat. A local government in France has heard what you've done, but you need to make some changes for the pitch-and correct some bugs.

This checkpoint is aimed at seeing how well you can:

- Use TDD principals to implement features on existing code
- Develop code using Clean Code Principals (heavy emphasis on encapsulation, resuability, and readability)
- Expand your knowledge of TDD with mocking and other DD frameworks
- Share and advocate for TDD within your project

Please keep these in mind as not enough evidence will mean you need to repeat this assignment, or not receive your intended mark. **Please ask if you're usure!**

After creating the venv, you can run the app via `flask run`

## Part 1-This Looks Familiar... :star:
*Completing this will allow you to pass the checkpoint*

After running the app, you should see on the page how many properties should be available; as you may notice, there are no tests. How can you confirm this is the correct number?

Once you have done that, here are some other outstanding tickets:


- [ ] Here's a list of the features needed for the demo:
    - The full list of the property coordinates (to be able to sketch the property on the map)
    - The size of the property in metric
    - The OSID
    - When the building age was updated
    - Connectivity; however instead of 'Standalone','Semi-Detached', and 'End Connected', it should read 'Free-Standing','Dual-Connected' and 'Single Connected'

    There should be a mix of both E2E and Unit testing to cover these cases. You should aim to have an average of 80% coverage between the two

- [ ] As your implemented the above features, think carefully how you can implement new changes whilst improving code readability, encapsulation and reducing data leakage. Here's some examples:

    - In `utils.py` there's `i in range` and `j in range`. Looking at them now, is it clear what they do? 

    - What's the role of `Property`? Can you say it has one job? Are there other objects that should be present (hint: yes)? Can the principle of composition be useful in future adaptations?

To be successful you need to improve the encapsulation and readability of this code by 30%.


## Part 2-If It Walks Like a Duck... :star::star:
*Completing this _and_ part 1 will allow you to pass the checkpoint with a merit*

This week we explored the merits of mocking and other ways to do developing code

- [ ] On your project, document your use of a mocking framework and submit evidence of your use of mocking in a feature or to fix a bug. 

- [ ] This European local government would like to know if they can use their API with this app. The API will be able to send information like number of floors, and distance to public transport in meters. Create a branch in your project to demonstrate using a mocking framework of how you would test this implementation.

- [ ] Using a BDD or other framework, rewrite the tests done in part 1. 


## Part 3-Be the Change :star::star::star:
*Completing this _and_ part 2 will allow you to pass the checkpoint with a distinction*

Hopefully by now you should appreciate the benefits of TDD, and you want to share the message with non-developers

- [ ] Show a non-dev (user researcher, delivery manager etc.) the tests written in part 2 with your new framework. How easy is it for them to understand what the code should do? What improvements can be made?

- [ ] Document how you are sharing TDD either with non-developers on your team or developers new to TDD. It must be clear they are new, to TDD, and include how you are working with them, and what test they have written.