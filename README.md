# Rightmove Web Scraper Project

## Overview
This Rightmove Web Scraper project originally began as a smaller component of a larger project I envisioned. My goal was to create a tool to gather information from the UK's popular property site, Rightmove, to help users understand the UK property market for both rental and buying purposes. This project represents my first endeavor into the world of programming and software development.

## Functionality
The program takes a link to a Rightmove property listing and gathers important information such as property type, price, location, and other relevant details. This information is then stored in a CSV file for easy access and analysis. By running the program with the provided link, users can quickly gather data to make informed decisions about properties they are interested in.

## Usage
To use this project, simply clone the repository and run the `requirements.txt` file to install the necessary dependencies. Then, update the `property_url` variable in the code with the Rightmove link you want to gather information from, and execute the program. The gathered data will be saved in a CSV file for further analysis.

## Techniques Used
- **Virtual Environments:** Utilized virtual environments to manage dependencies and ensure project isolation.
- **Python Packages:** Leveraged packages such as Beautiful Soup, Requests, and Pandas for web scraping and data manipulation.
- **Version Control:** Employed Git and GitHub for version control and collaboration, enabling me to track changes and manage project development.

## Limitations and Future Improvements
One of the limitations of the current implementation is the inability to scrape certain information, such as the number of bathrooms, due to challenges in locating this data in the HTML structure of Rightmove listings. I welcome collaboration and ideas for addressing this and other issues in the codebase. Additionally, an area for improvement could be the development of a user interface to enhance the usability and accessibility of the tool.

Feel free to explore the project and provide feedback or suggestions for improvement. Your input is invaluable in shaping the future development of this project.
