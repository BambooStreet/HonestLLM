---
layout: post
read_time: False
show_date: true
title: "Installation"
date: 2023-12-09 00:00
img: posts/20231209/install_main2.png
tags: [HonestLLM, opensource project, install]
author: BambooStreet
---

This document provides a step-by-step guide for installing **HonsetLLM**. Please ensure that your system meets the requirements before proceeding with the installation.

## System Requirements

- Operating System: Windows, macOS, Linux
- Python Version: 3.6 or higher
- Other Required Software: git, pip (Python package manager)

## Before installation
You'll need the following API keys
1. [naver news api](https://developers.naver.com/docs/serviceapi/search/news/news.md)
2. [open ai api](https://platform.openai.com/api-keys)

## Installation Steps

### 1. Clone the Repository

First, clone the project's GitHub repository.

```bash
git clone https://github.com/bamboostreet/HonestLLM.git
cd HonsetLLM
```

### 2. Set Up a Virtual Environment

Create and activate a Python virtual environment.

#### For Windows

```bash
python -m venv venv
venv\Scripts\activate
```


#### For macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies for the project.

```bash
pip install -r requirements.txt
```


### 4. Configure the Project

Complete the project setup, such as setting environment variables or configuring the database.


## Usage

After completing the installation, you can run the project using the following command.


## Getting ready..
Once approved for the waitlist, it will also be available in GPT's plugin store soon!
![gpt_pluginstore](/assets/img/posts/20231209/installation.png)


## Troubleshooting

If you encounter any issues during the installation process, report the issue on [Project Issue Tracker Link](https://bamboostreet.github.io/HonestLLM/Contact.html).


--------

This document outlines the basic installation process for **HonsetLLM**. Depending on the specifics of the project, additional steps or configurations may be required. For more detailed information, please refer to the project's official documentation or README file.
