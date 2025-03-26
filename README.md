# Advanced Prompt Engineering Workshop

Welcome to the Advanced Prompt Engineering Workshop. Follow these instructions as part of an AWS organized event:

## Step 1- Workshop Studio AWS Account access
For this workshop you’ll get access to a temporary AWS Account already pre-configured for you.

1. Obtain the event access code from the instructor.
   - Your Access Code is: **060f-07ec80-e0**

2. Sign in via the Workshop Studio join url: https://catalog.us-east-1.prod.workshops.aws/join?access-code=060f-07ec80-e0

![image](https://github.com/user-attachments/assets/ee3a5977-34e0-4c50-bc63-0ea377624be3)
![image](https://github.com/user-attachments/assets/92cba8d6-2b6d-4741-bc3c-34ccf432501d)

3. Review the terms and conditions associated with this event, and then click **Join event**.

![image](https://github.com/user-attachments/assets/633149ff-f19e-4fa1-bbf4-362ce2bf8141)

4. After joining the event, you should see the page with event information and workshop details. You should also see a section titled AWS account access in the left navigation bar.

5. Click on **Open AWS console**. This will open the AWS Management Console home page. 

6. Do not change the AWS region, keep it as the default (us-west-2).

7. Note: The AWS account will only be available for the duration of this workshop. Backup any material you wish to keep.


## Step 2 - Configure Amazon Bedrock Model Access
Next we allow access to the relevant language models available as part of Amazon Bedrock.

1. On AWS Console, Use the search bar to navigate to Amazon Bedrock

![image](https://github.com/user-attachments/assets/5f5a3c0e-4f78-493e-8505-26e74e5b7e26)

2. Within Amazon Bedrock, on left menu, click on **Model Access**

![image](https://github.com/user-attachments/assets/1733a972-f31d-4a83-9849-f894ba9bcf6d)

3. On the model access screen, select only following models and click on "Next" button followed by "Submit":

- Claude 3 Sonnet
- Claude 3 Haiku
- Mistral Large


## Step 3 - Amazon SageMaker Studio Access
Amazon SageMaker Studio is a web-based, integrated development environment (IDE) for machine learning. We will use JupyterLab for browsing and executing Python code.

1. Inside AWS Management Console, under Services search for Amazon SageMaker AI and Click on it

![image](https://github.com/user-attachments/assets/7099c9ae-d2b5-44f1-8ec4-52eb27340245)

2. On the left side navigation, click on the **Notebook**, select **Notebook instances**

3. A SageMaker Studio Notebook instance called _PromptEngWithAnthropicNotebook_ should already be provisioned. Click on **Open JupyterLab* (on the right side of the Actions column).

![image](https://github.com/user-attachments/assets/f3473ec3-4b1e-42a3-81be-904f22b7ccc2)


## Step 4 - Clone the Code and Start Working

1. Navigate to the root of the file system:
   ![image](https://github.com/user-attachments/assets/d704ca8a-62e3-4634-bdc7-ffdba60efd9e)

2. Click the Git icon and click on **Clone Repository**:
   ![image](https://github.com/user-attachments/assets/0466a45f-6b82-4ee9-89f5-59ed60757101)

Paste the repository URL and click on **Clone**:
```
https://github.com/bhorev/prompt-engineering-workshop
```
![image](https://github.com/user-attachments/assets/20b6b480-4791-4f9e-9877-143c3a8cf4a4)

3. Open the first notebook - **00_Tutorial_How-To.ipynb**
4. When opening a notebook you will be prompted to select a kernel. Keep the default (conda_python3).
   ![image](https://github.com/user-attachments/assets/8c51bcec-0e0f-4cc7-b5e4-08504f8aa14c)

5. Note: To execute a Jupyter notebook cell click on Shift+Enter or the Play button

> [!NOTE]
> If this is an AWS event, Stop here, You are ready!
