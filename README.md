# AWS Quickstart Guide & Pre-Requisites

## What and why

This is a quick start guide to install everything you need to interact with AWS via code (in this case using python).

This is achieved through installing a couple of things:
- Python & a Python IDE
- Boto3 (An SDK intended for interaction with AWS services)

## Account Creation

Follow the below guide to create a 'free-tier' account with AWS

Please note, you will need to provide card information & a phone number for the free account. You won't be charged, but please be careful if you create any services on AWS that don't fall within the 'free-tier'.

https://www.w3schools.com/aws/aws_cloudessentials_getstarted.php


Once you've created an account, you'll be greeted with the AWS landing page. You don't need to do anything else here yet but feel free to explore some services and have a read into what they do!

Some examples of simple services:

S3 - File Storage
DynamoDB - Databases
Lambda - Online IDE | Run code online
SNS - A notification service | Trigger a text/email when something happens


## Python IDE installation

You have a few options here (PyCharm, VSCode, etc)

For simplicity i'll be using VSCode, please don't use an online IDE for this such as Replit as package installation may be more complex.

Go to this link and download VSCode for the appropriate OS:
https://code.visualstudio.com/download


### Python installation

If you chose VSCode, you'll need to install python separately. (if not installed already)

you can follow this guide to install Python for VSCode:
https://code.visualstudio.com/docs/python/python-tutorial


### SDK Installation

Boto3 is a Python SDK used to interact with AWS resources through code. There's a handy documentation page for this which includes classes,  methods & code examples for different AWS services:

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

To install boto3, we can open a terminal window in your Python IDE and enter the following comand

```pip install boto3```

This should automatially install all the dependencies & the boto3 SDK

We can verify this package has installed successfully by opening your python terminal and entering

```pip show boto3```

This will show the location of the package if successful.


__Note:__ You will need python installed for pip to be available


## Generate Access Keys

This is the final step to enable interaction with AWS from your code editor. 

You'll need to follow some steps below on the AWS console to set up some access keys, they are vital for connecting to AWS and interacting with your services.

We will use a service called IAM, this is the AWS platform for managing users and access to different resources.

### Logging in

Go to the AWS sign in page and log in:

https://aws.amazon.com

Once logged in you'll see a screen like this:
![AWS Login Page](/Resources/awshome.png)

### Creating an IAM Account

Go to the search bar and type in ```IAM```

![IAM Search](/Resources/IAMSearch.png)

Click on ```Users``` just below the 'Top Features' Tab.

This will bring up a new window showing all of the current users, you'll see an empty table like this:

![IAM Users](/Resources/IAMUsers.png)

Click on the ```Create User``` button, enter a user name and click ```next```.

You'll now see a screen asking for you to set up some permissions for this account. We will keep things simple and add administrator access to our new account. 

To do this, select ```Attach policies directly``` and tick the ✅```Administrator Access``` policy.

This is shown in the image below:

![IAM Permissions](/Resources/IAMPermissions.png)

You can now click ```next``` and ```create user```

### Generating Access Keys

The last step is to get some credentials for the account you just created, essentially allowing us to 'log in' to our new account from our IDE.

To do this, just click the username of the account you just made:

![IAM User Open](/Resources/IAMOpenUser.png)

This will bring up a user page, we want to create access keys so we will go to the ```Security Credentials``` tab:

![IAM Search](/Resources/IAMSecurityCredentials.png)

Now to create the keys, scroll down to the ```Access Keys``` Tab and click on ```create access key```:

![IAM Search](/Resources/IAMAccessKeysCreate.png)

This will allow you to choose a type of key, we're after ```Command Line Interface (CLI)```, Select this and click next, just make sure to tick the box at the bottom of the page:

![IAM Search](/Resources/IAMTypeOfKey.png)

Now we are prompted to enter a description for the keys, this can be anything, see my example below and click ```Create Access Key```:

![IAM Search](/Resources/IAMNameYourKeys.png)

__The last step is important!__

You'll be prompted with an ```Access Key``` and a ```Secret Access Key``` 

There's an option to download these access keys as a CSV file

 __make sure you do!__ 
 
 Once this page is gone, you won't be able to find them again!


___

### Finished!

__Thats it!__ The hard stuff is done and you've completed the pre-requisites.

![Image](https://c.files.bbci.co.uk/157B5/production/_111398978_gettyimages-683632662.jpg)

