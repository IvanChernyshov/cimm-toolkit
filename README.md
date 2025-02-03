# Online Textbook on the Technical Aspects of Chemoinformatics

Welcome to the repository containing the source code for an online textbook dedicated to the technical aspects of chemoinformatics and molecular modeling. This open-access resource is designed for master's students at ITMO University enrolled in the "Chemistry and Artificial Intelligence (https://en.itmo.ru/en/viewjep/2/108/Chemistry_and_Artificial_Intelligence.htm)" program. The content of this textbook is developed by the dedicated team at the "Center for AI in Chemistry (https://scamt.ifmo.ru/science/groups/center-or-artificial-intelligence-in-chemistry/)" at ITMO University.


## What It Is

This textbook does not cover descriptions of chemoinformatics algorithms, examples of using chemoinformatics tools, or the theory and practice of machine learning. Instead, it focuses on the technical knowledge essential for successful work in the field of chemoinformatics.

The textbook addresses the following topics:

- Fundamentals of working in Linux

- Methods for publishing Python code and datasets

- Basics of web scraping

- Tools for extracting information from texts, including PDF files

- Automation of quantum chemical calculations for generating computational datasets


## Who Will Benefit

This textbook will primarily benefit newcomers to chemoinformatics and IT, as it serves as a convenient compilation of materials that are readily available online but may be challenging to find for those less experienced in the field.

For experienced users, it can serve as a handy reference guide and a source of code snippets for quick copying (though ChatGPT may prove to be a better alternative).


## Compiling textbook

To generate the HTML version of the textbook, please install the necessary dependencies and run the `make` script:

```ssh
> cd docs
> pip install -r ./requirements.txt
> make html
```

This will create the HTML-formatted textbook in the `docs/build` directory.


## Pull Requests

When submitting pull requests, please separate the creation of new content from the editing of existing material. For edits, follow the *"one document = one pull request"* rule.

We also encourage experienced chemists and cheminformaticians to submit pull requests on topics that are not covered in this textbook. Your knowledge and expertise can greatly enrich this resource and assist others in the field.

Thank you for your interest and support!

