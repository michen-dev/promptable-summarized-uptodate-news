<!-- ABOUT THE PROJECT -->
## About The Project


This is a promptable website to read summarized up-to-date news

In Detail:
- User can choose types of news AND also prompt what they specifically want to read
- Latest news are requested
- You will get a summary for each article and also a link to the original post if it is interesting for you



### Built With

* Python - Flask
* JavaScript
* HTML
* CSS
* LLMs - Ollama
* NewAPI.org




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- This project runs local LLM model with Ollama (I use granite3.2:8b)
- Articles are requested using NewsAPI service (I use NewAPI.org)

<!-- USAGE EXAMPLES -->
## Demo

<img width="1452" height="900" alt="image" src="https://github.com/user-attachments/assets/de15b04e-308f-49ca-acda-2c6dc44ae980" />
<img width="1452" height="900" alt="image" src="https://github.com/user-attachments/assets/93bfbeec-4f44-4580-ab9f-768039a01d99" />
<img width="1452" height="900" alt="image" src="https://github.com/user-attachments/assets/531ebb70-3d1b-4c50-8692-bea5315ff112" />



<!-- AIM PROBLEM -->
## Problem To Solve

This project aims to solve the difficulty of staying updated in this fast changing world

Since new innovations are constantly released while people do not have much time to find and read long blogs.
It provides a wide range of options for everyone in different fields.
It gives 5 latest relevant news which are summarized to present bullet points only.

<!-- KNOWN CONSTRAINTS -->
## Known Constraints

- Dependance on NewsAPI service: The effecient of newsAPI service significantly impacts on the website usefulness of searching for news. If the quality of searching is not high, returned articles might not satisfy the desire of users
- Dependance on AI generated content: Keywords for searching and summaries depend on AI. The respond of AI is not stable and in development phase, although it works well, unexpected result has been generated several times. The model of LLM is also a problem since the better of the model is, the stronger the local computer is required (running online is limited without subscription)

<!-- CONTACT -->
## Contact

My email: minh.chenh.contact@gmail.com

My Linkedin: https://www.linkedin.com/in/minh-chenh/

Project Link: https://github.com/michen-dev/promptable-summarized-uptodate-news




