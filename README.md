# autmo8

autom8 is a python based Robotic Process Automation platform for developing and deploying RPA's at scale
throughout any corporation of any size.

## Getting Started

Download the autom8 folder and import the my_RPA class into any python script.

## Prerequisites

Prerequisites:
1. Have Google Chrome Installed

2. Install the following python packages:
  - selenium
  - pandas
  - glob
  - platform
  - uuid

3. Run the CheckCDriver function to download the most recent ChromeDriver from Google

4. Import the my_RPA class with the following code:
```
from autom8 import *
```

## Quick Start

To create an instance of an active RPA we must instantiate the my_RPA class like in the example provided below.

```
human_resources_bot = my_RPA("Human Resources Bot")
human_resources_bot.create_log_file()
human_resources_bot.initialize_driver()
human_resources_bot.log("WebDriver Initiated")
```

## Documenation

Docs coming soon. Stay tuned or sign up for our mailing list *here*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to @AlSweigart for inspiring this package
