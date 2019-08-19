**kore.ai**

# KnowledgeGraphGenerator
Use Kore.ai's Knowledge Graph Generator to automatically extract terms from FAQs, define the hierarchy between these terms, and also associate the FAQs to the right terms.

[Overview](#Overview)<br> 
[Prerequisites](#Prerequisites)<br>
[Configuration Steps](#ConfigurationSteps)<br>
[Run KnowledgeGraph Generator](#Run)<br>

## Overview

Kore.ai KnowledgeGraph Generator enables you to cut down your effort in building ontology in Knowledge Collection section by automating this process through one single command.

In regular procedure of building KnowledgeGraph, you need to create the ontology and add questions under respective terms and create tags if necessary. The same can be replicating by just creating required input format file and running this KnowledgeGraph generator. 

Output generated through this engine can be directly imported in KnowledgeCollection and you can use the faqs after training the KnowledgeCollection. However, user should manually add synonyms if he wants to. Since the engine won't support this yet.

If you have managed your stopwords the engine will consider only those stopwords in generating the graph considering the fact that you pass JSON or CSV export directly. If CSV format from extraction type is given as input or user haven't modified hos stopword collection, Engine uses his predefined set of stopwords

## Prerequisites

* **Python 3.6.7:** The KnowledgeGraph Generator requires python 3.6.7. If you do not already have the software, download the suitable version for your operating system from here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

* **Virtual Environment:** It is preferred to use virtual environment, instead of directly installing requirements in your machine directly. Follow the steps mentioned here to setup virtual environment in your machine. Please find operating system specific instructions: [https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

## Configuration Steps

Configuring KnowledgeGraph Generator involves the following major steps:

* **Step 1:** **Download the KnowledgeGraphGenerator from GitHub :** You can find the repository here: [https://github.com/Koredotcom/KnowledgeGraphGenerator](https://github.com/Koredotcom/KnowledgeGraphGenerator)

* **Step 2:** **Activate virtual environment:** Please execute the following command with required changes in it to activate the virtual environment 
       <br> `source virtual_environments_folder_location/virtualenv_name/bin/activate`<br>
   Once the virtual environemnt is activated you should see virtual environment name at the start of every command in the console. Something like this
   ![Image alt text](https://github.com/Koredotcom/KnowledgeGraphGenerator/blob/master/blob/venv.png)
   
* **Step 3:** **Install requirements for the project:** Please run the following command from your project root directory (KnowledgeGraphGenerator) to install requirements
   <br> `pip install -r requirements.txt`<br>
    Run <br>`pip list`<br> command to verify is all the installed requirements

* **Step 4.** **Download spacy english model:** Run following command to download the model 
     <br>`python -m spacy download en`<br>

## Run KnowledgeGraph Generator

The command which generates KnowledgeGraph have options which need to be passed while executing the command. The following are the options which are used.
**Note: : The options which are listed as mandatory should be given along with  command, for options which are regarded as optional, the default values mentioned will be picked**

<table>
       <tr>
              <td> Option name </td>
              <td> Description </td>
              <td> Mandatory / Optional </td>
              <td> Default value </td>
       <tr>
       <tr>
              <td>--folder_path </td>
              <td> Output folder location to store the generated graph JSON file </td>
              <td> Optional </td>
              <td> /data/FAQ/AoStorage/ </td>
       </tr>
       <tr>
              <td> --file_path </td>
              <td> Input file location </td>
              <td> Mandatory </td> 
              <td></td>
       </tr>
       <tr>
              <td> --language </td>
              <td> The language in which questions exist </td>
              <td> Optional </td>
              <td> en (english) </td>
       </tr>
       <tr>
              <td> --type </td>
              <td> The type of input file 
                     <ol>
                            <li>json_export</li>
                            <li>csv</li>
                            <li> csv_export </li>
                     </ol>
              </td>
              <td> Mnadatory </td>
              <td></td>
</table>
