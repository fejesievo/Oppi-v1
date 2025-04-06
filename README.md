> This is the [Red Devil Hackathon](https://reddevilhacks.github.io/) markdown submission template. Replace *italicized* placeholders with your project details and remove the markdown quotes as well.

> Here are some example submissions from Boosung's previous hackathons: [Frody](https://devpost.com/software/temptemp) and [Albatross](https://devpost.com/software/albatross).

# *OPPI*
### *It is a Realtime Voice AI that talks on a call with you, giving you realtime time answers to what you speak*
**Team:** *Pranav, Fej, Anne, Fedya*

**Submission video:** *Link to video.*

Our video had some issues but we submitted it to Prof. Goble, just in case we miss the deadline.

> ⏱️ The video should be 5 minutes or less. In the video, you should include the project inspiration, what it does, and a demo showcasing the key features.

> 🎥 The easiest way to make a video here would be to use OBS or Zoom for screen recording. You can upload the video as an unlisted video on YouTube and add the link here.

## Inspiration
*Inspiration to our project was eliminate human labor for booking or reserving appointments, however, it was a 12hr hackathon and due to time constraints we decided to make a Realtime Voice AI that can talk to the user and also can have added facility to extract data to book appointements if given API access and framework.*

## What it does
*This project is a real-time voice assistant powered by Twilio and OpenAI's GPT-4o. When a user receives a Twilio number, they can talk and get connected to a live AI assistant via a WebSocket media stream. The assistant listens to the user's speech, processes it in real time through OpenAI's Realtime API, and responds with AI-generated speech. It uses FastAPI to handle HTTP and WebSocket routes and supports streaming—receiving audio from the caller and sending back AI-generated audio in response. The assistant is designed to be friendly, graceful, and a bit playful, with support for jokes and interactive conversation.*

## How we built it
*Like mentioned above it is powered by Twilio and OpenAI's GPT-4o. It uses OpenAI's API key to access the OpenAI's Realtime API facility. Here, we have Twilio's number, which is gonna call the user on their number. It listens the user's speech and processes it in real time through OpenAI's Realtime API and responds with the generated speech. We use Python as our primary language and use FastAPI to handle HTTP and WebSocket routes. We created functions that support receiving audio from twilio and getting them processed through OpenAI's API and returning them back to the user using speech.*

## Challenges & Accomplishments
*What were the biggest challenges your team faced during the hackathon? How did you overcome them?  
Also share your proudest accomplishments—what worked well, or what are you most proud of? What is something new you learned?*

The biggest challenge our team faced was to get the OpenAI API to start working. We faced several issues regarding that accessing audio and sending them to the API. Moreover, our websocket object had some problems and It was not using the ".open" and .get() attributes, which restricted OpenAI API to send the speech back to the user. To accomplish that we had to change the version of the websocket dependencies and try it out using a different attributes and functions. We were most proud of the edit we made in the function to get info from the json file because that made our project work at the end. 

## What's next?
*What's next for the project? Are there any improvements, features, or long-term goals for this project? How might you go about doing so?*

We decided that we gonna some more functionality in the Voice AI so that it can extract data from the user, check that on a database and check if a person can book or schedule any appointment. Furthermore, we also think of using Google API to actually adding those meetings/work on the google calender. Plus, we also think using the same idea we can build better library or media center structure for students to reserve rooms or collect books or equipments. 

## Try it out
*Include setup instructions so that judges (and others) can run your project locally. The judges must be able to run your application.*

Our Code was working on a demo app that we access through our Twilio account and by the time you might accessing it, our trial account might not give an access to it. We didn't create a web-app or Mobile-app for the AI because Twilio already provided it with the account. However the video would give you a good sense of how it is working. We can either make it call through the app/idle or call it yourself to turn it on. I am afraid that the API won't be functioning since it also uses our credit card to function and might be able to run if tried from your end (We might take back the access). However, if you want us to show you how it works we can definitly set it up for you to witness. 

```bash
# Example
git clone https://github.com/your-repo.git
cd your-repo
npm install
npm start
```

```bash
# Example 2
# 1. Clone the repository
git clone https://github.com/your-repo.git
cd your-repo

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python main.py
```
