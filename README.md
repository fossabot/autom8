# Autom8: Python for Robotic Process Automation

Autom8 is a high level library for creating business oriented Robotic Process Automations using Python 2.7. It currently supports both Mac OS and Windows.


Aimed at outperforming and outcosting closed sourced solutions such as Automation Anywhere or Blueprism, Autom8 consists of a central wrapper around the selenium webdriver exposing highly customized methods and functions through an efficient and easy to use API.

The package's goal is to facilitate the RPA development process and bring Python into the Intelligent Automation and Robotic Process Automation industries.

Some conveniences  provided are:
 - Robust methods to navigate business applications frontends oriented towards efficiently managing large scale Automation endeavors
 - RPA logging locally hosted or integrated with Google Cloud StackDriver (coming soon)
 - Integration with SAP scripting client (coming soon) (Windows only)
 - Documentation and examples to create robust enterprise grade RPAs using python
 - Integration with major platforms for task specific business automaions

## Getting Started


 1) Install necessary packages by running the pip command with provided requirements.txt file:
```
pip install -r requirements.txt
```

2) Make sure Google Chrome is installed on the host machine. Be prepared to run the CheckCDriver function provided in the library in order to download the most recent chrome webdriver for process automation. Running the following code will download the latest chromedriver and customize extensions optimized for RPA development:
 ```
from checkCDriver import checkCDriver
# Checks if Google Chrome Driver is found on machine. Downloads if needed.
checkCDriver()
```

3) You are now ready to use the package. Import the my_RPA class with the following code:
```
from autom8 import *
```

## Quick Start

To create an instance of an active RPA we must instantiate the my_RPA class. The instance will be the central object in our workflow and process automation.


```
human_resources_bot = my_RPA(bot_name="HR_bot", downloads_directory="timesheets")
human_resources_bot.create_log_file()
human_resources_bot.initialize_driver()
human_resources_bot.log("WebDriver Initiated")
```

A common issue in process automation is being able to efficiently identify specific elements within an html front end.

Ideally this should be done with the least lines of code possible.

This is why we have created the find_by_tag_and_attr method that iterates through every single element of a specific tag on a page and evaluates if any of the elements attributes matches the evaluation string provided. Matched elements are returned in a list.
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
