# Autom8: Python for Robotic Process Automation

Autom8 is a high level library for creating business oriented Robotic Process Automations using the Python programming language.

Aimed at outperforming and outcosting closed sourced solutions such as Automation Anywhere or Blueprism, Autom8 consists of a central wrapper around the selenium webdriver exposing highly customized methods and functions exposed through an efficient and easy to use API.

Autom8‘s goal is to facilitate the RPA development process and bring Python into the Intelligent Automation and Robotic Process Automation industries.

Some conveniences  provided are:
 - Robust methods to navigate business applications frontends oriented towards efficiently managing large scale Automation endeavors.
 - RPA logging locally hosted or integrated with google clouds Stackdriver
 - Integration with SAP scripting client
 - Documentation and examples to create robust enterprise grade RPAs using python.
 - Integration with major platforms for task specific business automaions

## Getting Started

 - Make sure Google Chrome is installed on the host machine. Be prepared to run the CheckCDriver function provided in the library in order to download the most recent chrome webdriver for process automation.
 - Install necessary packages by running the pip command with provided requirements.txt file:
```
pip install -r requirements.txt
```
 - Run the CheckCDriver function to download the most recent ChromeDriver from Google.
Import the my_RPA class with the following code:


3. Run the CheckCDriver function to download the most recent ChromeDriver from Google

4. Import the my_RPA class with the following code:
```
from autom8 import *
```

## Quick Start

To create an instance of an active RPA we must instantiate the my_RPA class. The instance will be the central object in our workflow and process automation.


```
human_resources_bot = my_RPA("Human Resources Bot")
human_resources_bot.create_log_file()
human_resources_bot.initialize_driver()
human_resources_bot.log("WebDriver Initiated")
```

A common issue in process automation is being able to efficiently identify specific elements within an html front end. Ideally this should be done with the least lines of code possible. This is why we have created the find_by_tag_and_attr method that iterates through every single element of a specific tag on a page and evaluates if any of the elements attributes matches the evaluation string provided then the selected element is returned.
```
my_robot = my_RPA(bot_name="my_robot", downloads_directory="my_robot_downloads_folder")
my_robot.find_by_tag_and_attr(tag, attribute, evaluation_string, sleep_secs)
```
## Documenation

Docs coming soon. Stay tuned or sign up for our mailing list *here*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to @AlSweigart for inspiring this package
